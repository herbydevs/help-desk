<template>
  <div class="login-page">
    <div class="login-container">
      <h2>Welcome Back</h2>
      <p>Please log in to your account to continue.</p>

      <form @submit.prevent="login">
        <label>Email</label>
        <input v-model="email" type="email" required placeholder="Enter your email" />

        <label>Password</label>
        <input v-model="password" type="password" required placeholder="Enter your password" />

        <button type="submit">Log In</button>
      </form>

      <p class="signup-text">
        Don't have an account?
        <a href="#">Sign up</a>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    async login() {
      try {
        const response = await fetch('http://127.0.0.1:5000/auth/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          credentials: 'include',  // This allows cookies or credentials to be sent
          body: JSON.stringify({
            email: this.email,
            password: this.password,
          }),
        });

        // Check the raw response for debugging purposes
        const data = await response.json();
        console.log('Response from backend:', data);

        if (response.ok && data.role) {
          alert('Login successful!');
          this.$emit('login', { role: data.role }); // ✅ emit role in a user-like object
        } else {
          console.error('Login failed:', data);
          alert(data.error || 'Login failed.');
        }
      } catch (error) {
        console.error(error);
        alert('Something went wrong.');
      }
    }
  },
};
</script>






<style scoped>
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(to right, #4facfe, #00f2fe);
  padding: 20px;
}

.login-container {
  background-color: white;
  padding: 40px;
  border-radius: 16px;
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
  text-align: center;
}

h2 {
  margin-bottom: 10px;
  font-size: 28px;
  color: #333;
}

p {
  margin-bottom: 20px;
  color: #777;
  font-size: 14px;
}

label {
  display: block;
  text-align: left;
  margin: 12px 0 6px;
  font-weight: bold;
  color: #444;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
  box-sizing: border-box;
}

button {
  margin-top: 20px;
  width: 100%;
  background-color: #4facfe;
  color: white;
  border: none;
  padding: 12px;
  font-size: 16px;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.3s ease;
}

button:hover {
  background-color: #3c9df3;
}

.signup-text {
  margin-top: 20px;
  font-size: 14px;
  color: #666;
}

.signup-text a {
  color: #4facfe;
  text-decoration: none;
  font-weight: bold;
}

.signup-text a:hover {
  text-decoration: underline;
}
</style>
