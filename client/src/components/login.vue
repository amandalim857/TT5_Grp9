<template>
<div>
    <!-- nav bar -->
    <nav class="navbar navbar-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="https://www.smu.edu.sg/">
                <img src="img/dbs_logo.png" id="logo" class="d-inline-block align-text-top">
            </a>
        </div>
    </nav>
    <!-- end of nav bar -->

    <div class="container-fluid h-100 d-inline-block" id="main">
        <div class="row " >
            <div class="col-4">
            </div>

            <div class="col-4">
                <form class="login-form needs-validation" novalidate>
                    <p class="fw-bolder fs-1 text-center" style="margin-top: 10%; margin-bottom: 10%; ">
                        LOGIN 
                    </p>
                    
                    <p class="fs-5">
                        Sign in with your email address.
                    </p>

                    <div class="mb-3">
                        <label for="email" class="form-label">Email address</label>
                        <input type="email" class="form-control" id="user-email" v-model="input_email" placeholder="username" required>
                    </div>
    
                    <div class="mb-3">
                        <label for="password" class="form-label">Password</label>
                        <input type="password" class="form-control" id="user-password" v-model="input_password" placeholder="password" required>
                    </div>

                    <button type="button" class="btn btn-success d-grid w-25 mt-3 mx-auto float-end" v-on:click="checkForm()">Sign In</button>

                    <div style="margin-top: 15px;">
                        <a href="" target="_blank">Forget Password?</a>
                    </div>

                </form>

            </div>
        </div>

    </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginPage',
  props: {
    msg: String
  },
  
  data() {
        return {
            errors: [],
            input_email: null,
            input_password: null
        }
    },

    methods:{
    checkForm:function(){
        if(this.input_email && this.input_password){
            this.validate()
        }
        this.errors = []
        if(!this.input_email){
            this.errors.push("Enter your email in the format \"user@domain\".")
        }
        else if(!this.input_password){
            this.errors.push("Enter your password.")
        }
    },

    validateForm(){
        this.errors = []
        this.errors.push("Either Email or Password is wrong.")
    },

    validate(){
        console.log("=== start validate() ===")
        localStorage.setItem('email', this.input_email)
        console.log(localStorage.getItem('email')) //using this to retrieve the email
        let url = "../backend/verifyStudent.php?student_email=" + this.input_email + "&password=" + this.input_password

        axios.get(url)
        .then((response) => {
            console.log(response)
            if(response.data == 'wrong email or password'){
                this.validateForm()
            }
            else{
                // window.location.href = "./searchBooking.html"
            }
        })
        .catch(error =>{
            console.log('not found')
            console.log(error.message)
        })
    }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    #style1 {
        width: 100%;
        height: 600px;
    }
    body{
        background: #F8F8F8;
    }

    #logo {
        width: 110px;
        height: 50px;
        margin-left: 10px;
    }

    #main {
    position: relative;
    width: 100%;
    min-height: 600px;
    margin-top: 60px;

    background: #F8F8F8;
    }
</style>
