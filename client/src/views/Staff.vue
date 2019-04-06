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
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="employeeList"
      :search="search"
    >
      <template slot="items" slot-scope="props">

        <td class="text-xs-left">{{ props.item.payroll_no }}</td>
        <td class="text-xs-left">{{ props.item.surname }}</td>
        <td class="text-xs-left">{{ props.item.other_names }}</td>
        <td class="text-xs-left">{{ props.item.designation }}</td>
        <td class="text-xs-left">{{ props.item.program }}</td>
        <td class="text-xs-left">{{ props.item.nationalty }}</td>
        <td class="text-xs-left">{{ props.item.passport_idno }}</td>
        <td class="text-xs-left"><router-link class="teal--text" :to="{ name: 'assignedsupervisor', params: { id: props.item.payroll_no }}">View</router-link></td>
      </template>
      <v-alert slot="no-results" :value="true" color="error" icon="warning">
        Your search for "{{ search }}" found no results.
      </v-alert>
    </v-data-table>
  </v-card>
</template>


<script>
import api from '../apis/api'
  export default {
    data () {
      return {
        search: '',        
        employeeList :[],
        addDetails:'addDetails',

        headers: [
            
          { text: 'Payroll Number', value: 'payroll' ,align: 'left',},
          {text:'Surname', value:'surname' ,align: 'left',  },
          { text: 'Other Names', value: 'othernames' ,align: 'left',},
          { text: 'Designation', value: 'designation' },
          { text: 'Programe', value: 'programe' },
          { text: 'Nationalty', value: 'nationality' },
          { text: 'ID Number', value: 'idno' },
          { text: 'Actions', value: 'action' }
        ],
        
      }
    },
    methods:{
        async fetchEmployee(){
            await api.getEntries('getAllStaff')
            .then(empList =>{
                this.employeeList = empList
                console.log("EMP ************", this.employeeList)
            })

        },
        getSupEmployees(){
            this.$router.push({ name: 'assignedsupervisor', params: { userId:"assignedsupervisoragik12345" } })

        }
    },
    created(){
        this.fetchEmployee();
     
    }
  }
</script>