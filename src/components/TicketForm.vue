<template>
  <div class="ticket-form-page">
    <div class="ticket-form-container">
      <h2>Submit a Support Ticket</h2>
      <form @submit.prevent="submitTicket">
        <label>Subject</label>
        <input v-model="subject" type="text" required placeholder="Issue subject" />

        <label>Category</label>
        <select v-model="category" required>
          <option disabled value="">Select a category</option>
          <option>Technical</option>
          <option>Billing</option>
          <option>Account</option>
          <option>Other</option>
        </select>

        <label>Priority</label>
        <select v-model="priority" required>
          <option disabled value="">Select priority</option>
          <option>Low</option>
          <option>Medium</option>
          <option>High</option>
          <option>Urgent</option>
        </select>

        <label>Description</label>
        <textarea
          v-model="description"
          rows="5"
          required
          placeholder="Describe your issue in detail"
        ></textarea>

        <button type="submit">Submit Ticket</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TicketForm',
  data() {
    return {
      subject: '',
      category: '',
      priority: '',
      description: ''
    };
  },
  methods: {
    async submitTicket() {
      try {
        const response = await fetch("http://127.0.0.1:5000/submit_ticket", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          credentials: "include",
          body: JSON.stringify({
            email: this.userEmail,  
            subject: this.subject,
            category: this.category,
            priority: this.priority,
            description: this.description,
          }),
        });

        const result = await response.json();
        console.log(result);
      } catch (err) {
        console.error("Error submitting ticket:", err);
      }
    }
  }
};
</script>


<style scoped>
.ticket-form-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(to right, #667eea, #764ba2);
  padding: 20px;
}

.ticket-form-container {
  background-color: #fff;
  padding: 40px;
  border-radius: 16px;
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 500px;
  text-align: center;
}

h2 {
  margin-bottom: 20px;
  font-size: 24px;
  color: #333;
}

form {
  display: flex;
  flex-direction: column;
  text-align: left;
}

label {
  margin-top: 15px;
  font-weight: bold;
  color: #444;
}

input,
select,
textarea {
  margin-top: 6px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
  width: 100%;
  box-sizing: border-box;
}

textarea {
  resize: vertical;
}

button {
  margin-top: 20px;
  background-color: #667eea;
  color: white;
  border: none;
  padding: 12px;
  font-size: 16px;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.3s ease;
}

button:hover {
  background-color: #5563d1;
}
</style>
