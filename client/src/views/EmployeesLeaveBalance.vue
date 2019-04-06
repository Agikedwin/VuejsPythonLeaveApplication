<template>
  <v-card>
    <div class="text-xs-center" v-if="progressBar">
      <v-progress-circular :size="50" color="teal" indeterminate></v-progress-circular>
    </div>
    <v-card-title>
      <v-spacer></v-spacer>

      <v-autocomplete
        v-slot:items="supervisorsList"
        :items="supervisorsList"
        :filter="customFilter"
        v-model="supervisor_id"
        color="gray"
        item-text="surname"
        item-value="payroll_no"
        clearable
        label="Select Employee"
        @change="getSelectedSup"
      ></v-autocomplete>
    </v-card-title>

    <v-data-table :headers="headers" :items="employeeList" :pagination.sync="pagination">
      <template slot="items" slot-scope="props">
        <td class="text-xs-left">{{ props.item.leave_type }}</td>
        <!-- <td class="text-xs-left">{{ props.item.date_from }}</td> -->
        <td class="text-xs-left">{{props.item.leave_days}}</td>
        <td class="text-xs-left">{{ props.item.leave_balance }}</td>
        <td class="text-xs-left">
          <v-progress-linear
            v-model="props.item.per_remaining"
            color="teal"
            value="0"
            height="20"
            label="test"
          >{{props.item.per_remaining}}%</v-progress-linear>
        </td>
      </template>
    </v-data-table>
  </v-card>
</template>


<script>
import api from "../apis/api";
export default {
  data() {
    return {
      pagination: { rowsPerPage: 10 },
      search: "",
      employeeList: [],
      addDetails: "addDetails",
      valueDeterminate: 0,

      approveForm: {
        approval_id: "",
        application_id: "",
        payroll_no: "",
        aproval_status: "",
        note: ""
      },

      supervisorsList: [],
      supervisorsResults: [],
      supervisor_id: 0,
      progressBar:true,

      headers: [
        { text: "Leave Type", value: "surname", align: "left" },
        { text: "Leave Days", value: "programe" },
        { text: "Days Remaining", value: "nationality" },
        { text: "% Used", value: "nationality" }
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
    getSelectedSup() {
      this.getSelecteSupervisorId = this.supervisor_id;
      this.fetchEmployee(this.getSelecteSupervisorId);
    },
    async fetchEmployee(supid) {
      await api.getEntry("leaveTypesHistory", supid).then(empList => {
        this.employeeList = empList.data.result;
      });
    },
    async fetchLeaveApplication() {
      await api.getEntries("leaveHistory").then(empList => {
        this.employeeList = empList;
        this.progressBar=false
        /*  for(var i=0;i<empList.length;i++){
                empList[i].days = empList[i].leave_balance
                var convertedValue=(empList[i].leave_balance * 100)/empList[i].leave_days
                empList[i].leave_balance = convertedValue
                
                console.log('Res ', empList)
                

              } */
        // this.employeeList = empList
        //this.valueDeterminate = empList
        //console.log("EMP ************", this.employeeList)
      });
    },
    async fetchSupervisors() {
      await api.getEntries("getAllEmployees").then(empList => {
        var result = [];
        var result2 = [];
        empList.forEach(function(element, index) {
          result.push(element);
        });
        this.supervisorsList = result;
        console.log(result);
      });
    }
  },
  created() {
    this.fetchSupervisors();
    this.fetchLeaveApplication();
  }
};
</script>