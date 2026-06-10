// =========================================
// main.js — Nehal Imtiaz Personal Homepage
// CS50x Problem Set 8
// =========================================

// === Cybersecurity & Tech Quote Rotator ===
const quotes = [
  {
    text: "Security is always excessive until it's not enough.",
    author: "Robbie Sinclair"
  },
  {
    text: "The only truly secure system is one that is powered off, cast in a block of concrete, and sealed in a lead-lined room with armed guards.",
    author: "Gene Spafford"
  },
  {
    text: "Cybersecurity is much more than a matter of IT.",
    author: "Stephane Nappo"
  },
  {
    text: "Privacy is not something that I'm merely entitled to, it's an absolute prerequisite.",
    author: "Marlon Brando"
  },
  {
    text: "Anyone who has never made a mistake has never tried anything new.",
    author: "Albert Einstein"
  },
  {
    text: "The more you know, the more you realize you don't know.",
    author: "Aristotle"
  },
  {
    text: "In the middle of every difficulty lies opportunity.",
    author: "Albert Einstein"
  }
];

let currentQuoteIndex = 0;

function newQuote() {
  currentQuoteIndex = (currentQuoteIndex + 1) % quotes.length;
  const quoteEl = document.getElementById("quote-text");
  const authorEl = document.querySelector(".quote-author");

  if (quoteEl) {
    quoteEl.style.transition = "opacity 0.3s ease";
    quoteEl.style.opacity = "0";
    setTimeout(() => {
      quoteEl.textContent = `"${quotes[currentQuoteIndex].text}"`;
      if (authorEl) authorEl.textContent = `— ${quotes[currentQuoteIndex].author}`;
      quoteEl.style.opacity = "1";
    }, 300);
  }
}

// === Contact Form Validation & Simulated Submission ===
function submitForm() {
  const name    = document.getElementById("name");
  const email   = document.getElementById("email");
  const subject = document.getElementById("subject");
  const message = document.getElementById("message");

  if (!name || !email || !subject || !message) return;

  if (!name.value.trim()) {
    shakeField(name); name.focus(); return;
  }
  if (!email.value.trim() || !email.value.includes("@")) {
    shakeField(email); email.focus(); return;
  }
  if (!subject.value) {
    shakeField(subject); subject.focus(); return;
  }
  if (!message.value.trim()) {
    shakeField(message); message.focus(); return;
  }

  const form = document.getElementById("contact-form");
  const success = document.getElementById("form-success");
  if (form && success) {
    form.style.transition = "opacity 0.4s ease";
    form.style.opacity = "0";
    setTimeout(() => {
      form.style.display = "none";
      success.style.display = "block";
    }, 400);
  }
}

function shakeField(el) {
  el.style.borderColor = "#e05a5a";
  el.style.animation = "shake 0.3s ease";
  setTimeout(() => {
    el.style.borderColor = "";
    el.style.animation = "";
  }, 600);
}

// === Project Filter ===
function filterProjects(category, btn) {
  document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
  if (btn) btn.classList.add("active");

  const cards = document.querySelectorAll(".project-card-wrap");
  let visible = 0;

  cards.forEach(card => {
    if (category === "all" || card.dataset.category === category) {
      card.style.display = "block";
      visible++;
    } else {
      card.style.display = "none";
    }
  });

  const noResults = document.getElementById("no-results");
  if (noResults) noResults.style.display = visible === 0 ? "block" : "none";
}

// === Scroll-triggered fade-in ===
function revealOnScroll() {
  const elements = document.querySelectorAll(".intro-card, .project-card, .timeline-item");
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        entry.target.style.animationDelay = `${i * 0.08}s`;
        entry.target.classList.add("fade-in-up");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  elements.forEach(el => observer.observe(el));
}

// === Navbar scroll highlight ===
function handleNavScroll() {
  const nav = document.querySelector(".site-nav");
  if (!nav) return;
  window.addEventListener("scroll", () => {
    nav.style.borderBottomColor = window.scrollY > 50
      ? "rgba(200, 169, 110, 0.2)"
      : "";
  });
}

// === Time-based greeting in hero ===
function setTimeGreeting() {
  const tagline = document.getElementById("hero-tagline");
  if (!tagline) return;

  const hour = new Date().getHours();
  let greeting = "";
  if (hour < 5)       greeting = "🌙 Up late studying? Same.";
  else if (hour < 12) greeting = "☀️ Good morning! Ready to learn something new.";
  else if (hour < 17) greeting = "🌤️ Good afternoon! Welcome to my corner of the web.";
  else if (hour < 21) greeting = "🌆 Good evening! Thanks for stopping by.";
  else                greeting = "🌙 Late night deep dive? You're in the right place.";

  const original = tagline.textContent;
  tagline.textContent = greeting;
  tagline.style.color = "var(--accent)";

  setTimeout(() => {
    tagline.style.transition = "opacity 0.5s ease";
    tagline.style.opacity = "0";
    setTimeout(() => {
      tagline.textContent = original;
      tagline.style.color = "";
      tagline.style.opacity = "1";
    }, 500);
  }, 2800);
}

// Shake keyframe
const style = document.createElement("style");
style.textContent = `
  @keyframes shake {
    0%   { transform: translateX(0); }
    25%  { transform: translateX(-6px); }
    50%  { transform: translateX(6px); }
    75%  { transform: translateX(-4px); }
    100% { transform: translateX(0); }
  }
`;
document.head.appendChild(style);

// === Init ===
document.addEventListener("DOMContentLoaded", () => {
  revealOnScroll();
  handleNavScroll();
  setTimeGreeting();
});
