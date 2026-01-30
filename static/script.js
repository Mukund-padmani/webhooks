async function fetchEvents() {
    const res = await fetch("/events");
    const data = await res.json();
  
    const list = document.getElementById("events");
    list.innerHTML = "";
  
    data.forEach(e => {
      let text = "";
  
      if (e.event_type === "push") {
        text = `${e.author} pushed to ${e.to_branch} on ${new Date(e.timestamp).toUTCString()}`;
      }
      if (e.event_type === "pull_request") {
        text = `${e.author} submitted a pull request from ${e.from_branch} to ${e.to_branch} on ${new Date(e.timestamp).toUTCString()}`;
      }
      if (e.event_type === "merge") {
        text = `${e.author} merged branch ${e.from_branch} to ${e.to_branch} on ${new Date(e.timestamp).toUTCString()}`;
      }
  
      const li = document.createElement("li");
      li.innerText = text;
      list.appendChild(li);
    });
  }
  
  fetchEvents();
  setInterval(fetchEvents, 15000);
  