<template>

  <v-card>
     <div class="text-xs-center" v-if="progressBar">
    <v-progress-circular
      :size="50"
      color="teal"
      indeterminate
    ></v-progress-circular>
    </div>
  
    <v-data-table
      :headers="headers"
      :items="employeeList"
      :pagination.sync="pagination"
      
    >
   
      <template slot="items" slot-scope="props"> 
        <td class="text-xs-left">{{ props.item.payroll_no }}</td>
        <td class="text-xs-left">{{ props.item.surname }} {{ props.item.other_names }}</td>
        <td class="text-xs-left">{{ props.item.leave_type }}</td>
        <td class="text-xs-left">{{ props.item.date_from }}</td>
        <td class="text-xs-left">{{ props.item.date_to }}</td>
        
        <div v-if="props.item.approved==0">
          <td class="text-xs-left">
            <v-tooltip bottom>
              <template v-slot:activator="{ on }">
                <v-btn flat fab class="blue--text"  v-on="on">
                  <v-icon >info</v-icon>
                </v-btn>
              </template>
              <span > Pending</span>
            </v-tooltip>
          </td>
        </div>
        <div v-if="props.item.approved==1">
          <td class="text-xs-left">
            <v-tooltip bottom>
              <template v-slot:activator="{ on }">
                <v-btn flat fab class="teal--text"  v-on="on">
                  <v-icon >done_outline</v-icon>
                </v-btn>
              </template>
              <span>Approved</span>
            </v-tooltip>
          </td>
        </div>
        <div v-if="props.item.approved==2">
          <td class="text-xs-left">
            <v-tooltip bottom>
              <template v-slot:activator="{ on }">
                <v-btn flat fab class="red--text"  v-on="on">
                  <v-icon  >info</v-icon>
                </v-btn>
              </template>
              <span>Declined</span>
            </v-tooltip>
          </td>
        </div>
        
        
      </template>
     
    </v-data-table>
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

        approveForm:{
          approval_id:"",
          application_id:"",
          payroll_no:localStorage.getItem('userSession'),
          aproval_status:"",
          note:""

        },
        leave_state:false,
        progressBar:true,

        headers: [
         
          { text: 'Applicant Payroll', value: 'othernames' ,align: 'left',},
          { text: 'Applicant name', value: 'othernames' ,align: 'left',},
           {text:'Leave Type', value:'surname' ,align: 'left',  },
          { text: 'Date From', value: 'payroll' ,align: 'left',},
          { text: 'Date To', value: 'designation' },
          { text: 'Status', value: 'programe' }
          
        ],
        
      }
    },
    methods:{
        async fetchLeaveApplication(){
            await api.getEntries('getLeaveApplicationsHistory')
            .then(empList =>{
              console.log("APPS  ",empList)
               setTimeout(duration => {                       
                this.leave_state = empList.approved
                this.employeeList = empList
                 this.progressBar = false;
                        },1000)              
            })

        },

        async addRecord(paylaod){
          await api.addEntry('addApprovals',paylaod)
          .then(data =>{
            console.log('data added ',data)
          })
        },

      approveSelected(data){
       console.log("test******888")
       this.approveForm.approval_id =data.approval_id;
       this.approveForm.application_id = data.application_id;
       this.approveForm.aproval_status= true;
       if(this.approveForm.application_id){
         this.addRecord(this.approveForm);
         this.approveForm='';
         this.fetchLeaveApplication();
         
       }else{
       }
      },
      declineSelected(data){
        this.approveForm.approval_id =data.approval_id;
       this.approveForm.approval_id = data.application_id;
       this.approveForm.aproval_status= false;

       if(this.approveForm.application_id){
         this.addRecord(this.approveForm);
          this.approveForm='';
          this.fetchLeaveApplication()
         
       }


      },
      submit(){
        this.addRecord(approveForm);
      }
    },
    created(){
        this.fetchLeaveApplication();
     console.log("EMP ************ 1111")
    }
  }
</script>