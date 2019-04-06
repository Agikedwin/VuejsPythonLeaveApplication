<template>

 <v-layout   >

   <template>
  <div class="text-xs-center">
    <v-dialog
      v-model="dialog"
      width="500" persistent
    >
      

      <v-card >
        <v-card-title>
         
        
         <span class="teal--text">Add Cadre</span>
         <v-spacer></v-spacer>
         <v-btn fab small  @click="closeDialog"><v-icon class="teal--text">close</v-icon></v-btn>
        </v-card-title>

       <v-card-text>
        <v-form v-model="valid" ref="form">
    <v-text-field
    color="teal"
      v-model="desigForm.name"
      label=" Cadre Name"
      :rules="nameRules"
      required
    ></v-text-field>

    <v-select label="Cadre Level"
     color="teal" 
     v-model="desigForm.department" 
     :items="listDepartments"  
     @change="selectedDept(desigForm.department)" 
      :rules="nameRules"                       
      required></v-select> 
      <v-card-actions>
    <v-spacer></v-spacer>
    <v-btn @click="submit('save')" color="teal--text">submit</v-btn>
     </v-card-actions>
     

  </v-form>       
 </v-card-text>
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
                color="teal--text"                
                absolute
                top
                right
                fab
                small
                @click="showDialog"
              >
                <v-icon class="teal--text">add</v-icon>
              </v-btn>
            </v-fab-transition>
      
    </v-card-title>
    <div class="text-xs-center" v-if="progressBar">
      <v-progress-circular :size="50" color="teal" indeterminate></v-progress-circular>
    </div>
    
  <v-data-table
    :headers="headers"
    :items="desigData"
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
      <td>{{ props.item.designation_id }}</td>
      <td class="text-xs-left">{{ props.item.designation_name }}</td>
      <td class="text-xs-left">{{ props.item.department_id}}</td>
      <td class="text-xs-left" >
      <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn flat fab class="teal--text" v-on="on" @click="editDept(props.item)">
                <v-icon   >edit</v-icon>
              </v-btn>
            </template>
            <span>Edit</span>
          </v-tooltip>
        </td>
      <td class="text-xs-left" >
        <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn flat fab class="teal--text" v-on="on" @click="deleteDept(props.item)">
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

 

  data: () => ({
     pagination: { rowsPerPage: 10 },
    desigForm: {
      name: "",
      department:"",
      designation:"",
      level:"",
      department_id:"",
      designation_id:0,      

    },
    
    fetchDepartments:[],
    listDepartments:[],
    desigData:[],
    deptData:[],
    dialog:false,
    msg:'',
    popupDialog: false,
    popupDialogfailed:false,
    popupColor:'',

    confirmationDialog:false,
    progressBar:false,

    valid: false,
    nameRules: [
      v => !!v || "Field is required",
      v => (v && v.length >= 2) || "Name must be less than 2 characters"
    ],

    selectRules: [v => !!v || "You must provide description"], 

     headers: [
          {text: 'Designation Id', value: 'name', sortable:false},
          { text: 'Designation Name', value: 'designation' , sortable:false },
          { text: 'Department', value: 'desig' , sortable:false },
           { text: 'Edit', value: 'edit' , sortable:false},
            { text: 'Delete', value: 'delete', sortable:false }
        ],
       
      
  }),
  methods: { 

  async getAllDesignations() { 

      await api
        .getEntries("getAllDesignations")
        .then(data => {
          
            this.desigData = data;
            this.progressState = false;
         
        })
        .catch(error => {
          console.log(error);
        });
    },
    
    async getRecordDept() { 

      await api
        .getEntries("getDepts")
        .then(data => {
          
            this.deptData = data;
          
         
        })
        .catch(error => {
          console.log(error);
        });
    },

    async addRecord(payload) {
     
      await api
        .addEntry("addDesignation", payload)
        .then(data => {
            this.msg ="Record successfully saved"
            this.getAllDesignations()
            this.popupDialog=true  
        })
        .catch(error => {
           this.msg ="Record Failed to saved"
             this.popupDialogfailed=true
              this.dialog=false
          console.log(error);
        });
    },

    async update(payload,deptid) {
     
      await api
        .editEntry("designation",deptid, payload)
        .then(data => {
          this.msg ="Record successfully saved"
            this.getAllDesignations()
            this.popupDialog=true 
        })
        .catch(error => {
          console.log(error);
        });
    },

    async delete(deptid,payload) {
     
      await api
        .deleteEntry("designation", deptid,payload)
        .then(data => {
           this.msg ="Record successfully deleted"
            this.getAllDesignations()
            this.popupDialog=true 
          //this.getRecord();
          
        })
        .catch(error => {
          console.log(error);
        });
    },
    closeDialog(){
      this.dialog=false
    },

    submit(val) {  
       if(val=="save")  {
     if (this.$refs.form.validate()) {
      
      if(this.desigForm.designation_id ==0){
        this.addRecord(this.desigForm);
      } else{
        this.update(this.desigForm, this.desigForm.designation_id)
      }
      this.desigForm.designation_id=0;
      }
       }
      if (val == "ok") {
        this.delete( this.desigForm.designation_id,  this.desigForm);
        this.confirmationDialog = false;
      }
      if (val == "no") {
        this.confirmationDialog = false;
      }
      this.deptForm == {};
     
      
    },
     async getDepartments(){
       await api.getEntries("getDepts").then(data =>{
         this.fetchDepartments = data
         console.log("DEPARTMENTS::::",this.fetchDepartments)

       })
       for(var i=0;i<this.fetchDepartments.length;i++){
         this.listDepartments.push(this.fetchDepartments[i].department_name)
       }
      
    },
    selectedDept(data){
      for(var i=0;i<this.fetchDepartments.length;i++){
        if(this.fetchDepartments[i].department_name==this.desigForm.department){         
          this.desigForm.department_id = this.fetchDepartments[i].department_id;
           console.log("the dep id ***",this.desigForm.department_id)
           break
           this.desigForm.department_id ='';
           this.desigForm.department_name = '';
        }
       }


    },

    showDialog(){    
     this.dialog=true
     this.$refs.form.reset()
    },
    
    clear() {
      //this.$refs.form.reset()let myObj = { name: 'Skip', breed: 'Labrador' };
      //localStorage.setItem(myObj, JSON.stringify(myObj));
      //this.getRecord()
      //console.log(localStorage.getItem(myObj))
       //getRecord()
    },
    editDept(selected){
      this.dialog=true;
      this.desigForm.designation_id = selected.designation_id
      this.desigForm.name = selected.designation_name;
      this.desigForm.description= selected.department_id;
      this.desigForm.department= selected.department_id
      
    },
    deleteDept(selected){
       this.msg ="Delete this record"
       this.desigForm.designation_id = selected.designation_id
      this.desigForm.name = selected.designation_name;
      this.desigForm.description= selected.department_id;
      this.desigForm.department= selected.department_id
    this.confirmationDialog=true

    }
  },
  created() {
      this.getAllDesignations()
      this. getRecordDept()
      this.getDepartments();
      
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

