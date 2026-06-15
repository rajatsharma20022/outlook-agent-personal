function triggerGithubIfUnreadExists() {

  // Search unread emails forwarded from Outlook

  const threads = GmailApp.search(
    'is:unread from:YOUR_OUTLOOK_EMAIL'
  );

  if (threads.length === 0) {

    Logger.log("No unread emails");

    return;

  }


  Logger.log(
    threads.length + " unread emails found"
  );


  // GitHub Personal Access Token

  const token =
    "YOUR_GITHUB_PAT";


  // Repository Details

  const owner =
    "YOUR_GITHUB_USERNAME";

  const repo =
    "YOUR_REPOSITORY_NAME";

  const workflow =
    "placement-tracker.yml";


  // Check if workflow is already running

  const runsUrl =
    `https://api.github.com/repos/${owner}/${repo}/actions/runs?status=in_progress`;


  const runsOptions = {

    method: "get",

    headers: {

      Authorization:
        `Bearer ${token}`,

      Accept:
        "application/vnd.github+json"

    }

  };


  const runsResponse =
    UrlFetchApp.fetch(
      runsUrl,
      runsOptions
    );


  const runsData =
    JSON.parse(
      runsResponse.getContentText()
    );


  if (runsData.total_count > 0) {

    Logger.log(
      "Workflow already running"
    );

    return;

  }


  Logger.log(
    "Triggering GitHub workflow..."
  );


  // Trigger workflow

  const dispatchUrl =
    `https://api.github.com/repos/${owner}/${repo}/actions/workflows/${workflow}/dispatches`;


  const payload = {

    ref: "main"

  };


  const dispatchOptions = {

    method: "post",

    headers: {

      Authorization:
        `Bearer ${token}`,

      Accept:
        "application/vnd.github+json"

    },

    contentType:
      "application/json",

    payload:
      JSON.stringify(payload)

  };


  UrlFetchApp.fetch(

    dispatchUrl,

    dispatchOptions

  );


  Logger.log(

    "Workflow triggered successfully"

  );

}