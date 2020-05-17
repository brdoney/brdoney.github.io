// Functionally the same as {% link assets/db/docs.json %}
const docsJsonUrl = `${document.location.origin}/assets/db/docs.json`;
const placeholder = "Search Pages...";

const autoCompleteEl = document.querySelector("#autoComplete");

new autoComplete({
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
    // Sort rendered results ascendingly
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
    }
  },
});

// Toggle event for search input showing & hidding results list onfocus / blur
const resultsList = document.querySelector("#autoComplete_list");
autoCompleteEl.addEventListener("focus", () => {
  resultsList.style.display = "block";
});
autoCompleteEl.addEventListener("blur", () => {
  resultsList.style.display = "none";
});
