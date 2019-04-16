import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Department from './views/Department.vue';
import RegisterEmployees from './views/RegisterEmployees.vue'
import EmployeeList from './views/EmployeeList.vue'
import AddDetails from './views/AddDetails.vue'
import Designations from './views/Designations.vue'
import LeaveTypes from './views/LeaveTypes.vue'
import LeaveApplication from './views/LeaveApplication.vue'
import LeaveApprovals from './views/LeaveApprovals.vue'
import ApplicationHistory from './views/ApplicationHistory.vue'
import LeaveBalance from './views/LeaveBalance.vue'
import EmployeesLeaveApplications from './views/EmployeesLeaveApplications.vue'
import AssignSupervisor from './views/AssignSupervisor.vue'
import EmployeeSupervisor from './views/EmployeeSupervisor.vue'
import Staff from './views/Staff.vue'
import EmployeesAssignedSupervisors from './views/EmployeesAssignedSupervisors.vue'
import Supervisor from './views/Supervisor.vue'
import Holidays from './views/Holidays.vue'
import InitialLeaveBalances from './views/InitialLeaveBalances.vue'
import EmployeeView  from './views/EmployeeView.vue'
import EmployeesLeaveBalance from './views/EmployeesLeaveBalance.vue'
import ChangePassword from './views/ChangePassword.vue'
import App from './App.vue'




Vue.use(Router);

const routerNav = new Router({
  routes: [
    {
      path: '/welcome',
      name: 'welcome',
      component: App,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    {
      path: '/home',
      name: 'home',
      component: Home,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    {
      path: '/',
      name: 'leavetypebalances',
      component: EmployeesLeaveBalance,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    {
      path: '/level',
      name: 'level',
      component: Department,
      meta: { 
        requiresAuth: true
    }
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterEmployees,
      meta: { 
        requiresAuth: true
    }
    },
    {
      path: '/designation',
      name: 'designation',
      component: Designations,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    {
      path: '/leaveType',
      name: 'leaveType',
      component: LeaveTypes,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    {
      path: '/employeeList',
      name: 'employeeList',
      component: EmployeeList,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    {
      path: '/addDetails',
      name: 'addDetails',
      component: AddDetails,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    {
      path: '/leaveApplication',
      name: 'leaveApplication',
      component: LeaveApplication,
      meta: { 
        requiresAuth: true,
        is_admin : false
    }

      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      //component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
    },
    {
      path: '/leaveApproval',
      name: 'leaveApproval',
      component: LeaveApprovals,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }

    },
    {
      path: '/applicationHistory',
      name: 'applicationHistory',
      component: ApplicationHistory,
      meta: { 
        requiresAuth: true,
        is_admin : false
    }
    },
    {
      path: '/leaveBalance',
      name: 'leaveBalance',
      component: LeaveBalance,
      meta: { 
        requiresAuth: true,
        is_admin : false
    }
    },
    {
      path: '/allapplications',
      name: 'allapplications',
      component: EmployeesLeaveApplications,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },

    {
      path: '/assinsupervisor',
      name: 'assinsupervisor',
      component: AssignSupervisor,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    {
      path: '/employeesupervisor',
      name: 'employeesupervisor',
      component: EmployeeSupervisor,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    {
      path: '/staff',
      name: 'staff',
      component: Staff,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    {
      path: '/assignedsupervisor',
      name: 'assignedsupervisor',
      component: EmployeesAssignedSupervisors,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    {
      path: '/supervisor',
      name: 'supervisor',
      component: Supervisor,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    {
      path: '/holidays',
      name: 'holidays',
      component: Holidays,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    {
      path: '/initialleavebalance',
      name: 'initialleavebalance',
      component: InitialLeaveBalances,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    {
      path: '/employeeview',
      name: 'employeeview',
      component: EmployeeView,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    {
      path: '/leavetypebalances',
      name: 'leavetypebalances',
      component: EmployeesLeaveBalance,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    {
      path: '/changepassword',
      name: 'changepassword',
      component: ChangePassword,
      meta: { 
        requiresAuth: true,
        is_admin : true
    }
    },
    
  ],

  
});

routerNav.beforeEach((to, from, next) => {
 // only authenticated routes to be visited
 let userDesignation: any;
 userDesignation = localStorage.getItem('userSession');
 // check if token is still valid
 if(localStorage.getItem('tokenKey') != null){
  //check if the route requested by admin adn desgnation is less than 6
  if(to.matched.some(record => record.meta.is_admin)) {
    if(userDesignation < 6) {
      next();
    }
  }else {
    // if the route is not for admin
    if(!to.matched.some(record => record.meta.is_admin)){
      next();
    }

  }
}

})

export default routerNav 


