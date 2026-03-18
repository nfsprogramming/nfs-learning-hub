// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-firestore.js";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAys70Ze82_0MI7jFRkxoRqyXwsbcUbS6Q",
  authDomain: "nfs-learning-hub-2c5a7.firebaseapp.com",
  projectId: "nfs-learning-hub-2c5a7",
  storageBucket: "nfs-learning-hub-2c5a7.firebasestorage.app",
  messagingSenderId: "1005875192289",
  appId: "1:1005875192289:web:9ec933f2f1ba8d605a72a0"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

export { auth, db };
