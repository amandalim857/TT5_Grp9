require("dotenv").config();
const express = require("express");
const cors = require("cors");
const bcrypt = require("bcrypt");
const { connectToDb, getDb } = require("./db.js");

const app = express();
const port = process.env.AUTH_SERVER_PORT || 5000;

app.use(express.json());

app.use(
  cors({
    credentials: true,
    origin: ["http://localhost:3000"],
  })
);

const getUserCount = async () => {
  const db = getDb();
  const result = await db
    .collection("counter")
    .findOneAndUpdate(
      { id: "users" },
      { $inc: { current: 1 } },
      { returnOriginal: false }
    );
  return result.value.current;
};

app.post("/register", async (req, res) => {
  const db = getDb();
  try {
    // bcrypt password  before storing newUser in db
    const id = await getUserCount();
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const newUser = { ...req.body, id, password: hashedPassword };
    await db.collection("users").insertOne(newUser);
    const user = await db
      .collection("users")
      .findOne({ username: req.body.username });
    res.status(201).send(user);
  } catch {
    res.sendStatus(500);
  }
});

app.post("/login", async (req, res) => {
  const db = getDb();
  const user = await db
    .collection("users")
    .findOne({ userName: req.body.userName });
  if (user == null) return res.status(400).send("User not found!");
  try {
    if (await bcrypt.compare(req.body.password, user.password)) res.send(user);
    else res.status(400).send("Incorrect password!");
  } catch {
    res.sendStatus(500);
  }
});

(async function () {
  try {
    await connectToDb();
    app.listen(port, function () {
      console.log(`App started on port ${port}`);
    });
  } catch (err) {
    console.log("ERROR:", err);
  }
})();
