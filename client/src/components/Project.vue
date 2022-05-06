<template>
    <div>
        <h1>project title here</h1>

        <!-- Remove -->
        <button type="button" class="btn btn-danger mx-2" @click="add">
            Add
        </button>

        <div v-for="expense in expenses" :key="expense" class="container my-5 bg-light">
            <div class="row">
                <div class="col my-auto">


                    <p>
                        <a class="" data-bs-toggle="collapse" :href="'#collapseExample' + expense.id" role="button" aria-expanded="false" aria-controls="collapseExample">
                            <h6>{{expense.id}} {{expense.name}}</h6>
                        </a>
                    </p>
                    <div class="collapse" :id="'collapseExample'+expense.id">
                        <div class="card-body bg-light">
                            <table>
                                <tr>
                                    <td>Description:</td>
                                    <td class="fw-bold">{{expense.description}}</td>
                                </tr>

                                <tr>
                                    <td>Amount:</td>
                                    <td class="fw-bold">{{expense.amount}}</td>
                                </tr>

                                <tr>
                                    <td>Created At:</td>
                                    <td class="fw-bold">{{expense.created_at}}</td>
                                </tr>

                                <tr>
                                    <td>Created By:</td>
                                    <td class="fw-bold">{{expense.created_by}}</td>
                                </tr>

                                <tr>
                                    <td>Updated At:</td>
                                    <td class="fw-bold">{{expense.updated_at}}</td>
                                </tr>

                                <tr>
                                    <td>Updated By:</td>
                                    <td class="fw-bold">{{expense.updated_by}}</td>
                                </tr>
                            </table>
                        </div>
                    </div>



                   
                </div>

                <div class="col text-end px-auto">
                    <!-- Remove -->
                    <button type="button" class="btn btn-danger mx-2" @click="remove">
                        Delete
                    </button>
                    
                    <!-- Button trigger modal -->
                    <button type="button" class="btn btn-success mx-2" data-bs-toggle="modal" data-bs-target="#exampleModal">
                        Edit
                    </button>
                
                    <!-- Modal -->
                    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLabel">Expense name/title here</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div class="modal-body">

                                    <table>
                                        <!-- Name -->
                                        <tr>
                                            <td class="pe-3">
                                                <label for="exampleFormControlInput1" class="col-form-label">Name:</label>
                                            </td>
                                            <td>
                                                <input type="text" class="form-control" id="exampleFormControlInput1" v-bind:placeholder="expense.name">
                                            </td>
                                        </tr>

                                        <!-- Description -->
                                        <tr>
                                            <td class="pe-3">
                                                <label for="exampleFormControlInput1" class="col-form-label">Description:</label>
                                            </td>
                                            <td>
                                                <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" v-bind:placeholder="expense.description"></textarea>
                                            </td>
                                        </tr>
                                        
                                        <!-- Amount -->
                                        <tr>
                                            <td class="pe-3">
                                                <label for="exampleFormControlInput1" class="col-form-label">Amount:</label>
                                            </td>
                                            <td>
                                                <input type="text" class="form-control" id="exampleFormControlInput1" v-bind:placeholder="expense.amount">
                                            </td>
                                        </tr>

                                        <!-- Category -->
                                        <tr>
                                            <td class="pe-3">
                                                <label for="exampleFormControlInput1" class="col-form-label">Category:</label>
                                            </td>
                                            <td class="text-start">
                                                <div class="dropdown">
                                                    <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                                                      Categories
                                                    </button>
                                                    <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                                                      <li><a class="dropdown-item" href="#">Production</a></li>
                                                      <li><a class="dropdown-item" href="#">Operating</a></li>
                                                      <li><a class="dropdown-item" href="#">Financial</a></li>
                                                      <li><a class="dropdown-item" href="#">Vendor</a></li>
                                                      <li><a class="dropdown-item" href="#">Manpower</a></li>
                                                      <li><a class="dropdown-item" href="#">Software</a></li>
                                                      <li><a class="dropdown-item" href="#">Hardware</a></li>
                                                    </ul>
                                                </div>
                                            </td>
                                        </tr>
                                    </table>

                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    <button type="button" class="btn btn-primary" @click="saveEdits">Save changes</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'EachProject',
  data: function() {
      return {
          expenses : [
            {
                "id": 1,
                "project_id": 2,
                "category_id": 2,
                "name": "Server Maintenance",
                "description": "Server maintenance and upgrading work to incorporate BC plans",
                "amount": 30000,
                "created_at": "2021-11-04T16:00:00.000Z",
                "created_by": "Jacky",
                "updated_at": "2021-11-06T16:00:00.000Z",
                "updated_by": "Jacky"
            },
            {
                "id": 2,
                "project_id": 2,
                "category_id": 3,
                "name": "Server Upgrades",
                "description": "Server upgrades incorporate BC plans",
                "amount": 14000,
                "created_at": "2021-11-04T16:00:00.000Z",
                "created_by": "Jacky",
                "updated_at": "2021-11-06T16:00:00.000Z",
                "updated_by": "Jacky"
            }
        ]
      }
  },
  methods: {
      saveEdits: function() {
          console.log("save edit here")
          // call axios here and update db
      },

      remove: function() {
          console.log('delete here')
          alert("Are you sure you want to remove the business expense for this project?")
          // proceed to call axios and delete from db
      }
  }
}
</script>