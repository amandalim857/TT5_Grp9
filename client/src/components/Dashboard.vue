<template>
  <div class="container container-fluid">
        <div class="row mt-5">

            <table class="table table-hover col-lg-12" id="center">
                <thead>
                  <tr>
                    <th scope="col">ID</th>
                    <th scope="col">User_ID</th>
                    <th scope="col">NAME</th>
                    <th scope="col">BUDGET</th>
                    <th scope="col">DESCRIPTION</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="project in projects" :key="project.id">
                    <th scope="row">{{project.id}}</th>
                    <td>{{project.user_id}}</td>
                    <td>{{project.name}}</td>
                    <td>{{project.budget}}</td>
                    <td>{{project.description}}</td>
                  </tr>
                </tbody>
            </table>

        </div>

    </div>
</template>

<script>
export default {
  name: 'DashBoard',
  props: {
    msg: String
  },

  data: function() {
      return {
          //assume the following data is obtained dynamically through Asynchronous requests
          projects: [
          {
              "id": 1,
              "user_id": 4,
              "name": "RTF",
              "budget": 12000,
              "description": "Realtime Face Recogniton"
          },
          {
              "id": 2,
              "user_id": 1,
              "name": "SWT",
              "budget": 80000,
              "description": "Smart Watch Tracker"
          },
          {
              "id": 3,
              "user_id": 2,
              "name": "ULS",
              "budget": 11000,
              "description": "Upgrade Legacy System"
          } 
          ]
      }
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
#center {
        margin-left: auto;
        margin-right: auto;
}
</style>
