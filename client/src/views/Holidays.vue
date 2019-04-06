<template>
  <v-layout>
    <div class="text-xs-center">
      <v-dialog v-model="dialog" width="500" persistent>
        <v-card>
          <v-card-title>Add Public Holiday{{holidayForm.holiday_name}}
            <v-spacer></v-spacer>
            <v-btn fab small @click="close">
              <v-icon color="teal--text">close</v-icon>
            </v-btn>
          </v-card-title>

          <v-form v-model="valid" ref="form">
            <v-text-field
              v-model="holidayForm.holiday_name"
              label="  holiday_name"
              required
              :rules="nameRules"
              color="teal"
            ></v-text-field>

            <v-flex xs12 sm12 md12>
              <v-menu
                v-model="menu1"
                color="teal"
                :close-on-content-click="true"
                :nudge-right="40"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                min-width="290px"
              >
                <v-text-field
                  color="teal"
                  slot="activator"
                  v-model="holidayForm.holiday_date"
                  label="Holiday Date"
                  prepend-icon="event"
                  readonly
                  :rules="nameRules"
                ></v-text-field>
                <v-date-picker
                  color="teal"
                  v-model="holidayForm.holiday_date"
                  @input="menu1 = false"
                ></v-date-picker>
              </v-menu>
            </v-flex>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn @click="submit('save')" color="teal--text">submit</v-btn>
            </v-card-actions>
          </v-form>
        </v-card>
      </v-dialog>
    </div>

    <v-flex>
      <v-card>
        <v-card-title>
          <v-spacer></v-spacer>
          <v-fab-transition style="height: 100px; position: relative">
            <v-btn color="teal--text" absolute top right small fab @click="showDialog">
              <v-icon>add</v-icon>
            </v-btn>
          </v-fab-transition>
        </v-card-title>

        <v-data-table :headers="headers" :items="holidayData" :pagination.sync="pagination">
          <template slot="headerCell" slot-scope="props">
            <v-tooltip bottom>
              <span slot="activator">{{ props.header.text }}</span>
              <span>{{ props.header.text }}</span>
            </v-tooltip>
          </template>

          <template slot="items" slot-scope="props">
            <td>{{ props.item.holiday_id }}</td>
            <td class="text-xs-left">{{ props.item.holiday_name }}</td>
            <td class="text-xs-left">{{ props.item.holiday_date}}</td>
            <td class="text-xs-left">
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn flat fab class="teal--text" v-on="on" @click="editHoliday(props.item)">
                    <v-icon>edit</v-icon>
                  </v-btn>
                </template>
                <span>Edit</span>
              </v-tooltip>
            </td>
            <td class="text-xs-left">
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn flat fab class="teal--text" v-on="on" @click="deleteHoliday(props.item)">
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
      </v-card>
    </v-flex>
  </v-layout>
</template>
    <!--End  Confirmation dialog -->
   
  

<script>
import { validationMixin } from "vuelidate";
import { required, maxLength } from "vuelidate/lib/validators";
import api from "../apis/api";

export default {
  mixins: [validationMixin],

  data: () => ({
     pagination: { rowsPerPage: 10 },
    holidayForm: {
      holiday_name: "",
      holiday_date: "", 
      holiday_id:"",     
    },
    menu1: false,
    fetchHoliday: [],
    listHoliday: [],
    holidayData: [],
    holiday_Data: [],
    dialog: false,
    msg: "",
    popupDialog: false,
    popupDialogfailed: false,
    popupColor: "",

    confirmationDialog: false,

    valid: false,
    nameRules: [
      v => !!v || "Field is required",
      v => (v && v.length >= 2) || "Field must  not be less than 2 characters"
    ],

    selectRules: [v => !!v || "You must provide description"],

    headers: [
      { text: "Holiday Id", value: "holiday_name", sortable: false },
      { text: "Holiday Name", value: "Holiday", sortable: false },
      { text: "holiday_date", value: "desig", sortable: false },
      { text: "Edit", value: "edit", sortable: false },
      { text: "Delete", value: "delete", sortable: false }
    ]
  }),
  methods: {
    async getAllHolidays() {
      await api
        .getEntries("getHolidays")
        .then(data => {
          console.log("here ************   ", data);

          this.holidayData = data;
          this.progressState = false;
        })
        .catch(error => {
          console.log(error);
        });
    },

    async addRecord(payload) {
      await api
        .addEntry("addHoliday", payload)
        .then(data => {
          this.msg = "Record successfully saved";
          this.getAllHolidays();
          this.popupDialog = true;
        })
        .catch(error => {
          this.msg = "Record Failed to saved";
          this.popupDialogfailed = true;
          this.dialog = false;
          console.log(error);
        });
    },

    async update(deptid, payload) {
      await api
        .editEntry("hodiday", deptid, payload)
        .then(data => {
          this.getAllHolidays();
          this.msg = "Record successfully updated";
          this.getAllHolidays();
          this.popupDialog = true;
        })
        .catch(error => {
          this.msg = "Record Failed to update";
          this.popupDialogfailed = true;
          this.dialog = false;
        });
    },

    async delete(deptid, payload) {
      await api
        .deleteEntry("hodiday", deptid, payload)
        .then(data => {
          this.msg = "Record successfully deleted";
          this.getAllHolidays();
          this.popupDialog = true;
        })
        .catch(error => {
          this.msg = "Record Failed to delete";
          this.popupDialogfailed = true;
          this.dialog = false;
          console.log(error);
        });
    },
    close() {
      this.dialog = false;
    },

    submit(val) {
      console.log("val  ",val);
      console.log("VAlidate  ",this.$refs.form.validate())
      console.log(this.holidayForm);
      if (val == "save") {
        if (this.$refs.form.validate()) {
          if (this.holidayForm.holiday_id == 0) {
            this.addRecord(this.holidayForm);
          } else {
            this.update(this.holidayForm.holiday_id, this.holidayForm);
          }
          this.dialog = false;
      
        }
      }

      if (val == "ok") {
        this.delete(this.holidayForm.holiday_id, this.holidayForm);
        this.confirmationDialog = false;
      }
      if (val == "no") {
        this.confirmationDialog = false;
      }
      
    },

    showDialog() {
      this.$refs.form.reset();
      this.dialog = true;
    },

    clear() {
      //this.$refs.form.reset()let myObj = { holiday_name: 'Skip', breed: 'Labrador' };
      //localStorage.setItem(myObj, JSON.stringify(myObj));
      //this.getRecord()
      //console.log(localStorage.getItem(myObj))
      //getRecord()
    },
    editHoliday(selected) {
      this.dialog = true;
      this.holidayForm.holiday_id = selected.holiday_id;
      this.holidayForm.holiday_name = selected.holiday_name;
      this.holidayForm.holiday_date = selected.holiday_date;
      console.log("TEST  ",this.holidayForm)
    },
    deleteHoliday(selected) {
      this.confirmationDialog = true;
      this.msg = "Do you want to delete this record";
      this.holidayForm.holiday_id = selected.holiday_id;
    }
  },
  created() {
    this.getAllHolidays();
  },

  computed: {},
  watch: {
    popupDialog(val) {
      if (!val) return;

      setTimeout(() => (this.popupDialog = false), 2000);
    },

    popupDialogfailed(val) {
      if (!val) return;

      setTimeout(() => (this.popupDialogfailed = false), 2000);
    }
  }
};
</script>

<style>
.departments {
  padding: 5px;
}
.adddept {
}

.listDept {
}
</style>

