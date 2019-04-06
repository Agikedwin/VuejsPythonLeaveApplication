<template>
  <v-card
    class="mx-auto"
   
  >
    <v-card-title class="title font-weight-regular justify-space-between">
      <span>{{ currentTitle }}</span>
      <v-avatar
        color="teal lighten-2"
        class="subheading white--text"
        size="24"
        v-text="step"
      ></v-avatar>
    </v-card-title>

    <v-window v-model="step">
      <v-window-item :value="1">
        <v-card-text>
          <v-text-field
            ref="currentpwd"
            color="teal lighten-2"
            label="Current Password"
            type="password"
            v-model="changePwdForm.current_password"
            :rules="nameRules"
          ></v-text-field>
          <div v-if="validCred">
              <span class="caption teal--text text--darken-1">
            This  current password  will be used to verify account
          </span>

          </div>
          <div  v-if="!validCred">
              <span class="caption red--text text--darken-1">
            The  current password  is invalid
          </span>
          </div>
          
        </v-card-text>
      </v-window-item>

      <v-window-item :value="2">
        <v-card-text>

             <v-text-field
          ref="newusername"
            color="teal lighten-2"
            label="New username"
            type="text"
             v-model="changePwdForm.new_username"
             :rules="nameRules"
          ></v-text-field>
          
          <v-text-field
          ref="newpwd"
            color="teal lighten-2"
            label="New Password"
            type="password"
             v-model="changePwdForm.new_password"
             :rules="nameRules"
          ></v-text-field>
          <v-text-field
            ref="newpwd"
            color="teal lighten-2"
            label="Confirm Password"
            type="password"
             v-model="changePwdForm.confirm_password"
             :rules="nameRules"
          ></v-text-field>
          <div>
            <div v-if="!checkpwd">
              <span class="caption red--text text--darken-1">
            The passwords provided do not watch
          </span>

          </div>
          <!-- <div  v-if="!checkpwd">
              <span class="caption red--text text--darken-1">
            The  current password  is invalid
          </span>
          </div> -->

          </div>
          
        </v-card-text>
      </v-window-item>

      <v-window-item :value="3">
        <div class="pa-3 text-xs-center">
         
         <div v-if="pwdstate==1">
             <v-icon color="teal">done_outline</v-icon>
             <h3 class="title font-weight-light mb-2 teal--text text--darken-1">Password successfully changed</h3>

         </div>

         <div v-if="pwdstate==2">
             <v-icon color="teal">done_outline</v-icon>
             <h3 class="title font-weight-light mb-2 red--text text--darken-1">Username provided already taken by another user</h3>

         </div>

         <div v-if="pwdstate==3">
             <v-icon color="teal">done_outline</v-icon>
             <h3 class="title font-weight-light mb-2 red--text text--darken-1">Unkown Errord occured</h3>

         </div>
          
        </div>
      </v-window-item>
    </v-window>

    <v-divider></v-divider>

    <v-card-actions>
      <v-btn
        :disabled="step === 1"
        flat
        @click="step--"
      >
        Back
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn
        :disabled="step === 3"
        color="teal"
        depressed
        @click="changePwd"
      >
        Next
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import api from "@/apis/api";
export default {
    

    data: () => ({
        step:1,
        validCred:true,
        checkpwd:true,
        pwdstate:0,
        changePwdForm:{
            new_username:"",
            current_password:"",
            new_password:"",
            confirm_password:""
        },

        nameRules: [
      v => !!v || "Name is required",
      v => (v && v.length >=2) || "Name must not be less than 5 characters"
    ],

    }),
    methods:{
        async checkValidPwd(payload){
            await api.addEntry("checkPwdvalid",payload)
            .then(res=>{
                if(res.data.state=='valid'){
                    this.validCred=true
                    this.validCred=true
                    console.log("test 0 ",this.validCred)
                     this.step++

                }else {
                    this.validCred=false
                    console.log("test 1 ",this.validCred)

                }

            })
        },

       async changeUserPassword(payload){
           await api.addEntry("changepwd",payload)
           .then(res =>{
               if(res.data.state=='successfull'){
                   this.pwdstate=1;
                    console.log("test 1 ",this.pwdstate)
                   this.step++

                  /*  setInterval(function(){
                       console.log("SUCCESSFULL ::::")
                       this.$router.push({name:'welcome'})
                       this.$router.push({ name: "welcome", params: { userId: "agik12345" } });
                   },3000) */
               }

               if(res.data.state=='exists'){
                   this.pwdstate=2;
                   console.log("test 2 ",this.pwdstate)
                   this.step++
                  
               }

               if(res.data.state=='Failed'){
                   this.pwdstate=3;
                   console.log("test 3 ",this.pwdstate)
                   this.step++

                   

               }
               
               
               console.log(" CHANGE ", data)

           })


        },

        comparePwd(){
            if(this.changePwdForm.new_password == this.changePwdForm.confirm_password){
                this.checkpwd=true
                this.changeUserPassword(this.changePwdForm)
            }else{
                this.checkpwd=false
                 console.log("this.checkpwd 2 ",this.checkpwd)
            }

        },

        changePwd(){
            console.log("validate  ", this.step)
        if(this.step==1){
            if(this.$refs.currentpwd.validate()){               
            console.log("the data  ", this.changePwdForm )
            this.checkValidPwd(this.changePwdForm)
            }
        }

        if(this.step==2){
            if(this.$refs.newpwd.validate()){               
            console.log("the data  ", this.changePwdForm )
            this.comparePwd(this.changePwdForm)
            }
        }

        

            
            
            
        }

        

    },
     computed: {
      currentTitle () {
        switch (this.step) {
          case 1: return 'Change your password'
          case 2: return 'Change  password'
          default: return ''
        }
      }
    }

}
</script>


