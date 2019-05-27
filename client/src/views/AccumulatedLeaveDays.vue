<template>
    <h1>TEST  LEAVE DAYS</h1>
</template>

<script>
import api from '../apis/api'
export default {

    methods:{

      async  accumulatedLeave(){
          await api.getEntries('accumulatedLeaveDays').then((value) => {
              console.log("THE VALUE ",value)
          })
        }

    },

created(){
    this.accumulatedLeave();



}
    
}
</script>
