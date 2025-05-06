<script setup>
import { ref } from 'vue';
import Login from './components/Login.vue'
import TicketForm from './components/TicketForm.vue'
import AccountMenu from './components/accountmenu.vue'
import ticketTable from './components/ticketTable.vue';
   
 
</script>



<template>
    <div id="app">
      <AccountMenu />
      <Login />
      <TicketForm />
      <ticketTable />
      <router-view />
    </div>
  </template>
  