// Functionally the same as {% link assets/db/docs.json %}
const docsJsonUrl = `${document.location.origin}/assets/db/docs.json`;
const placeholder = "Search Pages...";

const autoCompleteEl = document.querySelector("#autoComplete");

const ac = new autoComplete({
  data: {
    src: async () => {
      autoCompleteEl.setAttribute("placeholder", "Loading...");

      const source = await fetch(docsJsonUrl);
      const data = await source.json();

      autoCompleteEl.setAttribute("placeholder", placeholder);

      return data;
    },
    key: ["title"],
    cache: true,
  },
  sort: (a, b) => {
    // Sort rendered results in ascending order
    if (a.match < b.match) return -1;
    if (a.match > b.match) return 1;
    return 0;
  },
  placeHolder: placeholder,
  selector: "#autoComplete",
  threshold: 0, // Min. Chars length to start Engine
  debounce: 0, // Post duration for engine to start
  searchEngine: "loose", // Search Engine type/mode
  resultsList: {
    // Rendered results list object
    render: true,
    container: (source) => {
      source.setAttribute("id", "autoComplete_list");
    },
    destination: autoCompleteEl,
    position: "afterend",
    element: "ul",
  },
  maxResults: 5, // Max. number of rendered results
  highlight: true, // Highlight matching results
  resultItem: {
    // Rendered result item
    content: (data, source) => {
      source.innerHTML = `${data.match}<span class="autoComplete_result_chevron">&rsaquo;</span>`;
    },
    element: "li",
  },
  noResults: () => {
    const result = document.createElement("li");
    result.setAttribute("class", "no_result");
    result.setAttribute("tabindex", "1");
    result.innerHTML = "No Results";
    document.querySelector("#autoComplete_list").appendChild(result);
  },
  onSelection: (feedback) => {
    // Runs when autocomplete selection is selected
    if (feedback.selection != null) {
      const selectionData = feedback.selection.value;
      window.location.href = selectionData.url;
      autoCompleteEl.value = "";
    }
  },
});

// Choose the first result on enter, if there is one
autoCompleteEl.addEventListener("keydown", async (event) => {
  if (event.key === "Enter") {
    // Make sure that results have been displayed, if there are any
    await ac.listMatchedResults(ac.dataStream);

    // Click on (select) the top result, if there is one
    const resultsChildren = ac.resultsList.view.children;
    if (resultsChildren.length > 0) {
      const f = ac.resultsList.view.children[0];
      const ev = new Event("mousedown");
      f.dispatchEvent(ev);
    }
  } else if (event.key === "Escape") {
    autoCompleteEl.blur();
  }
});

// Toggle event for search input showing & hiding results list onfocus / blur
const resultsList = document.querySelector("#autoComplete_list");
autoCompleteEl.addEventListener("focus", () => {
  resultsList.style.display = "block";
});
autoCompleteEl.addEventListener("blur", () => {
  resultsList.style.display = "none";
});

window.onload = () => {
  var config = {
    // Font sizes currently don't work for Flowchart diagrams
    actorFontSize: 16,
    noteFontSize: 16,
    messageFontSize: 18,
    theme: "neutral",
  };
  mermaid.initialize(config);
  window.mermaid.init(
    undefined,
    document.querySelectorAll(".language-mermaid")
  );
};
