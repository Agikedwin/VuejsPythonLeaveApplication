<template>
  <v-layout justify-center>
    <v-flex xs12 sm12>
      

      <v-card>
        <v-container
          fluid
          grid-list-md
        >
          <v-layout row wrap>
            <v-flex
              v-for="card in cards"
              :key="card.title"
              v-bind="{ [`xs${card.flex}`]: true }"
            >
              <v-card>
                <v-img
                  :src="card.src"
                  height="200px"
                >
                  <v-container
                    fill-height
                    fluid
                    pa-2
                  >
                    <v-layout fill-height>
                      <v-flex xs12 align-end flexbox>
                       <v-data-table
                          :headers="headers"
                          :items="employeeList"
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
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-img>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn icon>
                    <v-icon>favorite</v-icon>
                  </v-btn>
                  <v-btn icon>
                    <v-icon>bookmark</v-icon>
                  </v-btn>
                  <v-btn icon>
                    <v-icon>share</v-icon>
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-flex>
  </v-layout>
</template>


<script>
import api from '../apis/api'
  export default {
    
    data: () => ({
      employeeList:[],
      headers: [        
          
           {text:'Leave Type', value:'surname' ,align: 'left',  },
          { text: 'Leave Days', value: 'programe' },
           { text: 'Days Remaining', value: 'nationality' },
          { text: '% Used', value: 'nationality' }
        ],
      cards: [
        { title: 'LIST OF REGISTRED EMPLOYEE GOES HERE', src: '', flex: 12 },
        { title: 'LEAVE APPLICATIONS STATUS HERE', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 6 },
        { title: 'PENDING APPLICAIONS GOES HERE', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6 }
      ]
    }),

    methods:{
           async fetchLeaveApplication(){
            await api.getEntries('leaveHistory')
            .then(empList =>{
              this.employeeList = empList
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
    },
    created() {
      this.fetchLeaveApplication()
    },
  }
</script>