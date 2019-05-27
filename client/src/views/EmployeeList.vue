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
    <v-flex xs12 sm12>
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
        <td class="text-xs-left"><v-btn flat fab small @click="viewEmployee(props.item)" ><v-icon class="teal--text">visibility</v-icon></v-btn></td>
        <td class="text-xs-left"><v-btn flat fab small @click="EditEmployee(props.item)" ><v-icon class="teal--text">edit</v-icon></v-btn></td>

      </template>
      <v-alert slot="no-results" :value="true" color="error" icon="warning">
        Your search for "{{ search }}" found no results.
      </v-alert>
    </v-data-table>
    </v-flex>
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

        headers: [
          {text:'Surname', value:'surname' ,align: 'left',  },
          { text: 'Other Names', value: 'othernames' ,align: 'left',},
          { text: 'Payroll Number', value: 'payroll' ,align: 'left',},
          { text: 'Designation', value: 'designation' },
          { text: 'Programe', value: 'programe' },
          { text: 'Nationalty', value: 'nationality' },
          { text: 'ID Number', value: 'idno' },
          { text: 'View', value: 'view' },
          { text: 'Edit', value: 'edit' }
        ],
        
      }
    },
    methods:{
        async fetchEmployee(){
            await api.getEntries('getAllEmployees')
            .then(empList =>{
                this.employeeList = empList
                console.log("EMP ************", this.employeeList)
            })

        },
        EditEmployee(items){
          console.log("here")
        this.$router.push({ name: "register", params: { userId: items } });
         console.log("here 2")

        },
        viewEmployee(items){
           this.$router.push({ name: "employeeview", params: { view: items } });
        },
    },
    created(){
        this.fetchEmployee();
     console.log("EMP ************", this.employeeList)
    }
  }
</script>