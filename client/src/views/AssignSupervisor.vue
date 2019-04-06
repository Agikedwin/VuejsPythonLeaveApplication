
<template>
  <v-card>
    <v-card-title>Nutrition
      <v-spacer></v-spacer>
      <!-- <template >
      <v-autocomplete
      v-model="select"
      :loading="loading"
      :items="supervisorsList[0].bank_name"
      :search-input.sync="searchAuto"
      cache-items

      class="mx-3"
      flat
      hide-no-data
      hide-details
      label="Search Supervisor"
      solo-inverted
    ></v-autocomplete>
      </template>-->
      <v-autocomplete
        ref="selectSupervisor"
        v-slot:items="supervisorsList"
        :rules="selectRules"
        :items="supervisorsList"
        :filter="customFilter"
        v-model="supervisor_id"
        color="gray"
        item-text="surname"
        item-value="payroll_no"
        clearable
        label="Select supervisor"
        @change="getSelectedSup"

      ></v-autocomplete>
    </v-card-title>
    <v-data-table
      v-model="selected"
      :headers="headers"
      :items="employeeList"
      :search="search"
      item-key="payroll_no"
      select-all
      :pagination.sync="pagination"
    >
      <template v-slot:items="props">
        <td>
          <div v-if="!props.item.supervisor_status">
          <v-checkbox 
          color="teal"
            v-model="props.selected"
            hide-details
            @change="getSelected(props.item)"
            id="checked"
          ></v-checkbox>
          </div>
          <div v-else>
            <v-tooltip bottom>
              <template v-slot:activator="{ on }">
                
                  <v-icon color="teal" >done_outline</v-icon>
                
              </template>
              <span>Assigned</span>
            </v-tooltip>

          </div>
        </td>
        <td class="text-xs-left">{{ props.item.surname }}</td>
        <td class="text-xs-left">{{ props.item.other_names }}</td>
        <td class="text-xs-left">{{ props.item.payroll_no }}</td>
        <td class="text-xs-left">{{ props.item.designation }}</td>
        <td class="text-xs-left">{{ props.item.program }}</td>
        <td class="text-xs-left">{{ props.item.nationalty }}</td>
        <td class="text-xs-left">{{ props.item.passport_idno }}</td>
      </template>

      <template v-slot:footer>
        <td :colspan="headers.length+1" class="text-xs-right">
          <v-spacer></v-spacer>
          <strong>Please click to Assign </strong>
          <v-btn @click="submit"  class="teal--text">Assign</v-btn>
        </td>
      </template>

      <v-alert
        v-slot:no-results
        :value="true"
        color="error"
        icon="warning"
      >Your search for "{{ search }}" found no results.</v-alert>
    </v-data-table>

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

    <!-- Confirmation dialog -->
    <template>
      <v-layout row justify-center>
        <v-dialog v-model="confirmationDialog" persistent max-width="350">
          <v-card>
            <v-card-text>{{msg}}</v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="green darken-1" value="ok" flat="flat" @click="closeInfo">ok</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!--End  Confirmation dialog -->
      </v-layout>
    </template>
  </v-card>
</template>


<script>
import api from "../apis/api";
export default {
  data() {
    return {
       pagination: { rowsPerPage: 10 },
      selected: [],
      search: "",
      selectedItems: [],
      toclean: [],
      employeeList: [],
      msg: "",
      popupDialog: false,
      popupDialogfailed: false,
      getSelecteSupervisorId: 0,
      supervisor_id:'',

      /* assignSupervisorForm: {
        supervisor_id: 0,
        emp_payroll_no: 0
      }, */

      loading: false,
      items: [],
      searchAuto: null,
      select: null,
      supervisorsList: [],
      supervisorsResults: [],
      isLoading: false,
      selectedresult:[],
      confirmationDialog:false,

      model: null,

      selectRules: [
      v => !!v  || "Please select supervisor"
    ],

      headers: [
        { text: "Surname", value: "surname", align: "left" },
        { text: "Other Names", value: "othernames", align: "left" },
        { text: "Payroll Number", value: "payroll", align: "left" },
        { text: "Designation", value: "designation" },
        { text: "Programe", value: "programe" },
        { text: "Nationalty", value: "nationality" },
        { text: "ID Number", value: "idno" }
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
      this.getSelecteSupervisorId =this.supervisor_id;
      console.log("THE SUP :::: ", this.getSelecteSupervisorId);
    },

    async fetchEmployee() {
      await api.getEntries("getAllSupervisors").then(empList => {
        this.employeeList = empList;
        console.log("agik",empList)
      });
    },

    async fetchSupervisors() {
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

    async addrecord(payload) {
      await api.addEntry("assignSupervisor", payload).then(add => {
        this.popupDialog = true;
        this.msg = "Supervisor successfully assigned";
      });
    },

    getSelected(item) {
      if (this.selectedItems.includes(item)) {
        console.log("item name available  ");
        this.selectedItems.pop(item);
      } else {
        console.log(" Not item name available  ");
        this.selectedItems.push(item);
        //this.selectedItems.push(item);
      }
      console.log(this.selectedItems);
    },
    saveRecord() {
      console.log("TEST : ", this.supervisor_id);
      // this.addrecord(this.selectedItems)
       for (var i = 0; i < this.selectedItems.length; i++) {
         this.selectedresult.push({supervisor_id: this.supervisor_id,
                                   emp_payroll_no:this.selectedItems[i].payroll_no})
     } 
      
       console.log("Saving the record  ***  selectedresult#### ",this.selectedresult);
       if(this.selectedresult.length>0 && this.selectedresult.supervisor_id !=0){
         this.addrecord(this.selectedresult)
         this.fetchEmployee()
         this.selectedItems =[]
       }else{
         this.confirmationDialog=true
         this.msg ="Select employee(s) to assign a supervisor "

       }
       
     // console.log("Saving the record ***  ",this.selectedItems);
     // console.log("Saving the record  ***  selectedresult ",this.selectedresult);
    },
    closeInfo(){
      this.confirmationDialog=false
    },
    submit() {
       console.log("Saving the record  ",this.$refs.selectSupervisor.validate());
      if(this.$refs.selectSupervisor.validate()){
        this.saveRecord();
      console.log("Saving the record  777 ",this.$refs.selectSupervisor.validate());

      }else{
        this.confirmationDialog= true
        this.msg ="Please select supervisor"
      }
      
    }
  },
  created() {
    this.fetchEmployee();
    this.fetchSupervisors();
    
  },
  watch: {
    popupDialog(val) {
      if (!val) return;

      setTimeout(() => (this.popupDialog = false), 2000);
    }

  }

 
};
</script>
content_copy

