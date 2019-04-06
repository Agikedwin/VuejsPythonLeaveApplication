<template>
<v-flex xs12 sm12 offset-sm0>
  <v-card class="applyleave">
    <v-form v-model="valid" ref="form">
      <v-container class="cont-2">
        <v-layout row wrap>
          <v-flex xs12 sm5>
            <v-autocomplete
              v-slot:items="supervisorsList"
              :items="supervisorsList"
              :filter="customFilter"
              :rules="nameRules"
              v-model="applicationForm.reliever_payroll_no"
              color="gray"
              item-text="surname"
              item-value="payroll_no"
              clearable
              label="Select your reliever"
              @change="getSelectedSup"
              
            ></v-autocomplete>
          </v-flex>

           <v-flex xs12 sm1></v-flex>

          <v-flex xs12 sm5></v-flex>
        </v-layout>
        
      </v-container>

     <v-list>
      <v-layout row wrap>
       
        <v-flex xs12 sm5>
          <v-select
            leave_name
            color="teal"
            :items="fetchLeaveType"
            label="Leave Types"
            item-text="leave_name"
            item-value="leave_id"
            v-model="selectedLeave"
            @change="getSelected"
            :rules="nameRules"
          ></v-select>
        </v-flex>

       <v-flex xs12 sm1></v-flex>

        <v-flex xs12 sm5>
          <v-text-field color="teal" :rules="remainingRules" label="Days Remaining" v-model="applicationForm.available"></v-text-field>
        </v-flex>
      </v-layout>

      <v-layout row wrap>
        <v-flex xs12 sm5>
          <v-menu
            v-model="menu1"
            color="teal"
            :close-on-content-click="true"
            :nudge-right="40"
            lazy
            transition="scale-transition"
            offset-y
            full-width
            min-width="290px"
          >
            <v-text-field
              color="teal"
              slot="activator"
              v-model="applicationForm.date_from"
              label="Date From"
              prepend-icon="event"
              readonly
              :rules="nameRules"
            ></v-text-field>
            <v-date-picker color="teal" v-model="applicationForm.date_from" @input="menu1 = false"></v-date-picker>
          </v-menu>
        </v-flex>

        <v-flex xs12 sm1></v-flex>

        <v-flex xs12 sm5>
          <v-menu
            v-model="menu2"
            color="teal"
            :close-on-content-click="true"
            :nudge-right="40"
            lazy
            transition="scale-transition"
            offset-y
            full-width
            min-width="290px"
          >
            <v-text-field
              color="teal"
              slot="activator"
              v-model="applicationForm.date_to"
              label="Date To"
              prepend-icon="event"
              readonly
              :rules="nameRules"
            ></v-text-field>
            <v-date-picker
              color="teal"
              v-model="applicationForm.date_to"
              @change="calculateDays(applicationForm.date_from,applicationForm.date_to )"
              @input="menu2 = false"
            ></v-date-picker>
          </v-menu>
        </v-flex>

        

      </v-layout>

       <v-layout row wrap>
    
    <v-flex xs12 sm5>
     <v-text-field
            disabled
            :rules="nameRules"
            color="teal"
            label="Number of days"
            v-model="applicationForm.no_days"
          ></v-text-field>
    </v-flex>
     <v-flex xs12 sm1></v-flex>
    <v-flex xs12 sm5>
     <v-text-field
              disabled
            color="teal"
            label="Days Carried Forward "
            
          ></v-text-field>
    </v-flex>
  </v-layout>
      <v-layout row wrap>
        <v-flex xs12 sm12>
          <v-textarea
            :rules="nameRules"
            color="teal"
            v-model="applicationForm.note"
            label="Leave Application Note"
            required
          ></v-textarea>
        </v-flex>
      </v-layout>
     </v-list>
    </v-form>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="teal" class="white--text" depressed @click="submit('apply')">Apply</v-btn>
    </v-card-actions>

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
        <v-dialog v-model="confirmationDialog" persistent max-width="350">
          <v-card>
            <v-card-text>{{dialogMsg}}</v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="green darken-1" value="ok" flat="flat" @click="submit('no')">No</v-btn>

              <v-btn color="green darken-1" alue="no" flat="flat" @click="submit('ok')">Yes</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!--End  Confirmation dialog -->
      </v-layout>
    </template>
    

    <template>

      <v-dialog
      v-model="savingDialog"
      hide-overlay
      persistent
      width="200"
    >
      <v-card
        color="success"
        dark
      >
        <v-card-text>
         Wait Applying...
          <v-progress-circular
            indeterminate
            color="white"
            class="mb-0"
          ></v-progress-circular>
        </v-card-text>
      </v-card>
    </v-dialog>
     
    </template>
  </v-card>
  </v-flex>
</template>

<script>
import api from "../apis/api";
export default {
  data: () => ({
    menu1: false,
    modal: false,
    menu2: false,
    applicationForm: {
      leave_type: "",
      leave_id: 0,
      available: "",
      payroll_no: localStorage.getItem("userSession"),
      date_from: "",
      date_to: "",
      no_days: "",
      note: "",
      reliever_payroll_no:"",
    },
    datePayload: {
      date_from: "",
      date_to: ""
    },
    selectedLeave: "",
    applicationData: [],
    leaveTypesdata: [],
    fetchLeaveType: [],
    listLeaveTypes: [],
    savingDialog:false,

    msg: "",
    popupDialog: false,
    popupDialogfailed: false,
    popupColor: "",
    progressBar:true,

    confirmationDialog: false,
    dialogMsg: "",

    supervisorsList: [],
    supervisorsList: [],
    supervisor_id: "",

    showDialog: false,
    valid: false,
    nameRules: [v => !!v || "Field is required"],
    LeaveBalanceName: [v => !!v || "You do not have any leave days left "],

    remainingRules: [v => (v && v > 0) || "You do not have any leave days left",
                    v => !!v || "Field is required"],

     selectRules: [
      v => !!v || "Please select supervisor",
      v => (v && v.length >= 2) || "Name must be less than 10 characters"
    ],
  }),

  methods: {
    customFilter(item, queryText, itemText) {
      const textOne = item.surname.toLowerCase();
      const textTwo = item.surname.toLowerCase();
      const searchText = queryText.toLowerCase();

      return (
        textOne.indexOf(searchText) > -1 || textTwo.indexOf(searchText) > -1
      );
    },
    async addRecord(payload) {
      this.showDialog = true;
      await api.addEntry("addApplication", payload).then(data => {
        console.log("RESPONSE STATUS ::: ", data);
        this.msg = "Leave successfully Applied";
        this.showDialog = false;
        this.savingDialog=false
        this.popupDialog = true;
        this.$refs.form.reset();
      });
    },

    async fetchEmployees() {
      await api.getEntries("allSupervisors").then(empList => {
        var result = [];
        var result2 = [];
        empList.forEach(function(element, index) {
          result.push(element);
        });

        this.supervisorsList = result;
        console.log(result);
      });
    },
    async getSelectedSup() {

      this.getSelecteSupervisorId = this.supervisor_id;

     

      console.log("THE Reliever :::: ", this.applicationForm.reliever_payroll_no);
      
       
    },

      getEmpSupervisorAssigned(){
        api.getEntries("checkSupExist")
          .then(data => {
            console.log("the liever ****** :::: 222", data)
          }).finally(data=>{
            console.log("the liever ****** :::: ", data)
          })

    },

    submit(val) {
      console.log("Adding val  this.applicationForm", this.applicationForm);
      console.log(this.$refs.form.validate());
      if (this.$refs.form.validate()) {
        if (val == "apply") {
          this.dialogMsg = "Are you sure you want to apply for this  leave ";
          this.confirmationDialog = true;
        }

        if (val == "ok") {
          console.log("Adding val ", val);
          this.savingDialog=true
          this.addRecord(this.applicationForm);
          this.confirmationDialog = false;
          //this.applicationForm = "";
        }

        if (val == "no") {
          this.confirmationDialog = false;
        }
      }
    },

    async getLeaveTypes() {
      await api.getEntries("getAllLeaveTypes").then(data => {
        this.fetchLeaveType = data;
        console.log(this.fetchLeaveType);
      });

      /* for (var i = 0; i < this.fetchLeaveType.length; i++) {
        this.listLeaveTypes.push(this.fetchLeaveType[i].leave_name);
      } */
    },
    getSelected() {
      this.applicationForm.leave_id = this.selectedLeave;

      console.log("THE TEXT :::  ", this.applicationForm.leave_id);
      this.getNoDays(this.applicationForm.leave_id);

      /* for (var i = 0; i < this.fetchLeaveType.length; i++) {
        if (this.fetchLeaveType[i].leave_name == selected) {
          this.applicationForm.leave_id = this.fetchLeaveType[i].leave_id;
          this.getNoDays(this.applicationForm.leave_id);
          break;
        } else {
          console.log("not found");
        }
      } */
    },
    async getNoDays(id) {
      await api.getSingleEntry("getNoDays", id).then(data => {
        this.applicationForm.available = data.data.remaining;
      });
    },
    async calculateDays(date_from, date_to) {
      this.datePayload.date_from = date_from;
      this.datePayload.date_to = date_to;

      // if weekends not inculded
      await api
        .addEntry("calculateLeaveDays", this.datePayload)
        .then(result => {
          console.log("NUMBER OF DAYS :::", result);
          this.applicationForm.no_days = result.data.no_days;
        });
    }
  },
  created() {
    console.log("PAYROLL NO LOCAL STORAGE ",localStorage.getItem("userSession"))
    this.getLeaveTypes();
    this.fetchEmployees();
    this.getEmpSupervisorAssigned()
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

<style>
.applyleave {
  padding-left: 20px;
}
</style>
