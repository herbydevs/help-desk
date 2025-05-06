<template>
    <div class="admin-tickets">
      <h2 class="page-title">Admin - Manage Tickets</h2>
      
      <!-- Filter controls -->
      <div class="filter-controls">
        <select v-model="statusFilter" class="filter-select">
          <option value="all">All Tickets</option>
          <option value="open">Open</option>
          <option value="resolved">Resolved</option>
        </select>
      </div>
  
      <!-- Ticket list -->
      <div class="ticket-list">
        <div v-for="ticket in filteredTickets" :key="ticket.id" class="ticket-card">
          <div class="ticket-header">
            <span class="ticket-id">Ticket #{{ ticket.id }}</span>
            <span :class="{'status-open': ticket.status === 'open', 'status-resolved': ticket.status === 'resolved'}">
              {{ ticket.status.charAt(0).toUpperCase() + ticket.status.slice(1) }}
            </span>
          </div>
          <div class="ticket-body">
            <p><strong>Subject:</strong> {{ ticket.subject }}</p>
            <p><strong>Description:</strong> {{ ticket.description }}</p>
            <button v-if="ticket.status === 'open'" @click="markResolved(ticket.id)" class="mark-resolved-btn">
              Mark as Resolved
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  
  // Mock ticket data (replace with an API call if needed)
  const tickets = ref([
    { id: 1, subject: 'Issue with login', description: 'User unable to log in', status: 'open' },
    { id: 2, subject: 'Broken link on homepage', description: 'A 404 error on the homepage', status: 'resolved' },
    { id: 3, subject: 'Payment error', description: 'Issues during payment process', status: 'open' },
    { id: 4, subject: 'Slow site speed', description: 'The website is very slow to load', status: 'resolved' },
  ]);
  
  const statusFilter = ref('all');
  
  // Filter tickets based on the selected status
  const filteredTickets = computed(() => {
    if (statusFilter.value === 'all') {
      return tickets.value;
    }
    return tickets.value.filter(ticket => ticket.status === statusFilter.value);
  });
  
  // Mark a ticket as resolved
  function markResolved(ticketId) {
    const ticket = tickets.value.find(t => t.id === ticketId);
    if (ticket) {
      ticket.status = 'resolved';
    }
  }
  </script>
  
  <style scoped>
  .admin-tickets {
    padding: 20px;
    font-family: Arial, sans-serif;
  }
  
  .page-title {
    font-size: 2rem;
    margin-bottom: 20px;
  }
  
  .filter-controls {
    margin-bottom: 20px;
  }
  
  .filter-select {
    padding: 8px 16px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
    cursor: pointer;
  }
  
  .ticket-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  
  .ticket-card {
    background-color: #fff;
    border: 1px solid #ddd;
    padding: 16px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .ticket-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 12px;
    font-weight: bold;
  }
  
  .status-open {
    color: red;
  }
  
  .status-resolved {
    color: green;
  }
  
  .ticket-body {
    margin-bottom: 12px;
  }
  
  .mark-resolved-btn {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    font-size: 14px;
    cursor: pointer;
    border-radius: 4px;
  }
  
  .mark-resolved-btn:hover {
    background-color: #45a049;
  }
  </style>
  