<template>

 <v-layout   >

   <template>
  <div class="text-xs-center">
    <v-dialog
      v-model="dialog"
      persistent
      width="500"
    >
      

      <v-card>
        <v-card-title 
        class="teal--text"        
        >
         Add LeaveTypes
         <v-spacer></v-spacer>
         <v-btn fab small @click="close"><v-icon class="teal--text">close</v-icon></v-btn>
        </v-card-title>

       
        <v-form v-model="valid" ref="form">
    <v-text-field
      v-model="leaveTypeForm.name"
      label=" Leave Name"
      color="teal"
      required
      :rules="nameRules"
    ></v-text-field>

    <v-text-field label="Number of Days" 
                         v-model="leaveTypeForm.no_days"
                         color="teal"
                          :rules="nameRules"
                         required></v-text-field> 
    
    <v-card-actions>
      <v-spacer></v-spacer>
    <v-btn @click="submit('save')" class="teal--text">submit</v-btn>
    </v-card-actions>
    

  </v-form>       

      </v-card>


    </v-dialog>

   
  </div>
</template>
    
    <v-flex >
    <v-card>  

      <v-card-title>
     
      <v-spacer></v-spacer>
      <v-fab-transition style="height: 100px; position: relative">
              <v-btn
                small              
                absolute
                top
                right
                fab
                persistent
                @click="showDialog"
              >
                <v-icon color="teal">add</v-icon>
              </v-btn>
            </v-fab-transition>
      
    </v-card-title>
    
  <v-data-table
    :headers="headers"
    :items="LeaveTypeData"
    :pagination.sync="pagination"
  >
    <template slot="headerCell" slot-scope="props">
      <v-tooltip bottom>
        <span slot="activator">
          {{ props.header.text }}
        </span>
        <span>
          {{ props.header.text }}
        </span>
      </v-tooltip>
    </template>
    <template slot="items" slot-scope="props">
      <td>{{ props.item.leave_id }}</td>
      <td class="text-xs-left">{{ props.item.leave_name }}</td>
      <td class="text-xs-left">{{ props.item.no_days }}</td>
      <td class="text-xs-left">{{ props.item.countinous}}</td>
      <td class="text-xs-left" >
      <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn flat fab class="teal--text" v-on="on" @click="editLeaveType(props.item)">
                <v-icon   >edit</v-icon>
              </v-btn>
            </template>
            <span>Edit</span>
          </v-tooltip>
        </td>
      <td class="text-xs-left" >
        <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn flat fab class="teal--text" v-on="on" @click="deleteLeaveType(props.item)">
                <v-icon   >delete</v-icon>
              </v-btn>
            </template>
            <span>Delete</span>
          </v-tooltip>  
      
      
      </td>
    </template>
  </v-data-table>
   

    <v-dialog
      v-model="popupDialog"
      hide-overlay
      persistent
      width="500"
    >
      <v-card
        color="success"
        dark
      >
        <v-card-text>
         {{msg}}<span><v-icon>ok</v-icon></span>
          
        </v-card-text>
      </v-card>
    </v-dialog>

    <v-dialog
      v-model="popupDialogfailed"
      hide-overlay
      persistent
      width="500"
    >
      <v-card
        color="danger"
        dark
      >
        <v-card-text>
         {{msg}}<span><v-icon>ok</v-icon></span>
          
        </v-card-text>
      </v-card>
    </v-dialog>

      <!-- Confirmation dialog -->
    <template>
      <v-layout row justify-center>
        <v-dialog v-model="confirmationDialog" persistent max-width="250">
          <v-card>
            <v-card-text>{{msg}}</v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="green darken-1" value="no" flat="flat" @click="submit('no')">No</v-btn>

              <v-btn color="green darken-1" value="ok" flat="flat" @click="submit('ok')">Yes</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-layout>
    </template>
    <!--End  Confirmation dialog -->


      </v-card>
    </v-flex>
  </v-layout>  
  
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, maxLength } from "vuelidate/lib/validators";
import api from '../apis/api';

export default {
  mixins: [validationMixin],

  validations: {
    name: { required, maxLength: maxLength(10) },
    select: { required },
    checkbox: {
      checked(val) {
        return val;
      }
    }
  },

  data: () => ({
     pagination: { rowsPerPage: 10 },
    leaveTypeForm: {
      name: "",
      no_days:"",
      continous:0,
      leave_id:0,
    },
    fetchLeaveTypes:[],
    listLeaveTypes:[],
    LeaveTypeData:[],
    dialog:false,

    msg:'',
    popupDialog: false,
    popupDialogfailed:false,
    popupColor:'',

    confirmationDialog:false,

    valid: false,
    nameRules: [
      v => !!v || "The field  is required",
     
    ],

     headers: [
          {text: 'Leave Type Id', value: 'name', sortable:false},
          { text: 'Leave  Name', value: 'name' , sortable:false },
          { text: 'Leave days', value: 'days' , sortable:false },
          { text: 'Continous', value: 'desig' , sortable:false },
           { text: 'Edit', value: 'edit' , sortable:false},
            { text: 'Delete', value: 'delete', sortable:false }
        ],
       
      
  }),
  methods: { 

  async getAllLeaveTypes() { 

      await api
        .getEntries("getAllLeaveTypes")
        .then(data => {
          
            this.LeaveTypeData = data;
            this.progressState = false;
         
        })
        .catch(error => {
          console.log(error);
        });
    },
    
    

    async addRecord(payload) {
     
      await api
        .addEntry("addLeaveTypes", payload)
        .then(data => {
            this.msg ="Record successfully saved"
            this.getAllLeaveTypes()
            this.popupDialog=true  
             this.leaveTypeForm.leave_id =0
        })
        .catch(error => {
           this.msg ="Record Failed to saved"
             this.popupDialogfailed=true
              this.dialog=false
          console.log(error);
        })    
        
    },

    async update(leaveid,payload) {
     
      await api
        .editEntry("leaveTypes",leaveid, payload)
        .then(data => {
           this.msg ="Record successfully updated"
            this.getAllLeaveTypes()
            this.popupDialog=true 
             this.leaveTypeForm.leave_id =0 
        })
        .catch(error => {
          this.msg ="Record Failed to saved"
             this.popupDialogfailed=true
              this.dialog=false
          console.log(error);
        });

        
    },

    async delete(leaveid,payload) {
     
      await api
        .deleteEntry("leaveTypes", leaveid,payload)
        .then(data => {
            this.msg ="Record successfully deleted"
            this.getAllLeaveTypes()
            this.popupDialog=true  
             this.leaveTypeForm.leave_id = 0
        })
        .catch(error => {
         this.msg ="Record Failed to delete record"
             this.popupDialogfailed=true
              this.dialog=false
          console.log(error);
        });
       
    },

    submit(val) {
      if(val=='save'){
      if(this.$refs.form.validate()){
        if(this.leaveTypeForm.leave_id==0){
        this.addRecord(this.leaveTypeForm);
      } else{
       this.update(this.leaveTypeForm.leave_id, this.leaveTypeForm)
      }
     
      }
      }
      if(val=='ok'){
        this.delete(this.leaveTypeForm.leave_id, this.leaveTypeForm)

      }
      if(val=='no'){
        this.confirmationDialog=false
      }

      
      this.dialog = false;
      this.confirmationDialog=false
      
    },
       showDialog(){    
     this.dialog=true
      this.$refs.form.reset()
    },
    close(){
      this.dialog=false
    },

   clear() {
      //this.$refs.form.reset()let myObj = { name: 'Skip', breed: 'Labrador' };
      //localStorage.setItem(myObj, JSON.stringify(myObj));
      //this.getRecord()
      //console.log(localStorage.getItem(myObj))
       //getRecord()
    },
      
    
    editLeaveType(selected){
      console.log('the data ::::', selected)
      this.dialog=true;
      this.leaveTypeForm.leave_id = +selected.leave_id;
      this.leaveTypeForm.name = selected.leave_name;
      this.leaveTypeForm.no_days = selected.no_days;
      this.leaveTypeForm.continous= selected.continous;

      console.log('the data ::::eeeeeeee', this.leaveTypeForm)
      
    },
    deleteLeaveType(selected){
      this.msg="Do you want to delete this record?"
      this.leaveTypeForm.leave_id = +selected.leave_id
      this.confirmationDialog=true
      console.log("testing........2")
    
  },
  },

  
  
  created() {
      console.log('reached here at created')
      
      this.getAllLeaveTypes()
    },

  computed: {
   
  },
   watch: {
      popupDialog (val) {
        if (!val) return

        setTimeout(() => (this.popupDialog = false), 2000)
      },

      popupDialogfailed (val) {
        if (!val) return

        setTimeout(() => (this.popupDialogfailed = false), 2000)
      }
    }
};
</script>

<style>
.departments{
padding: 5px;
}
.adddept{
  
}

.listDept{
  
}
</style>

