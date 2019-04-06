<template>
  <v-list two-line>
       <v-spacer></v-spacer>
         
       <v-divider></v-divider>
    <template>
         <v-fab-transition style="height: 100px; position: relative">
            <v-btn color="gray" absolute top right fab small @click="emplist">
              <v-icon class="teal--text">visibility</v-icon>
            </v-btn>
          </v-fab-transition>
      <v-list-tile>
        <v-layout row wrap>
          <v-flex xs12 sm4>
            <v-list-tile-title>EMPLOYEE ID :{{employeeList.employee_id}}</v-list-tile-title>
          </v-flex>

          <v-flex xs12 sm4>PAYROLL NUMBER: {{employeeList.payroll_no}}</v-flex>

          <v-flex xs12 sm4>FIRST APPOINTMENT : {{employeeList.appointment_date}}</v-flex>
          <v-divider></v-divider>
        </v-layout>
      </v-list-tile>
    </template>
 <v-divider></v-divider>
    <template>
      <v-list-tile>
        <v-layout row wrap>
          <v-flex xs12 sm4>
            <v-list-tile-title>SURNAME :{{employeeList.surname}}</v-list-tile-title>
          </v-flex>

          <v-flex xs12 sm4>OTHER NAMES: {{employeeList.other_names}}</v-flex>

          <v-flex xs12 sm4>PASSPORT/ID : {{employeeList.passport_idno}}</v-flex>
        </v-layout>
        
      </v-list-tile>
    </template>
 <v-divider></v-divider>
    <template>
      <v-list-tile>
        <v-layout row wrap>
          <v-flex xs12 sm4>
            <v-list-tile-title>NATIONALITY :{{employeeList.nationalty}}</v-list-tile-title>
          </v-flex>

          <v-flex xs12 sm4>PLACE OF BIRTH: {{employeeList.birth_place}}</v-flex>

          <v-flex xs12 sm4> DATE OF BIRTH: {{employeeList.dob}}</v-flex>
        </v-layout>
      </v-list-tile>
    </template>
     <v-divider></v-divider>
    <template>
      <v-list-tile>
        <v-layout row wrap>
          <v-flex xs12 sm4>
            <v-list-tile-title>TERMS OF SERVICE:{{employeeList.terms_of_service}}</v-list-tile-title>
          </v-flex>

          <v-flex xs12 sm4>SPAUSE NAME: {{employeeList.spause_name}}</v-flex>

          <v-flex xs12 sm4>PROGRAM : {{employeeList.program}}</v-flex>
        </v-layout>
      </v-list-tile>
    </template>
     <v-divider></v-divider>
    
     
    <template>
      <v-list-tile>
        <v-layout row wrap>
          <v-flex xs12 sm4>
            <v-list-tile-title>ENTRY SALARY:{{employeeList.entry_salary}}</v-list-tile-title>
          </v-flex>

          <v-flex xs12 sm4>DESIGNATION: {{employeeList.designation}}</v-flex>

          <v-flex xs12 sm4>MARITAL STATUS : {{employeeList.marital_status}}</v-flex>
        </v-layout>
      </v-list-tile>
    </template>
     <v-divider></v-divider>
    <template>
      <v-list-tile>
        <v-layout row wrap>
          <v-flex xs12 sm4>
            <v-list-tile-title>BANK NAME :{{employeeList.bank_name}}</v-list-tile-title>
          </v-flex>

          <v-flex xs12 sm4>BRANCH: {{employeeList.branch}}</v-flex>

          <v-flex xs12 sm4>PROGRAM : {{employeeList.program}}</v-flex>
        </v-layout>
      </v-list-tile>
    </template>
     <v-divider></v-divider>

    <template>
      <v-list-tile>
        <v-layout row wrap>
          <v-flex xs12 sm4>
            <v-list-tile-title>KRA NO :{{employeeList.kra_no}}</v-list-tile-title>
          </v-flex>

          <v-flex xs12 sm4>NHIF NO: {{employeeList.nhif}}</v-flex>

          <v-flex xs12 sm4>NSSF : {{employeeList.nssf_no}}</v-flex>
        </v-layout>
      </v-list-tile>
    </template>
     <v-divider></v-divider>
  </v-list>
</template>


<script>
import api from "../apis/api";
export default {
  data() {
    return {
      search: "",
      employeeList: []
    };
  },
  methods: {
    async fetchEmployee() {
        
      
      await api
        .getEntry("getEmployee", this.$route.params.view.payroll_no)
        .then(empList => {
          this.employeeList = empList.data.result[0];
          console.log("EMP ************", this.employeeList);
        });
    },
    emplist(){
        this.$router.push({ name: "employeeList", params: { } });

    }
  },
  created() {
      
    if(this.$route.params.view){
        console.log("THE TEST DATA  3333:: ", this.$route.params.view);
       this.fetchEmployee(); 
    }else{
       this.$router.push({ name: "employeeList", params: { } });
    }
    
  },
  beforeCreate() {
    console.log("THE TEST DATA :: ", this.$route.params);
  }
};
</script>