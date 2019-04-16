<template>
  <v-card>
    <v-card-title>
      Employee List
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="search"
        label="Search"
        single-line
        hide-details
        color="teal"
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="employeeList"
      :search="search"
      :pagination.sync="pagination"
    >
      <template slot="items" slot-scope="props">
        <td class="text-xs-left">{{ props.item.surname }}</td>
        <td class="text-xs-left">{{ props.item.other_names }}</td>
        <td class="text-xs-left">{{ props.item.payroll_no }}</td>
        <td class="text-xs-left">{{ props.item.designation }}</td>
        <td class="text-xs-left">{{ props.item.program }}</td>
        <td class="text-xs-left">{{ props.item.nationalty }}</td>
        <td class="text-xs-left">{{ props.item.passport_idno }}</td>
        <td class="text-xs-left" ><span class="red--text">{{ props.item.leave_balance }}</span></td>
        <td class="text-xs-left"><v-btn  flat fab  @click="leaveBalance(props.item)"><v-icon  class="teal--text">add</v-icon></v-btn></td>
      </template>
      <v-alert slot="no-results" :value="true" color="error" icon="warning">
        Your search for "{{ search }}" found no results.
      </v-alert>
    </v-data-table>

    <v-dialog persistent v-model="dialog"  width="500">
        <v-card>
            <v-form v-model="valid" ref="form">
            <v-card-title class="teal--text">
                Enter Leave Balance
                <v-spacer></v-spacer>
                <v-btn flat fab  @click="closeDialog"><v-icon class="teal--text">close</v-icon></v-btn>
                
            </v-card-title >
            <v-divider></v-divider>
            <v-card-text >
                <v-text-field
                label="" 
                type="number"           
                v-model="balanceForm.leave_balance"
                color="teal"
                :rules="nameRules"
                >
                </v-text-field>

                </v-card-text>
                <v-card-actions>
                    <v-spacer> </v-spacer>
                        <v-btn small @click="submit" class="teal--text">submit</v-btn>
                   
                </v-card-actions>
                </v-form>
        </v-card>

    </v-dialog>


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
  </v-card>
</template>


<script>
import api from '../apis/api'
  export default {
    data () {
      return {
         pagination: { rowsPerPage: 10 },
        search: '',        
        employeeList :[],
        addDetails:'addDetails',
        dialog:false,
        popupDialogfailed:false,
        popupDialog:false,
        msg:"",

        balanceForm:{
            leave_balance:"",
            payroll_no:""
        },

        headers: [
          {text:'Surname', value:'surname' ,align: 'left',  },
          { text: 'Other Names', value: 'othernames' ,align: 'left',},
          { text: 'Payroll Number', value: 'payroll' ,align: 'left',},
          { text: 'Designation', value: 'designation' },
          { text: 'Programe', value: 'programe' },
          { text: 'Nationalty', value: 'nationality' },
          { text: 'ID Number', value: 'idno' },
          { text: 'Leave Balance', value: 'balance' },
          { text: 'Leave Balance', value: 'action' }
        ],

        valid: false,
    nameRules: [
      v => !!v || "Name is required",
      v => (v && v.length >= 1) || "Name must be less than 10 characters"
    ],
        
      }
    },
    methods:{
        async fetchEmployee(){
            await api.getEntries('getAllBalance')
            .then(empList =>{
                this.employeeList = empList
                console.log("EMP ************", this.employeeList)
            })

        },
        async addRecord(payload){
            await api.addEntry("addLeaveBalance",payload).then(data =>{

            this.msg = "Record successfully saved";
            this.popupDialog = true;  
            this.fetchEmployee()        

            }).catch(error =>{
                this.msg = "Record Failed to saved";
            this.popupDialogfailed = true;
            })
        },
        leaveBalance(selected){
            this.balanceForm.payroll_no=selected.payroll_no

            this.dialog=true

        },
        closeDialog(){
            this.dialog=false
        },
        submit(){
            console.log(this.balanceForm)
            if(this.$refs.form.validate()){
                this.addRecord(this.balanceForm)
            }
           

        }
    },
    created(){
        this.fetchEmployee();
     
    },

    watch: {
    popupDialog(val) {
      if (!val) return;

      setTimeout(() => (this.popupDialog = false), 3000);
    },

    popupDialogfailed(val) {
      if (!val) return;

      setTimeout(() => (this.popupDialogfailed = false), 3000);
    }
  }
  }
</script>