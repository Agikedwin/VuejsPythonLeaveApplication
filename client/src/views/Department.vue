<template>
  <!--  <form>
    <v-text-field
      v-model="deptForm.name"
      :counter="10"
      label="Name"
      required
    ></v-text-field>
    <v-textarea
      v-model="deptForm.description"
      label="Description"
      required
    ></v-textarea>

    <v-btn @click="submit">submit</v-btn>
    <v-btn @click="clear">clear</v-btn>
  </form>-->
  <v-layout>
    <template>
      <div class="text-xs-center">
        <v-dialog v-model="dialog" width="500" persistent>
          <v-card>
            <v-card-title>
              <span class="teal--text">ADD LEVE </span>
              <v-spacer></v-spacer>
              <v-btn fab small @click="clear">
                <v-icon class="teal--text">close</v-icon>
              </v-btn>
            </v-card-title>
            <v-card-text>
              <v-form v-model="valid" ref="form">
                <v-text-field
                  color="teal"
                  v-model="deptForm.name"
                  label=" Department Name"
                  :rules="nameRules"
                  required
                  @input="changed"
                ></v-text-field>
                <v-textarea
                  color="teal"
                  v-model="deptForm.description"
                  label="Level"
                  required
                  :rules="selectRules"
                ></v-textarea>
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

    <v-flex>
      <v-card>
        <v-card-title>
          <div>
            <h3>LIST LEVELS</h3>
          </div>
          <v-spacer></v-spacer>
          <v-fab-transition style="height: 100px; position: relative">
            <v-btn color="gray" absolute top right fab small @click="showDialog">
              <v-icon class="teal--text">add</v-icon>
            </v-btn>
          </v-fab-transition>
        </v-card-title>

        <template>
  <v-layout>
    <v-flex xs12 sm12 offset-sm3>
      <v-card>
        ooo
      </v-card>
    </v-flex>
  </v-layout>
</template>

        <v-data-table :headers="headers" :items="deptData" class="elevation-1">
          <template slot="headerCell" slot-scope="props">
            <v-tooltip bottom>
              <span slot="activator">{{ props.header.text }}</span>
              <span>{{ props.header.text }}</span>
            </v-tooltip>
          </template>
          <template slot="items" slot-scope="props">
            <td>{{ props.item.department_id }}</td>
            <td class="text-xs-left">{{ props.item.department_name }}</td>
            <td class="text-xs-left">{{ props.item.description}}</td>
            <td class="text-xs-left">
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn flat fab class="teal--text" v-on="on" @click="editDept(props.item)">
                    <v-icon>edit</v-icon>
                  </v-btn>
                </template>
                <span>Edit</span>
              </v-tooltip>
            </td>
            <td class="text-xs-left">
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn flat fab class="teal--text" v-on="on" @click="deleteDept(props.item)">
                    <v-icon>delete</v-icon>
                  </v-btn>
                </template>
                <span>Delete</span>
              </v-tooltip>
            </td>
          </template>
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
import api from "../apis/api";

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
    deptForm: {
      name: "",
      description: "",
      department_id: 0
    },
    dialog: false,
    msg: "",
    popupDialog: false,
    popupDialogfailed: false,

    confirmationDialog: false,

    valid: false,
    nameRules: [
      v => !!v || "Name is required",
      v => (v && v.length >= 2) || "Name must be less than 10 characters"
    ],

    selectRules: [v => !!v || "You must provide description"],

    deptData: [],
    headers: [
      { text: "Department Id", value: "name", sortable: false },
      { text: "Department", value: "department", sortable: false },
      { text: "Description", value: "description", sortable: false },
      { text: "Edit", value: "edit", sortable: false },
      { text: "Delete", value: "delete", sortable: false }
    ]
  }),
  methods: {
   changed() {
     var conn = api.checkBackendConn()
   
       console.log("con*** 1", conn.Promise)
     if(!conn){
       this.$store.commit('change', 'Connected')
       
        console.log("con*** 1",)
     }else{
       this.$store.commit('change', 'diconnected')
        
        console.log("con*** 2",)
     }
    
    },

    async checkBackendConn() {
        console.log("THE axio")
       
        await axios.get(url)
        .then(data => {
            if (data) {
                result = true
                console.log("THE axio 1", result)
                 return true


            } else {
                console.log("THE axio 2", result)
                result = false

            }
        }).catch(error => {
            console.log("THE axio 3", error)
             return false
           
           
        })
       

    },

             

    async getRecord() {
      await api
        .getEntries("getDepts")
        .then(data => {
          this.deptData = data;
          this.progressState = false;
          this.progressBar = false;
        })
        .catch(error => {
          console.log(error);
        });
      this.deptForm.department_id = 0;
    },

    async addRecord(payload) {
      await api
        .addEntry("addDeptment", payload)
        .then(data => {
          console.log("ADD ENTRY  data", data);
          
          if (data.status == 200) {
            this.msg = "Record successfully saved";
            this.getRecord();
            this.popupDialog = true;
          } else {
            this.msg = "Record Failed to saved";
            this.popupDialogfailed = true;
          }
          this.deptForm.department_id == 0;
          console.log("ADD ENTRY ", this.deptForm);

          this.dialog = false;
        })
        .catch(error => {
          console.log(error);
        });
    },

    async update(payload, deptid) {
      await api
        .editEntry("department", deptid, payload)
        .then(data => {
          console.log("TEST DATA ::: ", data);

          if (data.status == 200) {
            this.msg = data.data.msg;
            this.popupDialog = true;
          } else {
            this.msg = data.data.msg;
            this.popupDialogfailed = true;
          }
          this.deptForm.department_id = 0;
          this.getRecord();
        })
        .catch(error => {
          console.log(error);
        });
    },

    async delete(deptid, payload) {
      await api
        .deleteEntry("department", deptid, payload)
        .then(data => {
          this.getRecord();
          if (data.status == 200) {
            this.msg = data.data.msg;
            this.popupDialog = true;
          } else {
            this.msg = data.data.msg;
            this.popupDialogfailed = true;
          }
          this.confirmationDialog = false;
          this.deptForm.department_id = 0;
        })
        .catch(error => {
          console.log(error);
        });
    },
    showDialog() {
      this.deptForm.department_id = 0;
      console.log(" this.deptForm.department_id ", this.deptForm.department_id);
      this.$refs.form.reset();

      this.dialog = true;
    },

    submit(val) {
      if (val == "save") {
        if (this.$refs.form.validate()) {
          console.log("DEPT ID ", this.deptForm.department_id);
          //this.addRecord(this.deptForm);
          if (this.deptForm.department_id == 0) {
            this.addRecord(this.deptForm);
          } else {
            this.update(this.deptForm, this.deptForm.department_id);
          }
          this.dialog = false;
        }
      }
      if (val == "ok") {
        this.delete(this.deptForm.department_id, this.deptForm);
        this.confirmationDialog = false;
      }
      if (val == "no") {
        this.confirmationDialog = false;
      }
      this.deptForm == {};
    },

    clear() {
      this.dialog = false;
    },
    editDept(selected) {
      this.deptForm.name = selected.department_name;
      this.deptForm.description = selected.description;
      this.deptForm.department_id = selected.department_id;
      this.dialog = true;
    },
    deleteDept(selected) {
      this.msg = "Do you want to delete this record?";
      this.deptForm.name = selected.department_name;
      this.deptForm.description = selected.description;
      this.deptForm.department_id = selected.department_id;

      this.confirmationDialog = true;
    }
  },
  created() {
    console.log("reached here at created");
    this.getRecord();
   
   
  },

  computed: {},
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
};
</script>

<style>
.departments {
  padding: 5px;
}
.adddept {
  width: 490px;
}

.listDept {
}
</style>

