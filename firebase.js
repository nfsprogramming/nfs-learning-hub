// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-firestore.js";

// Your web app's Firebase configuration
const firebaseConfig = {
  // Use a placeholder that Vercel's build command will replace with the environment variable.
  // Vercel Build Command: sed -i "s/ENV_FIREBASE_API_KEY/$FIREBASE_API_KEY/g" firebase.js
  apiKey: "ENV_FIREBASE_API_KEY",
  authDomain: "nfs-learning-hub-2c5a7.firebaseapp.com",
  projectId: "nfs-learning-hub-2c5a7",
  storageBucket: "nfs-learning-hub-2c5a7.firebasestorage.app",
  messagingSenderId: "1005875192289",
  appId: "1:1005875192289:web:9ec933f2f1ba8d605a72a0"
};

// TODO: If you are NOT using a build step, you must put the real key above.
// If you ARE using Vercel, set the FIREBASE_API_KEY environment variable and 
// use this build command: sed -i "s/ENV_FIREBASE_API_KEY/$FIREBASE_API_KEY/g" firebase.js

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

export { auth, db };
