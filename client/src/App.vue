<template>
  <v-app id="inspire">

    
   
    <template v-if="login">
      <v-toolbar color="teal" dark fixed app clipped-right>
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <v-toolbar-title>KEMRI-FACES EMPLOYEES LEAVE MANAGEMENT SYSTEM  </v-toolbar-title>
        <v-toolbar-items class="hidden-sm-and-down">
          <!-- <v-btn flat @click="goToDashboard">DASHBOARD</v-btn>
          <v-btn flat @click="goToStaff">STAFF</v-btn>
          <v-btn flat @click="goToSupervisors">SUPERVISORS</v-btn>
          <v-spacer></v-spacer>
          <h4>{{userLoggeInName}}</h4>
          -->
        </v-toolbar-items>
        <v-spacer></v-spacer> 


      <template>
  <div class="text-xs-center">
    <v-menu
      v-model="menu"
      :close-on-content-click="false"
      :nudge-width="100"
      offset-x
    >
      <template v-slot:activator="{ on }">
       <v-btn icon  v-on="on">
      <v-icon>more_vert</v-icon>
    </v-btn>
         
      </template>

      <v-card>
        <v-list>
          <v-list-tile avatar>
            <v-list-tile-avatar>
              <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John">
            </v-list-tile-avatar>

            <v-list-tile-content>
              <v-list-tile-title>{{userLoggeInName}}</v-list-tile-title>
              <v-list-tile-sub-title>{{userLoggeInPayroll}}</v-list-tile-sub-title>
            </v-list-tile-content>

            

            <v-list-tile-action>
              <v-btn
                :class="fav ? 'teal--text' : ''"
                icon
                @click="fav = !fav"
              >
                <v-icon>favorite</v-icon>
              </v-btn>
            </v-list-tile-action>
          </v-list-tile>
        </v-list>

        <v-divider></v-divider>

        <v-list>
          <v-list-tile >
            <v-list-tile-avatar>
             <v-icon>person</v-icon>
            </v-list-tile-avatar>

             <v-list-tile-content>
              <v-list-tile-title>{{userLoggeInCadre}}</v-list-tile-title>
              <v-list-tile-sub-title>From :{{userLoggeInDOA}}</v-list-tile-sub-title>
            </v-list-tile-content>

          </v-list-tile>
        </v-list>

        <v-divider></v-divider>
       <v-spacer></v-spacer> 
        <v-card-actions>
          <v-spacer></v-spacer> 

           <v-list-tile-avatar>
             <v-icon>settings</v-icon>
            </v-list-tile-avatar>

          <v-btn flat @click="changePwd">Change Password</v-btn>
          
        </v-card-actions>

         <v-divider></v-divider>
       
        <v-card-actions>          

           <v-list-tile-avatar>
             <v-icon>logout</v-icon>
            </v-list-tile-avatar>

          <v-btn flat @click="logoutUser">Logout</v-btn>
          
        </v-card-actions>
      </v-card>
    </v-menu>
  </div>
</template>




     
      </v-toolbar>

      <v-navigation-drawer v-model="drawer" fixed app>
        <v-list>
          <v-list-tile>
            <v-list-tile-avatar>
              <!--  <img lazy-src="assets/profile.jpg">  -->
              <v-img src="https://picsum.photos/510/300?random" aspect-ratio="1.7"></v-img>
            </v-list-tile-avatar>
            <v-list-tile-content>
              <v-list-tile-title>{{userloggedIn}}<span class="teal--text">(LOGGED IN)</span></v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
        <v-divider></v-divider>

        <v-list color="gray">
          <v-list-tile>
            <v-list-tile-action>
              <v-icon>home</v-icon>
            </v-list-tile-action>
            <v-list-tile-title>Home</v-list-tile-title>
          </v-list-tile>
          <v-divider></v-divider>

          <v-list-group v-if="hrPreviledges" no-action sub-group>
            <v-list-tile slot="activator">
              <v-list-tile-title class="teal--text">ADD NEW</v-list-tile-title>
              <v-spacer></v-spacer>
              <v-icon class="teal--text">add_circle_outline</v-icon>
            </v-list-tile>

            <v-list-tile v-for="(admin, i) in admins" :key="i" @click>
              <router-link :to="{ name: admin[2] }" class="white--text">
                <v-list-tile-sub-title v-text="admin[0]" class="gray--text"></v-list-tile-sub-title>
              </router-link>
              <v-list-tile-action>
                <v-icon v-text="admin[1]"></v-icon>
              </v-list-tile-action>
            </v-list-tile>
          </v-list-group>
          <v-divider></v-divider>

          <v-list-group no-action sub-group v-if="hrPreviledges">
            <v-list-tile slot="activator">
              <v-list-tile-title class="teal--text">MANAGE EMPLOYEES</v-list-tile-title>
              <v-spacer></v-spacer>
              <v-icon class="teal--text">group_add</v-icon>
            </v-list-tile>

            <v-list-tile v-for="(admin, i) in admins1" :key="i" @click>
              <router-link :to="{ name: admin[2] }" class="white--text">
                <v-list-tile-sub-title v-text="admin[0]" class="gray--text"></v-list-tile-sub-title>
              </router-link>
              <v-list-tile-action>
                <v-icon v-text="admin[1]"></v-icon>
              </v-list-tile-action>
            </v-list-tile>
          </v-list-group>
          <v-divider></v-divider>

          <v-list-group no-action sub-group v-if="hrPreviledges">
            <v-list-tile slot="activator">
              <v-list-tile-title class="teal--text">MANAGE LEAVE</v-list-tile-title>
              <v-spacer></v-spacer>
              <v-icon class="teal--text">notifications_active</v-icon>
            </v-list-tile>

            <v-list-tile v-for="(admin, i) in admins2" :key="i" @click>
              <router-link class="white--text" :to="{ name: admin[2] }">
                <v-list-tile-sub-title v-text="admin[0]" class="gray--text"></v-list-tile-sub-title>
              </router-link>
              <v-list-tile-action>
                <v-icon v-text="admin[1]"></v-icon>
              </v-list-tile-action>
            </v-list-tile>
          </v-list-group>
          <v-divider></v-divider>

          <v-list-tile>
            <v-list-tile-action>
              <v-icon>person</v-icon>
            </v-list-tile-action>
            <v-list-tile-title ><span class="teal--text">STAFF PORTAL</span></v-list-tile-title>
          </v-list-tile>
          <v-divider></v-divider>

          <v-list  no-action sub-group>
            <v-list-tile slot="activator">
              <v-list-tile-title class="teal--text"></v-list-tile-title>
              <v-spacer></v-spacer>
              <v-icon class="teal--text">person</v-icon>
            </v-list-tile>

            <v-list-tile class="portal_items" v-for="(port, i) in portal" :key="i" @click>
              <v-icon></v-icon>
              <router-link class="white--text" :to="{ name: port[1] }">
                <v-list-tile-sub-title v-text="port[0]" class="gray--text"></v-list-tile-sub-title>
              </router-link>
            </v-list-tile>
          </v-list>
          <v-divider></v-divider>
        </v-list>
      </v-navigation-drawer>
      

      <v-content>
       
        <v-list>
          
          <v-list-tile subheader > 
             <v-spacer></v-spacer>
            
           <span class="teal--text">{{userLoggeInName }} </span> <h3> ( {{  userLoggeInCadre || uppercase}} )</h3>
          </v-list-tile>
          
        </v-list>

        <router-view></router-view>
      </v-content>
      <v-navigation-drawer v-model="right" right temporary fixed></v-navigation-drawer>
      <v-footer color="teal" dark class="white--text">
        <span></span>
        <v-spacer></v-spacer>
        <span>All rights reserved    &copy;Kemri-Faces2019    </span>
      </v-footer>
    </template>

    <template v-else>
      <v-content>
        <v-container fluid fill-height>
          <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>
              <v-card class="elevation-12">
                <v-toolbar dark color="teal">
                  <v-toolbar-title>Login </v-toolbar-title>
                  <v-spacer></v-spacer>
                  <v-tooltip bottom>
                    <v-btn icon large slot="activator">
                      <v-icon large></v-icon>
                    </v-btn>
                    <span></span>
                  </v-tooltip>
                </v-toolbar>
                <v-card-text>
                  <v-form v-model="loginState" ref="form">
                    <v-text-field
                      prepend-icon="person"
                      name="login"
                      label="Username"
                      v-model="LoginForm.username"
                      type="text"
                      color="teal--text"
                      :rules="nameRules"
                    ></v-text-field>
                    <v-text-field
                      prepend-icon="lock"
                      name="password"
                      label="Password"
                      v-model="LoginForm.password"
                      id="password"
                      type="password"
                      color="teal--text"
                      :rules="passwordRules"
                    ></v-text-field>
                    <div v-if="validatepwd">
                    <span class="red--text">Wrong username or password !! please try again </span>
                    </div>
                    <div v-if="supervisorExists">
                    <span class="red--text">You do not have a supervisor!! Please contact Hr for assistance </span>
                    </div>
                  </v-form>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn @click="loginUser" color="teal--text">Login</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-content>
    </template>
    <template>
       <div class="text-xs-center" v-if="progressLoading">
      <v-progress-circular :size="50" color="teal" indeterminate></v-progress-circular>
    </div>
      
    </template>
    
   
  </v-app>
</template>

<script>
import api from "@/apis/api";
export default {
  data: () => ({
    
    drawer: null,
    drawerRight: null,
    right: false,
    left: false,
    login: false,
    loginState:false,
    validatepwd:false,
    supervisorExists:false,
    hrPreviledges:false,
    userloggedIn:"",
    userLoggeInName:"",
    userLoggeInCadre:"",
    userLoggeInPayroll:"",
    userLoggeInDOA:"",
    LoginForm: {
      username: "",
      password: ""
    },

    
    progressBar:true,
    //progressLoading:true,
    fav: true,
      menu: false,
      message: false,
      hints: true,
      nameRules: [
      v => !!v || "Username is required",
      v => (v && v.length >= 2) || "Name must be less than 10 characters"
    ],

    passwordRules: [
    v => !!v || "Password is required",
      v => (v && v.length >= 5) || "Password must contain at least 5 characters",
      v => /[A-Z].+$/.test(v) || "Password must a capital letter",
      v => /[0-9].+$/.test(v) || "Password must a digit",
      v => /(?=.[!@#*()\$%\^&]).+$/.test(v) || "Password must contain a special character",
      //v => /^[a-zA-Z0-9].+.[a-zA-Z0-9]+$/.test(v) || 'Password must have lower and and upper case and a digit' 
 
    ],
    admins: [
      ["Levels", "", "level"],
      ["Cadre", "", "designation"],
      [" Employee", "", "register"],
      ["Leave Types", "", "leaveType"],
      ["Public Holidays", "", "holidays"],
      ["Initial Leave Balances","", "initialleavebalance"]
    ],
    admins1: [
      ["Employee List", "", "employeeList"],
      ["Assign Supervisors", "", "assinsupervisor"],
      ["Employee Supervisor", "", "employeesupervisor"]
    ],

    admins2: [
      ["Leave Balances", "", "leavetypebalances"],
      ["Leave Applications History", "", "allapplications"],
      ["Approve/Decline Leave", "", "leaveApproval"]
    ],

    portal: [
      ["Leave Balance", "leaveBalance"],
      ["Apply Leave", "leaveApplication"],
      ["Application History", "applicationHistory"]
    ],
    mini: true,
    right: null
  }),
  props: {
    source: String
  },
  methods: {
    changePwd(){
      this.menu=false;
      console.log("THE TEST CHANGE")
      this.$router.push({name:'changepassword'})
    },
    goToStaff() {
      console.log("Clicked ::::::::");

      this.$router.push({ name: "staff", params: { userId: "agik12345" } });
    },
    goToSupervisors() {
      this.$router.push({
        name: "supervisor",
        params: { userId: "agik12345" }
      });
    },
    goToDashboard(){
     this.$router.push({
        name: "home",
        params: { userId: "agik12345" }
      });
    },
    async checkUserExists(payload) {
      await api
        .loginUser("userLogin", payload)
        .then(result => {
          console.log("RESPONSE AT LOGIN ************ ",result)
          if(result == "False"){
            console.log("RESPONSE AT LOGIN 111 ",result)
            this.supervisorExists = true;
          }else {

           this.supervisorExists = false;

            console.log("RESPONSE AT LOGIN  22",result)
          if (result != null) {
            this.login = true;
            this.validatepwd = false
            this.supervisorExists = false
            this.accessPreviledges(result.data.user_details)
            console.log("Login ", result);
          } else {
            this.validatepwd=true
            console.log("Wrong Pwd");
          }
          console.log("AT LOGIN 22", localStorage.getItem("userSession"));

          }
          
        })
        .catch(error => {
          console.log(error);
        });
    },
    // get user cadre

    async userCadre(cadreId){
      await api.getEntry("getSingleCadre",cadreId)
      .then(data =>{
        console.log("CADREScc", data.data.cadre)
        this.userLoggeInCadre = data.data.cadre
      })
    },

    accessPreviledges(userDetails){
      this.userloggedIn = userDetails.username
      this.userLoggeInName = userDetails.surname+ "   "+ userDetails.other_names  //"    ("+ userDetails.designation+")"
      this.userLoggeInDOA = userDetails.appointment_date
      this.userLoggeInPayroll = userDetails.payroll_no
      if(userDetails.designation <= 6){
        this.hrPreviledges = true
        
        console.log("userDetails 66666 ::: ",userDetails)
      } else{
        this.hrPreviledges = false
        console.log("userDetails  ::: ",userDetails)
      //hrPreviledges

      }

      this.userCadre(userDetails.designation)
      

    },

    async checkAssignedSupervisor(){
     // await api.

    },
    logoutUser(){
      this.login=false
    },

    loginUser() {
      if(this.$refs.form.validate()){
        this.checkUserExists(this.LoginForm);

      }
      
    }
    /* async checkBackendConn(){
        console.log("THE axio",)
        var conn =  axios.get(url)
        conn.then(data =>{
            if(data){
                console.log(data)
            }else{
                console.log('Not found')
            }
        }).catch(error =>{
            this.$store.commit('change', 'falseConnection')
            console.log('Not found error ',error)
        });
        
    }, */
  },
  
  beforeCreate(){
    this.progressBar =true
  },
  created() {
    console.log("HERE");
    this.login = false;
    this.progressBar=true
    // state = api.checkBackendConn()
  },

  watch: {
    //fp = new http_ping("www.linux.com.au")
  },
   
};
</script>

</<style>
.portal_items{
  padding-left:55px;
}
</style>


    