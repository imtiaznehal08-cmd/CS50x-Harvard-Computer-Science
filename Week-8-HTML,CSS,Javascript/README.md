# CS50x - Week 8: HTML, CSS, JavaScript

This repository contains my solutions for the frontend web development projects in **Week 8** of Harvard's CS50x introduction to computer science. This module focused on the foundational technologies of the web: structuring content with HTML5, styling elegant user interfaces using CSS3 and Bootstrap 5, and implementing dynamic user interactivity via client-side JavaScript.

## 📋 Projects Overview

1. **Homepage (Personal Portfolio)**: A responsive, professional multi-page personal website detailing my academic background in Information Technology, cybersecurity technical focus, and running portfolio projects.
2. **Trivia**: An interactive web-based cybersecurity trivia application featuring automated validation for multiple-choice and free-response questions.

---

## 🌐 1. Personal Homepage Portfolio

A beautifully crafted, modern dark-themed web portfolio engineered from scratch using **Bootstrap 5**, custom **CSS3 variables**, and modular **JavaScript**. 

### 📄 Architecture & Cross-Linking
The site is built across 4 fully semantic, cross-linked HTML documents:
* `index.html` — The landing/hero page featuring a large typography design, an overview of target core tracks, and an interactive quote element.
* `about.html` — A deep dive into my professional bio, an interactive accordion expanding skill categories, and a structured milestone roadmap timeline.
* `projects.html` — A functional project grid loaded with dynamic categoric sorting badges.
* `contact.html` — A styled contact hub engineered with frontend validation and feedback response panels.

### ⚡ Technical Implementation Details
* **HTML5 Semantics:** Fully leverages modern layouts utilizing elements like `<nav>`, `<header>`, `<section>`, `<blockquote>`, and `<footer>` for maximum readability and SEO foundation.
* **Custom Fluid Styling:** Built on top of a central component (`styles.css`) using responsive modern primitives like `clamp()` for fluid responsive typography, CSS Custom Variables (`:root`), transition transforms, and layered custom gradients.
* **Client-Side Interactivity (`main.js`):**
    * *Dynamic Time-Based Greeting:* Reads the device system time to display context-aware micro-copy greetings (e.g., *"🌙 Up late studying? Same."* or *"☀️ Good morning!"*) before smoothly resetting to the main subtitle.
    * *Quote Rotator Engine:* Hosts a state-tracked array of industry quotes that gracefully cycle inside the view panel with custom text opacities on call.
    * *Advanced Project Live Filter:* Intercepts custom filter group actions to automatically toggle the target layout wrapper blocks using DOM `data-category` matching metrics.

---

## 🧠 2. Cybersecurity Trivia Application

An educational single-page application built to test users on core network and web application vulnerability concepts. 

### 🛠️ Interactive Engineering
The application uses pure client-side JavaScript to intercept user input and provide real-time visual and text feedback without relying on page reloads or server responses:
* **Part 1: Multiple Choice (Man-in-the-Middle Attack)**
    * Uses a `querySelectorAll` query interface to track element click actions across multiple response buttons.
    * Dynamically mutates element style attributes on event triggers (turning incorrect selections to Crimson Red and correct selections to Green) while rendering active text feedback.
* **Part 2: Free Response (Phishing)**
    * Captures live text entries from input element fields on form submission.
    * Applies standard string sanitization routines (`.trim().toLowerCase()`) to securely evaluate correct answers case-insensitively, automatically adjusting input field alerts based on precision accuracy.

---

## 🛠️ Key Skills Learned

Through completing these projects, I developed a strong foundation in modern frontend engineering and responsive design principles:

* **Semantic HTML5 Architecture:** Learned to write clean, accessible, and structured markup using semantic elements (`<nav>`, `<section>`, `<article>`, `<blockquote>`) rather than relying on unsemantic nested `<div>` structures.
* **Advanced CSS Layouts & Custom Properties:** Mastered responsive layouts by combining standard CSS grids and flexbox models with modular utility design tools. Gained deep familiarity with CSS Variables (`:root`) for maintaining scalable global color and typography states.
* **Responsive Mobile-First Design:** Implemented fluid responsive utility containers using Bootstrap 5 fluid break grids alongside custom `@media` queries to ensure seamless reading viewports across both mobile devices and wide desktops.
* **Asynchronous Client-Side DOM Manipulation:** Developed dynamic user experiences using native JavaScript to listen for DOM events, mutate node styles programmatically, traverse parent-child elements (`parentElement`), and safely alter interior container text layout parameters (`innerHTML`).
* **Data Sanitization & Validation Form Logic:** Implemented input collection architectures that sanitize external string datasets before evaluation via programmatic trim functions (`.trim().toLowerCase()`) to verify case-insensitive string equality.
* **Asynchronous UX Enhancements:** Integrated interactive micro-interactions into user paths—such as implementing timed animations (`setTimeout`), scroll-reveals with intersection observer logic, and context-dependent system hooks like system-time greeting engines.

---

## 🚀 How to View Locally

Since these are pure frontend, client-side applications, they do not require any server-side compilers or runtimes to execute.

1. Clone this repository to your workstation:

   git clone [https://github.com/yourusername/repository-name.git](https://github.com/yourusername/repository-name.git)
   Open the directory and launch any entry point file directly inside your favorite browser:

 2. To see the portfolio and to open trivia game, double-click or open index.html files.

