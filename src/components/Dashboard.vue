<template>
  <div class="hello">
   <table>
        <tr>
            <th>ID</th>
            <th>User ID</th>
            <th>Budget</th>
            <th>Desription</th>
        </tr>
        <tr>
            <td>1</td>
            <td>4</td>
            <td>1200000</td>
            <td>Realtime Face Recognition</td>
        </tr>
        <tr>
            <td>Centro comercial Moctezuma</td>
            <td>Francisco Chang</td>
            <td>Mexico</td>
        </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'DashBoard',
  props: {
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
