---
description: Enterprise Data Synthesizer. Analyzes internal communication logs and unstructured data to generate structured business reports.
license: MIT
metadata:
  last_deployed: "2026-04-25"
  version: "1.0.0"
  source: "https://wukong.dingtalk.com/"
---

# Wukong Data Synthesizer

This skill is designed to turn massive amounts of unstructured enterprise communication into clear, actionable data insights. It specializes in "reading between the lines" of chat logs and meeting notes.

## MCP runtime requirements

The standard-library-only policy applies to direct `client.py` use. Running `mcp_server.py` requires Python 3.10+ and the official `mcp` SDK (`mcp>=1.0.0,<2`) from `requirements.txt`. Install it into your chosen environment from the repository checkout:

```bash
python -m pip install -r requirements.txt
```

Configure the MCP client with that environment's absolute Python executable path and the absolute path to `mcp_server.py`. The client launches a local STDIO process; a GitHub URL is not a remote MCP endpoint.

## Instructions
1. **Communication Mining:** Parse chat logs and meeting transcripts to extract key decisions, risks, and milestones.
2. **Sentiment & Health Check:** Analyze the tone of project discussions to identify potential team burnout or project delays.
3. **Automated Reporting:** Synthesize internal data into standard business formats (Weekly Status Reports, Post-Mortems, QBRs).
4. **Knowledge Retrieval:** Provide instant answers to "Who said what?" or "Why did we decide X?" based on internal history.

## Examples
- "Analyze the sales data and chat logs from the last month and create a summary report on our biggest challenges."
- "Based on the team's discussions in the 'Backend Dev' channel, what are the current top 3 technical blockers?"
