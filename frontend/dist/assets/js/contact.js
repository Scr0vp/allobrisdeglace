/* ALLO BRIS DE GLACE — formulaire de contact
   Validation côté client (français) + envoi à l'API /api/contact. */
(function () {
  "use strict";

  var form = document.getElementById("contact-form");
  if (!form) return;

  var EMAIL_RE = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
  var PHONE_RE = /^\+?[0-9][0-9 .\-()]{7,18}$/;

  var MSG_REQUIRED = "Ce champ est obligatoire.";
  var MSG_EMAIL = "Veuillez saisir une adresse e-mail valide.";
  var MSG_PHONE = "Veuillez saisir un numéro de téléphone valide.";
  var MSG_INVALID = "Veuillez vérifier les informations saisies.";
  var MSG_ERROR = "Une erreur est survenue. Veuillez réessayer ou nous appeler directement.";

  var status = form.querySelector("[data-testid='form-status']");
  var submitBtn = form.querySelector("[data-testid='form-submit-button']");
  var submitLabel = submitBtn.querySelector("span").textContent;
  var successBox = document.querySelector("[data-testid='form-success-message']");

  form.elements.page_source.value = window.location.href;

  function setError(name, message) {
    var slot = form.querySelector('[data-error-for="' + name + '"]');
    var field = form.elements[name];
    if (slot) slot.textContent = message || "";
    if (field && field.setAttribute) {
      field.setAttribute("aria-invalid", message ? "true" : "false");
    }
  }

  function clearErrors() {
    ["nom", "prenom", "telephone", "email", "region", "type_vehicule",
     "immatriculation", "service", "message", "consentement_rgpd"
    ].forEach(function (name) { setError(name, ""); });
    status.textContent = "";
    status.className = "form-status";
  }

  function collect() {
    return {
      nom: form.elements.nom.value.trim(),
      prenom: form.elements.prenom.value.trim(),
      telephone: form.elements.telephone.value.trim(),
      email: form.elements.email.value.trim(),
      region: form.elements.region.value,
      type_vehicule: form.elements.type_vehicule.value.trim(),
      immatriculation: form.elements.immatriculation.value.trim(),
      service: form.elements.service.value,
      message: form.elements.message.value.trim(),
      consentement_rgpd: form.elements.consentement_rgpd.checked,
      page_source: form.elements.page_source.value,
      entreprise: form.elements.entreprise.value
    };
  }

  function validate(values) {
    var errors = {};
    if (!values.nom) errors.nom = MSG_REQUIRED;
    if (!values.prenom) errors.prenom = MSG_REQUIRED;
    if (!values.telephone) errors.telephone = MSG_REQUIRED;
    else if (!PHONE_RE.test(values.telephone)) errors.telephone = MSG_PHONE;
    if (!values.email) errors.email = MSG_REQUIRED;
    else if (!EMAIL_RE.test(values.email)) errors.email = MSG_EMAIL;
    if (!values.region) errors.region = MSG_REQUIRED;
    if (!values.type_vehicule) errors.type_vehicule = MSG_REQUIRED;
    if (!values.service) errors.service = MSG_REQUIRED;
    if (!values.message) errors.message = MSG_REQUIRED;
    if (!values.consentement_rgpd) errors.consentement_rgpd = MSG_REQUIRED;
    return errors;
  }

  function showErrors(errors, fallbackMessage) {
    var first = null;
    Object.keys(errors).forEach(function (name) {
      setError(name, errors[name]);
      if (!first && form.elements[name]) first = form.elements[name];
    });
    status.textContent = fallbackMessage || MSG_INVALID;
    status.classList.add("is-error");
    if (first && first.focus) first.focus();
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    clearErrors();

    var values = collect();
    var errors = validate(values);
    if (Object.keys(errors).length > 0) {
      showErrors(errors);
      return;
    }

    submitBtn.disabled = true;
    submitBtn.querySelector("span").textContent = "Envoi en cours…";

    fetch("/api/contact", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(values)
    })
      .then(function (res) {
        return res.json().catch(function () { return {}; }).then(function (data) {
          return { status: res.status, data: data };
        });
      })
      .then(function (result) {
        if (result.status === 200 && result.data.ok) {
          form.hidden = true;
          if (successBox) {
            successBox.hidden = false;
            successBox.setAttribute("tabindex", "-1");
            successBox.focus();
            successBox.scrollIntoView({ behavior: "smooth", block: "center" });
          }
          if (typeof window.abdgTrackConversion === "function") {
            window.abdgTrackConversion();
          }
          return;
        }
        if (result.data && result.data.errors) {
          showErrors(result.data.errors, result.data.message);
        } else {
          status.textContent = (result.data && result.data.message) || MSG_ERROR;
          status.classList.add("is-error");
        }
      })
      .catch(function () {
        status.textContent = MSG_ERROR;
        status.classList.add("is-error");
      })
      .finally(function () {
        submitBtn.disabled = false;
        submitBtn.querySelector("span").textContent = submitLabel;
      });
  });
})();
