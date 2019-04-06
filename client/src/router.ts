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

export default new Router({
  routes: [
    {
      path: '/welcome',
      name: 'welcome',
      component: App
    },
    {
      path: '/home',
      name: 'home',
      component: Home,
    },
    {
      path: '/',
      name: 'leavetypebalances',
      component: EmployeesLeaveBalance
    },
    {
      path: '/level',
      name: 'level',
      component: Department,
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterEmployees,
    },
    {
      path: '/designation',
      name: 'designation',
      component: Designations,
    },
    {
      path: '/leaveType',
      name: 'leaveType',
      component: LeaveTypes,
    },
    {
      path: '/employeeList',
      name: 'employeeList',
      component: EmployeeList,
    },
    {
      path: '/addDetails',
      name: 'addDetails',
      component: AddDetails,
    },
    {
      path: '/leaveApplication',
      name: 'leaveApplication',
      component: LeaveApplication

      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      //component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
    },
    {
      path: '/leaveApproval',
      name: 'leaveApproval',
      component: LeaveApprovals

    },
    {
      path: '/applicationHistory',
      name: 'applicationHistory',
      component: ApplicationHistory
    },
    {
      path: '/leaveBalance',
      name: 'leaveBalance',
      component: LeaveBalance
    },
    {
      path: '/allapplications',
      name: 'allapplications',
      component: EmployeesLeaveApplications
    },

    {
      path: '/assinsupervisor',
      name: 'assinsupervisor',
      component: AssignSupervisor
    },
    {
      path: '/employeesupervisor',
      name: 'employeesupervisor',
      component: EmployeeSupervisor
    },
    {
      path: '/staff',
      name: 'staff',
      component: Staff
    },
    {
      path: '/assignedsupervisor',
      name: 'assignedsupervisor',
      component: EmployeesAssignedSupervisors
    },
    {
      path: '/supervisor',
      name: 'supervisor',
      component: Supervisor
    },
    {
      path: '/holidays',
      name: 'holidays',
      component: Holidays
    },
    {
      path: '/initialleavebalance',
      name: 'initialleavebalance',
      component: InitialLeaveBalances
    },
    {
      path: '/employeeview',
      name: 'employeeview',
      component: EmployeeView
    },
    {
      path: '/leavetypebalances',
      name: 'leavetypebalances',
      component: EmployeesLeaveBalance
    },
    {
      path: '/changepassword',
      name: 'changepassword',
      component: ChangePassword
    },
    
  ],
});
