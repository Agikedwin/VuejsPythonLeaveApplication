<template>
  <v-layout>
    <v-flex>
      <v-card>
        <v-fab-transition style="height: 100px; position: relative">
            <v-btn color="gray" absolute top right fab small @click="emplist">
              <v-icon class="teal--text">visibility</v-icon>
            </v-btn>
          </v-fab-transition>
        <v-stepper v-model="step" vertical >
          <v-stepper-header> 
            <v-stepper-step color="teal lighten-2" step="1" :complete="step > 1">Your Information </v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step color="teal lighten-2" step="2" :complete="step > 2">More Details</v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step step="3" color="teal lighten-2">More</v-stepper-step>
          </v-stepper-header>
          <v-stepper-items>
            <v-stepper-content step="1">
              <v-form v-model="valid" ref="form">
              <v-text-field label=" Surname Name" :rules="nameRules" color="teal" v-model="registrationForm.surname" required></v-text-field>
              <v-text-field label="Others Names" :rules="nameRules" color="teal" v-model="registrationForm.other_names" required></v-text-field>
              <v-text-field
                label="Employee Personal/Staff No"
                type="number"
                v-model="registrationForm.payroll_no"
                 color="teal"
                 :rules="payrollRule"
                required
              ></v-text-field><div v-if="checkUnique"><span class="red--text">The payroll number already exists</span></div>

              <v-flex xs12 sm12 md12>
                <v-menu
                  v-model="menu1"
                  :close-on-content-click="true"
                  :nudge-right="40"
                  lazy
                  transition="scale-transition"
                  offset-y
                  full-width
                  min-width="290px"
                   color="teal"
                >
                  <v-text-field
                    box
                    slot="activator"
                    v-model="registrationForm.appointment_date"
                    label="Date of first appointemnt"
                    prepend-icon="event"
                    readonly
                     color="teal"
                     :rules="nameRules"
                  ></v-text-field>
                  <v-date-picker   color="teal" v-model="registrationForm.appointment_date" @input="menu1 = false"></v-date-picker>
                </v-menu>
              </v-flex>

              <v-select
                label="Cadre"
                v-model="registrationForm.cadre"
                :items="listCadre"
                @change="selectedCadre()"
                item-text="name"
                item-value="id"
                return-object
                required
                 color="teal"
                 :rules="nameRules"
              ></v-select>

              <v-text-field
                label=" Salary Entry Point"
                v-model="registrationForm.entry_salary"
                required
                type="number"
                 color="teal"
                 :rules="nameRules"
              ></v-text-field>
              <v-text-field label="Program" :rules="nameRules"  color="teal" v-model="registrationForm.program" required></v-text-field>
              </v-form>
              <v-btn class="teal--text"   @click.native="stepNext">Continue</v-btn>
            </v-stepper-content>
            <v-stepper-content step="2">
              <v-form v-model="valid" ref="form2">
              <v-select
                label="Terms of Service"
                v-model="registrationForm.terms_of_service"
                :items="terms"
                required
                 color="teal"
                 :rules="nameRules"
              ></v-select>

              <v-flex xs12 sm12 md12>
                <v-menu
                  v-model="menu2"
                  :close-on-content-click="true"
                  :nudge-right="40"
                  lazy
                  transition="scale-transition"
                  offset-y
                  full-width
                  min-width="290px"
                   color="teal"
                >
                  <v-text-field
                    box
                    slot="activator"
                    v-model="registrationForm.dob"
                    label="Date of birth"
                    prepend-icon="event"
                    readonly
                     color="teal"
                     :rules="lengthRules"
                  ></v-text-field>
                  <v-date-picker  color="teal" v-model="registrationForm.dob" @input="menu2 = false"></v-date-picker>
                </v-menu>
              </v-flex>

              <v-text-field  color="teal" :rules="nameRules" label="Place of Birth" v-model="registrationForm.birth_place" required></v-text-field>
              <v-text-field   color="teal" :rules="nameRules"  label="Nationalty" v-model="registrationForm.nationalty" required></v-text-field>
              <v-text-field
                label="Passport/Id No"
                type="number"
                v-model="registrationForm.passport_idno"
                required
                 color="teal"
                 :rules="nameRules"
              ></v-text-field>

              <v-select
                label="Marital Status"
                v-model="registrationForm.marital_status"
                :items="marital"
                required
                 color="teal"
                 :rules="nameRules"
              ></v-select>
              <v-text-field  color="teal" :rules="phoneRule" label="Phone Number" v-model="registrationForm.phone_no" required></v-text-field>
              <v-text-field   color="teal" :rules="emailRules"  label="Email Address" v-model="registrationForm.email" required></v-text-field>
              <v-text-field  color="teal" :rules="nameRules"  label="Spause Name" v-model="registrationForm.spause_name" required></v-text-field>
              <v-text-field  color="teal" type="number"  label="Spause's ID No" v-model="registrationForm.spause_idno" required></v-text-field>

              <v-btn flat @click.native="step = 1">Previous</v-btn>
              <v-btn class="teal--text" @click.native="stepNext3">Continue</v-btn>
              </v-form>
            </v-stepper-content>
           
            <v-stepper-content step="3">
               <v-form v-model="valid" ref="form3">
              <v-text-field  color="teal"  :rules="nameRules"  label="KRA Pin No" v-model="registrationForm.kra_no" required></v-text-field>
              <v-text-field  color="teal" type="number"  label="NSSF No" v-model="registrationForm.nssf_no" required></v-text-field>
              <v-text-field   color="teal" type="number"  label="NHIF No" v-model="registrationForm.nhif_no" required></v-text-field>
              <v-text-field  color="teal"  label="Bank Name" v-model="registrationForm.bank_name" required></v-text-field>
              <v-text-field   color="teal" type="number"  label="Account No" v-model="registrationForm.account_no" required></v-text-field>
              <v-text-field   color="teal" label="Branch" v-model="registrationForm.branch" required></v-text-field>

              <v-btn flat @click.native="step = 2">Previous</v-btn>
              <span v-if="!progressBar">
                <v-btn class="teal--text"   @click.prevent="submit">Save</v-btn>
              </span>
              <span v-if="progressBar">
                <v-progress-circular  indeterminate  color="teal" ></v-progress-circular>saving...
              </span>

              
              </v-form>
            </v-stepper-content>
            
          </v-stepper-items>
        </v-stepper>
      </v-card>
    </v-flex>

    <v-dialog v-model="popupDialog" hide-overlay persistent width="500">
      <v-card color="success" dark>
        <v-card-text>
          {{msg}}
          <span>
            <v-icon>ok</v-icon>
          </span>
        </v-card-text>
      </v-card>
    </v-dialog>

    <v-dialog v-model="popupDialogfailed" hide-overlay persistent width="500">
      <v-card color="danger" dark>
        <v-card-text>
          {{msg}}
          <span>
            <v-icon>ok</v-icon>
          </span>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
import api from "../apis/api";
export default {
  data: () => ({
    step: 1,
    registrationForm: {
      employee_id:0,
      surname: "",
      other_names: "",
      appointment_date: "",
      payroll_no: "",
      cadre: "",
      designation_id:"",
      entry_salary: "",
      program: "",
      department: "",
      terms_of_service: "",
      dob: "",
      birth_place: "",
      nationalty: "",
      passport_idno: "",
      marital_status: "",
      email: "",
      phone_no: "",
      spause_name: "",
      spause_idno: "",
      kra_no: "",
      nssf_no: "",
      nhif_no: "",
      bank_name: "",
      account_no: "",
      branch: ""
    },

    menu1: false,
    modal: false,
    menu2: false,

    msg: "",
    popupDialog: false,
    popupDialogfailed: false,
    popupColor: "",
    progressBar:false,

    fetchCadre: [],
    listCadre: [],
    checkUnique:false,
    empPayroll:[],
    
    terms: ["Permanent", "Contract"],
    marital: ["Married", "Single","Widowed","Separated","Divorced"],

    valid: false,
    nameRules: [
      v => !!v || "Field is required",
    ],

    lengthRules: [v => !!v || "You must provide "],
    payrollRule:[v=>!!v || "Field required",
                 v=> v.length == 5 || "The payroll number must be 5 characters"],
    phoneRule: [ v => /(?=['+'].['0-9']).+$/.test(v) || "Phone number must start with + followed by country code ",
                 v => !!v || "Field required",  
                 v => v.length > 10 || "The digits must be more than 10 characters",              
                ],

    emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid'
      ],
  }),

  methods: {
    async getRecord() {
      await api
        .getEntries("getAllEmployees")
        .then(data => {
        
          for(var i=0; i<data.length;i++){
            this.empPayroll.push(data[i].payroll_no)
          }
          this.regData = data;
          
        })
        .catch(error => {
          console.log(error);
        });
    },

    async addRecord(payload) {
      await api
        .addEntry("addEmployee", payload)
        .then(data => {
          console.log("data", data);
          if (data.status == 200) {
            this.msg = "Record successfully saved";
            this.progressBar = false
            this.popupDialog = true;
          } else {
            this.msg = "Record Failed to saved";
            this.popupDialogfailed = true;
            this.progressBar = true
          }
        })
        .catch(error => {
          this.progressBar = true
          console.log(error);
        });
    },

    async update(empid,payload) {
      await api
        .editEntry("editemployee", empid, payload)
        .then(data => {
          
          if (data.status == 200) {
           this.msg = "Record successfully saved";
            this.popupDialog = true;
          } else {
            this.msg = "Record Failed to update";
            this.popupDialogfailed = true;
          }
        })
        .catch(error => {
          console.log(error);
        });
    },

    async delete(payload, regid) {
      await api
        .deleteEntry("addDeptment", regid, payload)
        .then(data => {
          console.log("the submiting data .......2");
          this.getRecord();
          console.log("the submiting data .......");
          if (data.data.message == "success") {
            console.log("Record added successfully!");
          } else {
            alert("Record adding failed");
          }
        })
        .catch(error => {
          console.log(error);
        });
    },

    async getCadre() {
      await api.getEntries("getAllDesignations").then(data => {
        this.fetchCadre = data;
      });
      for (var i = 0; i < this.fetchCadre.length; i++) {
        this.listCadre.push(this.fetchCadre[i].designation_name);
      }
    },
    selectedCadre() {
      for (var i = 0; i < this.fetchCadre.length; i++) {
        
        if (
          this.fetchCadre[i].designation_name == this.registrationForm.cadre
        ) {
         
          this.registrationForm.designation_id = this.fetchCadre[i].designation_id;
          this.registrationForm.department = 0;
          console.log("OBTAINED CADRE 444::", this.registrationForm)
          break;
        }
      }
    },

    submit() {
      if(this.$refs.form3.validate()){
        if(this.registrationForm.employee_id==0){
          this.progressBar = true
          this.addRecord(this.registrationForm);
        //this.$refs.form3.reset()
        }else{
          // get the cadre id when editing since the cadre may not be selected
          //for(var i = 0; i<this.f)
          this.selectedCadre()
          console.log("OBTAINED CADRE ::", this.registrationForm)
          this.update(this.registrationForm.payroll_no, this.registrationForm)
        }
        
      }
      
      /* if(this.registrationForm.department_id ==0){
        this.addRecord(this.registrationForm);
      } else{
        this.update(this.registrationForm, this.registrationForm.department_id)
      } */
    },

    clear() {
      //this.$refs.form.reset()let myObj = { name: 'Skip', breed: 'Labrador' };
      //localStorage.setItem(myObj, JSON.stringify(myObj));
      //this.getRecord()
      //console.log(localStorage.getItem(myObj))
      //getRecord()
    },
    editDept(selected) {
      this.registrationForm.name = selected.department_name;
      this.registrationForm.description = selected.description;
      this.registrationForm.department_id = selected.department_id;
    },
    deleteDept() {
      console.log("testing........2");
    },
    stepNext(){
      console.log("THE NEXT ",)
      var payroll=+this.registrationForm.payroll_no;
      if(this.registrationForm.employee_id==0){
        if(this.$refs.form.validate() ){
        if(this.empPayroll.indexOf(payroll)>-1){
           this.checkUnique=true
        }else{
          this.checkUnique=false
          this.step =2          
        }
             }
      }else{
        this.checkUnique=false
          this.step =2 

      }
      
     
    },
    stepNext3(){
       if(this.$refs.form2.validate()){
         this.step =3
        
     } 
    },
    emplist(){
        this.$router.push({ name: "employeeList", params: { } });

    },
    customFilter(){
     
       
      
      
    }
  },
  created() {
  //console.log("THE DATA ", this.$route.params.userId.payroll_no)
  this.getCadre();
    this.getRecord()
  
   if(this.$route.params.userId.payroll_no>0){
     this.registrationForm=this.$route.params.userId
     this.registrationForm.cadre = this.$route.params.userId.designation
    

      console.log(" THE DATA this.$route.params.userId##### :::", this.$route.params.userId.designation)

   }else{
     this.$refs.form.reset()
   }

   
    
  },
  beforeCreate(){
  },
  watch: {
    popupDialog(val) {
      if (!val) return;

      setTimeout(() => (this.popupDialog = false), 2000);
    },

    popupDialogfailed(val) {
      if (!val) return;

      setTimeout(() => (this.popupDialogfailed = false), 2000);
    }
  }
};
</script>
