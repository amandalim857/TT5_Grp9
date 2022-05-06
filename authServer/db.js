const { MongoClient } = require("mongodb");

let db;

const connectToDb = async () => {
  const url =
    process.env.DB_URL ||
    "mongodb+srv://cheewengg:14MV4MGvBCDCpeYL@cluster0.9xr62.mongodb.net/authenticate?retryWrites=true&w=majority";

  const client = new MongoClient(url, { useNewUrlParser: true });
  await client.connect();

  console.log("Connected to MongoDB at", url);
  db = client.db();
};

const getDb = () => {
  return db;
};

module.exports = { connectToDb, getDb };
