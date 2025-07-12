const translations = {
  uk: {
    title: "Велике починається з малого (BBS)",
    slogan: "Все велике починається з малого.<br/>Одне слово. Один крок. Одна дія. Один світ, що змінюється.",
    navVision: "Бачення",
    navProjects: "Проєкти",
    navJoin: "Долучитись",
    navSupport: "Підтримати",
    navNews: "Новини",
    navFAQ: "Питання",
    navContact: "Контакти",
    navPanel: "Панель",
    joinText: "Чи ти мрійник, розробник, вчитель або просто небайдужий — ти нам потрібен. Незалежно ким ти є і ким себе відчуваєш — тут ми без масок, ярликів чи визначень. Ти нам потрібний як особистість. Як цілісність людяності."
  }
};

function setLang(lang) {
  if (lang === "uk") {
    const t = translations.uk;
    for (let key in t) {
      const el = document.getElementById(key);
      if (el) el.innerHTML = t[key];
    }
  } else {
    location.reload(); // англійська — оригінал
  }
}
