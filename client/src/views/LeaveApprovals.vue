<template>
  <v-card>
    <div class="text-xs-center" v-if="progressBar">
      <v-progress-circular :size="50" color="teal" indeterminate></v-progress-circular>
    </div>
    <v-data-table :headers="headers" :items="employeeList" :search="search" :pagination.sync="pagination">
      <template slot="items" slot-scope="props">
        <td class="text-xs-left">{{ props.item.payroll_no }}</td>
        <td class="text-xs-left">{{ props.item.surname }} {{ props.item.other_names }}</td>
        <td class="text-xs-left">{{ props.item.leave_type }}</td>
        <td class="text-xs-left">{{ props.item.date_from }}</td>
        <td class="text-xs-left">{{ props.item.date_from }}</td>
        <td class="text-xs-left">
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn flat fab class="teal--text" v-on="on" @click="approveSelected(props.item)">
                <v-icon class="steal" dark>input</v-icon>
              </v-btn>
            </template>
            <span>Click to approve</span>
          </v-tooltip>
        </td>
        <td class="text-xs-left">
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn flat fab class="teal--text" v-on="on" @click="declineSelected(props.item)">
                <v-icon dark>eject</v-icon>
              </v-btn>
            </template>
            <span>Click to decline</span>
          </v-tooltip>
        </td>
      </template>
      <v-alert
        slot="no-results"
        :value="true"
        color="error"
        icon="warning"
      >Your search for "{{ search }}" found no results.</v-alert>
    </v-data-table>

    <template>
      <div class="text-xs-center">
        <v-dialog v-model="dialog" persistent width="500">
          <v-card>
            <v-card-title class="headline grey " primary-title>Approve Leave
              <v-spacer></v-spacer>
              <v-btn icon dark @click="dialog = false">
                <v-icon>close</v-icon>
              </v-btn>
            </v-card-title>

            <v-card-text>
               <v-form v-model="valid" ref="form">
              <v-flex xs12>
                <v-textarea label="Provide A Note" 
                :rules="noteRules"
                color="teal"
                v-model="approveForm.note" required></v-textarea>
              </v-flex>
              <v-flex xs12>
                <v-checkbox
                  v-model="checkbox1"
                  color="teal"
                  :label="`Am the final person to authorize this leave `"
                  @change="showApproving1"
                  
                ></v-checkbox>
                <v-checkbox
                  v-model="checkbox2"
                  color="teal"
                  :label="`The leave requires next level of authorization `"
                  @change="showApproving2"
                  
                ></v-checkbox>
              </v-flex>

              <v-flex xs12 v-if="showNextLevelApp">
                <v-autocomplete
                  v-slot:items="supervisorsList"
                  :items="supervisorsList"
                  :filter="customFilter"
                  v-model="supervisor_id"
                  color="teal"
                  item-text="surname"
                  item-value="payroll_no"
                  clearable
                  label="Supervisor"
                  @change="getSelectedSup"
                ></v-autocomplete>
              </v-flex>
               </v-form>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="teal" flat @click="submit('open')">Submit</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
    </template>

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
    <!-- Confirmation dialog -->
    <template>
      <v-layout row justify-center>
        <v-dialog v-model="confirmationDialog" persistent max-width="250">
          <v-card>
            <v-card-text>{{dialogMsg}}</v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="green darken-1" value="no" flat="flat" @click="submit('no')">No</v-btn>

              <v-btn color="green darken-1" value="ok" flat="flat" @click="submit('ok')">Yes</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!--End  Confirmation dialog -->

        
      </v-layout>
    </template>

    <!-- Confirmation dialog  Check a must-->
    <template>
      <v-layout row justify-center>
        <v-dialog v-model="confirmationCheckDialog" persistent max-width="250">
          <v-card>
            <v-card-text>{{dialogMsg}}</v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn color="green darken-1" value="check" flat="flat" @click="submit('check')">ok</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!--End  Confirmation dialog -->

        
      </v-layout>
    </template>
    
    <!--Decline Leave approval-->

    
    <template>
  <div class="text-xs-center">
    <v-dialog
      v-model="declineDialog"
      width="500"
    >
     

      <v-card>
        <v-card-title
          class="headline grey " 
        >
          Decline Leave Application
          <v-spacer></v-spacer>
              <v-btn icon dark @click="declineDialog = false">
                <v-icon>close</v-icon>
              </v-btn>
        </v-card-title>

        <v-card-text>
          <v-textarea v-model="approveForm.note" color="teal"></v-textarea>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="teal"
            flat
            @click="submit('decline_canceal')"
          >
            Canceal
          </v-btn>
          <v-btn
            color="teal"
            flat
            @click="submit('decline_submit')"
          >
            Submit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
  <!--End Decline Leave approval-->
</template>


  </v-card>
</template>




<script>
import api from "../apis/api";
import Validations from '../utils/Validations'
export default {
  data() {
    return {
      pagination: { rowsPerPage: 10 },
      search: "",
      employeeList: [],
      addDetails: "addDetails",
      dialog: false,
      checkbox1: false,
      checkbox2: false,
      showNextLevelApp: false,

      supervisor_id: 0,
      supervisorsList: [],
      supervisorsResults: [],
      progressBar:false,

      approveForm: {
        approval_id: "",
        application_id: 0,
        payroll_no: localStorage.getItem("userSessionPayroll"),
        leave_status: "",
        nextPersonToApprove: 0,
        note: ""
      },
      

      msg: "",
      popupDialog: false,
      popupDialogfailed: false,
      popupColor: "",

      confirmationDialog: false,
      declineDialog:false,
      leaveDeclineNote:"",
      leaveDeclineApplicationId:"",
      confirmationCheckDialog:false,
      dynamicAction:"",
      dialogMsg:"",

        valid:false,
      noteRules: [
          (v) => !!v || 'Name is required' ],
        
        chechRules: [ 
          (v) => !!v || 'You must agree to continue!',
        ],

        chechRules2: [ 
         
           (v) => v || 'You must agree to continue!',
        ],
        

      headers: [
        { text: "Applicant Payroll", value: "othernames", align: "left" },
        { text: "Applicant name", value: "othernames", align: "left" },
        { text: "Leave Type", value: "surname", align: "left" },
        { text: "Date From", value: "payroll", align: "left" },
        { text: "Date To", value: "designation" },
        { text: "Accept", value: "programe" },
        { text: "Decline", value: "nationality" }
      ]
    };
  },
  methods: {
    customFilter(item, queryText, itemText) {
      const textOne = item.surname.toLowerCase();
      const textTwo = item.surname.toLowerCase();
      const searchText = queryText.toLowerCase();

      return (
        textOne.indexOf(searchText) > -1 || textTwo.indexOf(searchText) > -1
      );
    },

    async fetchSupervisors() {
      await api.getEntries("allSupervisors").then(empList => {
        var result = [];
        var result2 = [];
        empList.forEach(function(element, index) {
          result.push(element);
        });
        this.supervisorsList = result;
      });
    },
    getSelectedSup() {
      this.approveForm.nextPersonToApprove = this.supervisor_id;
    },
    async fetchLeaveApplication() {
      await api.getEntries("approveLeaveApplications").then(empList => {
        this.employeeList = empList;
      });
    },

    async leaveActions(payload) {
      console.log("At SUB 3,",payload)
      await api.addEntry("addApprovals", payload).then(data => {
        console.log("the approvals", data);
        this.msg = "Leave successfully declined";
        this.showDialog = false;
        this.popupDialog = true;
      });
    },

    async addRecord(payload) {
      await api.addEntry("addApprovals", payload).then(data => {
        this.msg = "Leave successfully Applied";
        this.showDialog = false;
        this.popupDialog = true;
        this.progressBar = false;
      });
    },

    approveSelected(data) {
      this.dialog = true;
      this.dynamicAction ='approve'
      this.dialogMsg="Aprrove the leave?"
      this.approveForm.application_id = data.application_id;
      
      //this.application_id=application_id;
    },
    submitApproved() {
      
      if (this.approveForm.application_id > 0) {
        this.addRecord(this.approveForm);
        this.fetchLeaveApplication();
      }
      {
      }
    },
    submitDecline() {
      
       console.log('VALUES ::::2 ', this.approveForm)
      if (this.approveForm.application_id) {
       this.leaveActions(this.approveForm);
        this.fetchLeaveApplication();
      }
      this.declineDialog = true
      
    },
    declineSelected(data) {
      console.log("no record to Data", data);
      this.approveForm.application_id = data.application_id;
      this.approveForm.payroll_no= data.payroll_no
      this.approveForm.leave_status =2
      this.declineDialog=true
      this.dynamicAction ='decline'
      this.dialogMsg="Do you want to decline?"

      

      
    },
    showApproving1() {
      this.showNextLevelApp = false;
      this.checkbox2 = false;
      this.checkbox1=true
      this.approveForm.nextPersonToApprove = 0;
      this.approveForm.leave_status = 1;
     
    },
    showApproving2() {
       
      this.showNextLevelApp = true;
      this.checkbox1 = false;
      this.checkbox2 =true
      this.approveForm.leave_status = 0;
      console.log("THE TEST HERE ",this.checkbox1)
    },
    submit(val) {
      if(this.$refs.form.validate()){
      console.log("the dialog dynamic ", val)
      console.log("the dialog dynamic 1 ", this.checkbox2)
      console.log("the dialog dynamic 2", this.checkbox2)
      if (val == "open") {
        if(this.checkbox1==false && this.checkbox2==false){
          this.dialogMsg="Please click your option"
        this.confirmationCheckDialog = true;
       console.log("Please check one of the boxes")
        }else if(this.checkbox2==true && this.approveForm.nextPersonToApprove==0){
          this.dialogMsg="Please select the next person to approve this leave"
           this.confirmationCheckDialog = true;
       console.log("THE STATUS 22")
        } else{
           this.dialogMsg="Aprrove the leave?"
        this.confirmationDialog = true;
        }


      }
      
      
       if(val=="check"){
          this.confirmationCheckDialog = false;
        }
      if (val == "ok" && this.dynamicAction =='approve') {
        this.submitApproved();
        this.progressBar=true;
        this.checkbox1 = false;
        this.checkbox2 = false;
        this.confirmationDialog = false;
        this.dialog = false;
      }
      if (val == "no") {
        this.confirmationDialog = false;
        this.declineDialog = false;
      }
      if(val == 'decline_canceal'){
        console.log("VAL ",val)

      }
      if(val == 'decline_submit' ){
        console.log("VAL 1 ",val)
        this.confirmationDialog = true;
       
      }
      if(val == 'decline_canceal'){
        this.declineDialog = false
        console.log("VAL 2 ",val)
       
      }
      if (val == "ok" && this.dynamicAction =='decline') {
        this.submitDecline();
        this.confirmationDialog = false;
        this.declineDialog = false;
      }
      } else{
        console.log("the data here")
      }
      this.checkbox2=false
      this.checkbox1=false
    }
    
  },
  created() {
    this.fetchLeaveApplication();
    this.fetchSupervisors();
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