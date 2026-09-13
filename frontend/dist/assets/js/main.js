/* ALLO BRIS DE GLACE — interactions principales
   Défilement fluide (Lenis), révélations au scroll, parallaxe du hero,
   consentement cookies et suivi Google (Ads / Analytics) après accord. */
(function () {
  "use strict";

  var prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ------------------------------------------------ défilement fluide */
  if (!prefersReduced && typeof window.Lenis === "function") {
    try {
      var lenis = new window.Lenis({ lerp: 0.12, smoothWheel: true });
      var raf = function (time) {
        lenis.raf(time);
        requestAnimationFrame(raf);
      };
      requestAnimationFrame(raf);
    } catch (err) { /* Lenis indisponible : défilement natif */ }
  }

  /* ------------------------------------------------- ombre de l'en-tête */
  var siteHeader = document.querySelector(".site-header");
  var onScrollHeader = function () {
    if (siteHeader) siteHeader.classList.toggle("is-scrolled", window.scrollY > 8);
  };
  window.addEventListener("scroll", onScrollHeader, { passive: true });
  onScrollHeader();

  /* ------------------------------------------- menu mobile (hamburger) */
  var menuToggle = document.querySelector('[data-testid="mobile-menu-toggle"]');
  var mobileMenu = document.getElementById("mobile-menu");

  function closeMobileMenu() {
    if (!menuToggle || !mobileMenu || mobileMenu.hidden) return;
    mobileMenu.hidden = true;
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-label", "Ouvrir le menu");
  }

  function openMobileMenu() {
    if (!menuToggle || !mobileMenu) return;
    mobileMenu.hidden = false;
    menuToggle.setAttribute("aria-expanded", "true");
    menuToggle.setAttribute("aria-label", "Fermer le menu");
  }

  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener("click", function (event) {
      event.stopPropagation();
      if (mobileMenu.hidden) { openMobileMenu(); } else { closeMobileMenu(); }
    });
    mobileMenu.addEventListener("click", function (event) {
      if (event.target.closest("a")) closeMobileMenu();
    });
    document.addEventListener("click", function (event) {
      if (!event.target.closest(".site-header")) closeMobileMenu();
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") closeMobileMenu();
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth > 768) closeMobileMenu();
    });
  }

  /* --------------------------------------------- révélations au scroll */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !prefersReduced) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* ------------------------------------------ parallaxe du visuel hero */
  var media = document.querySelector("[data-parallax] img");
  if (media && !prefersReduced) {
    var ticking = false;
    window.addEventListener("scroll", function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        var rect = media.getBoundingClientRect();
        if (rect.bottom > 0 && rect.top < window.innerHeight) {
          media.style.setProperty("--parallax", (rect.top * -0.05).toFixed(1) + "px");
        }
        ticking = false;
      });
    }, { passive: true });
  }

  /* -------------------------------- consentement & suivi Google (opt-in) */
  var CONSENT_KEY = "abdg-consent";
  var banner = document.querySelector(".cookie-banner");
  var trackingConfig = null;

  function injectGtag(id) {
    if (!id || document.getElementById("gtag-script")) return;
    var script = document.createElement("script");
    script.id = "gtag-script";
    script.async = true;
    script.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(id);
    document.head.appendChild(script);
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    if (trackingConfig.google_analytics_id) {
      window.gtag("config", trackingConfig.google_analytics_id);
    }
    if (trackingConfig.google_ads_conversion_id) {
      window.gtag("config", trackingConfig.google_ads_conversion_id);
    }
  }

  function enableTracking() {
    fetch("/api/config").then(function (res) { return res.json(); }).then(function (cfg) {
      trackingConfig = cfg;
      injectGtag(cfg.google_analytics_id || cfg.google_ads_conversion_id);
    }).catch(function () { /* suivi indisponible : le site reste fonctionnel */ });
  }

  window.abdgTrackConversion = function () {
    if (window.gtag && trackingConfig &&
        trackingConfig.google_ads_conversion_id &&
        trackingConfig.google_ads_conversion_label) {
      window.gtag("event", "conversion", {
        send_to: trackingConfig.google_ads_conversion_id + "/" + trackingConfig.google_ads_conversion_label
      });
    }
  };

  var storedConsent = null;
  try { storedConsent = localStorage.getItem(CONSENT_KEY); } catch (err) {}
  if (storedConsent === "accept") {
    enableTracking();
  } else if (!storedConsent && banner) {
    banner.hidden = false;
  }

  if (banner) {
    banner.addEventListener("click", function (event) {
      var btn = event.target.closest("[data-consent]");
      if (!btn) return;
      var choice = btn.getAttribute("data-consent");
      try { localStorage.setItem(CONSENT_KEY, choice); } catch (err) {}
      banner.hidden = true;
      if (choice === "accept") enableTracking();
    });
  }

  /* ----------------------------- suivi des clics (appel, WhatsApp, devis) */
  var TRACK_EVENTS = {
    call: "click_to_call",
    whatsapp: "whatsapp_click",
    quote: "quote_click"
  };
  document.addEventListener("click", function (event) {
    var link = event.target.closest("a[data-track]");
    if (!link || !window.gtag) return;
    window.gtag("event", TRACK_EVENTS[link.getAttribute("data-track")] || "interaction", {
      page_path: window.location.pathname
    });
  });
})();
