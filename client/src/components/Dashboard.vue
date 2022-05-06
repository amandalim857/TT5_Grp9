<template>
  <div class="hello">
    <table>
    <tr>
        <th>ID</th>
        <th>User ID</th>
        <th>Name</th>
        <th>Budget</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>1</td>
        <td>4</td>
        <td>posb</td>
        <td>3434</td>
        <td>Hello hello</td>
    </tr>
    <tr>
        <td>2</td>
        <td>3</td>
        <td>dbs</td>
        <td>34315</td>
        <td>Hello hello hello</td>
    </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'DashBoard',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
