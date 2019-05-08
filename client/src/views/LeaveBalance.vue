<template>
  <v-card>

    <div class="text-xs-center" v-if="progressBar">
      <v-progress-circular :size="50" color="teal" indeterminate></v-progress-circular>
    </div>
  
    <v-data-table
      :headers="headers"
      :items="employeeList"
      :pagination.sync="pagination"
    >
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
import api from '../apis/api'
  export default {
    data () {
      return {
        search: '',        
        employeeList :[],
        addDetails:'addDetails',
        valueDeterminate:0,
        pagination: { rowsPerPage: 10 },

        approveForm:{
          approval_id:"",
          application_id:"",
          payroll_no:"",
          aproval_status:"",
          note:""

        },
        progressBar:true,

        headers: [        
          
           {text:'Leave Type', value:'surname' ,align: 'left',  },
          { text: 'Leave Days', value: 'programe' },
           { text: 'Days Remaining', value: 'nationality' },
          { text: '% Used', value: 'nationality' }
        ],
        
      }
    },
    methods:{
        async fetchLeaveApplication(){
            await api.getEntries('leaveHistory')
            .then(empList =>{
              this.employeeList = empList
              console.log("THIS IS TEST ::: ", this.employeeList)
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
            })

        },

        actualValue(){
          var x= 100;
          var y= 25
          var z =10

        }

       
      
     
    },
    created(){
        this.fetchLeaveApplication();
    }
  }
</script>