# Issue Templates Documentation
> **Purpose:** Comprehensive issue template collection following 2025 best practices for community management, bug reporting, and feature requests. These templates streamline issue reporting and ensure contributors provide all necessary information upfront.

**Document Type:** Community Management Templates  
**Version:** 2.0 - Enhanced with 2025 Best Practices  
**Last Updated:** 2025-01-15  
**Template Status:** Production Ready

---

## Document Control
| Field | Value |
|-------|-------|
| **Project Name** | [PROJECT_NAME] |
| **Community Manager** | [COMMUNITY_MANAGER_NAME] |
| **Issue Workflow** | [WORKFLOW_TYPE] |
| **Last Updated** | [YYYY-MM-DD] |
| **Template Review** | [YYYY-MM-DD] |
| **Automation Status** | [MANUAL / AUTOMATED / HYBRID] |

---

## 📋 Table of Contents
- [🎯 Issue Template Overview](#-issue-template-overview)
- [🐛 Bug Report Template](#-bug-report-template)
- [✨ Feature Request Template](#-feature-request-template)
- [📚 Documentation Template](#-documentation-template)
- [🔒 Security Vulnerability Template](#-security-vulnerability-template)
- [❓ General Support Template](#-general-support-template)
- [🛠️ Configuration & Setup](#️-configuration--setup)
- [📊 Community Guidelines](#-community-guidelines)

---

## 🎯 Issue Template Overview

### Purpose & Philosophy
Our issue templates are designed to create a structured, efficient, and welcoming environment for community contributions. Following 2025 best practices, these templates balance comprehensive information gathering with user-friendly experiences, ensuring both contributors and maintainers can collaborate effectively.

### Template Strategy
- **Guided Experience:** Clear categories help users choose the right template
- **Comprehensive Information:** Structured fields ensure all necessary details are captured
- **User-Friendly:** Simple language and clear instructions reduce barriers to contribution
- **Automated Processing:** Templates support automated labeling and routing
- **Community Building:** Encouraging tone that welcomes all types of contributions

### Available Templates
1. **🐛 Bug Report** - For reporting software defects and issues
2. **✨ Feature Request** - For proposing new features and enhancements
3. **📚 Documentation** - For documentation improvements and additions
4. **🔒 Security Vulnerability** - For responsible disclosure of security issues
5. **❓ General Support** - For questions and general inquiries

---

## 🐛 Bug Report Template

### Template Configuration
```yaml
---
name: "🐛 Bug Report"
about: "Report a bug to help us improve the project"
title: "[BUG]: "
labels: ["type: bug", "status: needs-triage"]
assignees: ''
---
```

### Template Content

```markdown
## 🔍 Pre-submission Checklist

Thank you for taking the time to report a bug! Please complete this checklist before submitting:

- [ ] I have searched existing issues to ensure this bug hasn't been reported
- [ ] I have provided the minimal steps to reproduce the issue
- [ ] I have included all relevant environment information
- [ ] I have checked the documentation and FAQ for solutions

---

## 🐛 Bug Description

**Clear and concise description of the bug:**
<!-- Describe what the bug is in simple terms -->

**Impact on users:**
<!-- How does this bug affect the user experience? -->

---

## 🔄 Steps to Reproduce

**Minimal reproduction steps:**
1. [STEP_1_DESCRIPTION]
2. [STEP_2_DESCRIPTION]
3. [STEP_3_DESCRIPTION]
4. [EXPECTED_RESULT_OR_ERROR]

**Expected behavior:**
<!-- What should happen instead? -->

**Actual behavior:**
<!-- What actually happens? -->

---

## 📱 Environment Information

**System Details:**
- **Operating System:** [OS_NAME_AND_VERSION]
- **Browser:** [BROWSER_NAME_AND_VERSION]
- **Application Version:** [APPLICATION_VERSION]
- **Device Type:** [DEVICE_TYPE]

**Additional Context:**
- **Screen Resolution:** [SCREEN_RESOLUTION_IF_APPLICABLE]
- **Network Connection:** [NETWORK_TYPE_IF_APPLICABLE]
- **User Role/Permissions:** [USER_PERMISSIONS_IF_APPLICABLE]

---

## 📸 Visual Evidence

**Screenshots/Videos:**
<!-- Drag and drop images or videos here -->

**Console Logs:**
```
<!-- Paste any relevant console errors or logs here -->
```

**Network Requests:**
```
<!-- Include relevant network request/response data if applicable -->
```

---

## 🔧 Additional Information

**Workarounds:**
<!-- Any temporary solutions you've found -->

**Related Issues:**
<!-- Link to any related issues using #issue_number -->

**Frequency:**
- [ ] Always occurs
- [ ] Occurs sometimes
- [ ] Occurred once
- [ ] Occurs under specific conditions

**Priority Assessment:**
- [ ] Critical - Blocks core functionality
- [ ] High - Significantly impacts user experience
- [ ] Medium - Noticeable but has workarounds
- [ ] Low - Minor inconvenience

---

## 🤝 Contribution

**Would you like to work on fixing this bug?**
- [ ] Yes, I'd like to submit a pull request
- [ ] Yes, but I need guidance
- [ ] No, but I'm available for testing
- [ ] No, just reporting

---

*Thank you for helping improve our project! We'll review this issue and respond as soon as possible.*
```

---

## ✨ Feature Request Template

### Template Configuration
```yaml
---
name: "✨ Feature Request"
about: "Suggest a new feature or enhancement"
title: "[FEATURE]: "
labels: ["type: enhancement", "status: needs-triage"]
assignees: ''
---
```

### Template Content

```markdown
## 🔍 Pre-submission Checklist

- [ ] I have searched existing issues and feature requests
- [ ] I have checked the project roadmap for similar features
- [ ] I have considered if this could be implemented as a plugin/extension
- [ ] I understand this is a feature request, not a bug report

---

## ✨ Feature Summary

**Feature Name:**
<!-- Short, descriptive name for the feature -->

**One-line Description:**
<!-- Summarize the feature in one sentence -->

---

## 🎯 Problem Statement

**What problem does this feature solve?**
<!-- Describe the user problem or need this feature addresses -->

**Who would benefit from this feature?**
- [ ] End users
- [ ] Developers
- [ ] Administrators
- [ ] All users
- [ ] Specific user group: [describe]

**How are users currently handling this need?**
<!-- Describe current workarounds or alternative solutions -->

---

## 💡 Proposed Solution

**Detailed Description:**
<!-- Provide a detailed description of how the feature should work -->

**User Interface Mockups:**
<!-- Include wireframes, mockups, or sketches if applicable -->

**User Stories:**
<!-- Write user stories in the format: "As a [user type], I want [goal] so that [benefit]" -->
- As a [USER_TYPE_1], I want [USER_GOAL_1] so that [USER_BENEFIT_1]
- As a [USER_TYPE_2], I want [USER_GOAL_2] so that [USER_BENEFIT_2]

---

## 🔧 Technical Considerations

**Implementation Approach:**
<!-- If you have technical suggestions, describe them here -->

**Potential Challenges:**
<!-- What technical or design challenges might this feature face? -->

**Dependencies:**
<!-- Are there any dependencies on other features or systems? -->

**Breaking Changes:**
- [ ] This feature would require breaking changes
- [ ] This feature is backward compatible
- [ ] Unsure about compatibility impact

---

## 📊 Success Metrics

**How would we measure success?**
<!-- What metrics would indicate this feature is successful? -->

**Acceptance Criteria:**
<!-- Define what "done" looks like for this feature -->
- [ ] [ACCEPTANCE_CRITERION_1]
- [ ] [ACCEPTANCE_CRITERION_2]
- [ ] [ACCEPTANCE_CRITERION_3]

---

## 🌟 Additional Context

**Similar Features in Other Tools:**
<!-- Reference similar features in other applications -->

**Priority Level:**
- [ ] Critical - Core functionality gap
- [ ] High - Significantly improves user experience
- [ ] Medium - Nice to have enhancement
- [ ] Low - Minor improvement

**Timeline Expectations:**
- [ ] Needed urgently
- [ ] Needed within 3 months
- [ ] Needed within 6 months
- [ ] No specific timeline

---

## 🤝 Contribution

**Would you like to work on implementing this feature?**
- [ ] Yes, I'd like to submit a pull request
- [ ] Yes, but I need guidance on the approach
- [ ] I can help with design/testing
- [ ] No, just suggesting the idea

---

*Thank you for your feature suggestion! We'll review this request and provide feedback on feasibility and timeline.*
```

---

## 📚 Documentation Template

### Template Configuration
```yaml
---
name: "📚 Documentation"
about: "Suggest improvements to documentation"
title: "[DOCS]: "
labels: ["type: documentation", "status: needs-triage"]
assignees: ''
---
```

### Template Content

```markdown
## 📚 Documentation Improvement Request

**Documentation Section:**
<!-- Which part of the documentation needs attention? -->

**Issue Type:**
- [ ] Missing documentation
- [ ] Incorrect information
- [ ] Outdated content
- [ ] Unclear explanation
- [ ] Broken links
- [ ] Formatting issues
- [ ] Translation needed

---

## 🎯 Current State

**What's currently documented:**
<!-- Describe the current state of the documentation -->

**Link to current documentation:**
<!-- Provide URL or file path -->

---

## ✨ Proposed Improvement

**What should be changed/added:**
<!-- Detailed description of the proposed changes -->

**Why this improvement is needed:**
<!-- Explain the benefit to users -->

**Suggested content:**
<!-- If you have specific content suggestions, include them here -->

---

## 👥 Target Audience

**Who would benefit from this documentation:**
- [ ] New users/beginners
- [ ] Experienced users
- [ ] Developers
- [ ] Administrators
- [ ] All users

---

## 🤝 Contribution Offer

**Can you help with this documentation?**
- [ ] Yes, I can write the content
- [ ] Yes, I can review/edit content
- [ ] I can provide examples/screenshots
- [ ] No, just identifying the need

---

*Thank you for helping improve our documentation!*
```

---

## 🔒 Security Vulnerability Template

### Template Configuration
```yaml
---
name: "🔒 Security Vulnerability"
about: "Report a security vulnerability (use private disclosure)"
title: "[SECURITY]: "
labels: ["type: security", "priority: critical"]
assignees: ['security-team']
---
```

### Template Content

```markdown
## ⚠️ SECURITY VULNERABILITY REPORT

**IMPORTANT:** If this is a security vulnerability, please do NOT create a public issue. Instead, please report it privately through one of these channels:

- **Email:** [SECURITY_EMAIL_ADDRESS]
- **Security Advisory:** Use [PLATFORM]'s private vulnerability reporting feature
- **Encrypted Communication:** [ENCRYPTED_CONTACT_METHOD]

---

## 🔒 Vulnerability Details

**Vulnerability Type:**
- [ ] Authentication bypass
- [ ] Authorization issues
- [ ] Data exposure
- [ ] Code injection
- [ ] Cross-site scripting (XSS)
- [ ] Cross-site request forgery (CSRF)
- [ ] Other: [describe]

**Severity Assessment:**
- [ ] Critical - Immediate action required
- [ ] High - Significant security risk
- [ ] Medium - Moderate security risk
- [ ] Low - Minor security concern

---

## 📋 Affected Components

**Affected versions:**
<!-- Which versions are affected? -->

**Affected components:**
<!-- Which parts of the system are vulnerable? -->

---

## 🔍 Proof of Concept

**Steps to reproduce:**
<!-- Provide minimal steps to demonstrate the vulnerability -->

**Expected impact:**
<!-- What could an attacker achieve? -->

---

## 🛡️ Suggested Mitigation

**Immediate workarounds:**
<!-- Any temporary measures users can take -->

**Proposed fix:**
<!-- If you have suggestions for fixing the vulnerability -->

---

## 📞 Contact Information

**Your contact details:**
<!-- How can we reach you for follow-up questions? -->

**Disclosure timeline:**
<!-- When do you plan to publicly disclose this vulnerability? -->

---

*Thank you for responsibly disclosing this security issue. We take security seriously and will respond promptly.*
```

---

## ❓ General Support Template

### Template Configuration
```yaml
---
name: "❓ General Support"
about: "Ask questions or get help"
title: "[SUPPORT]: "
labels: ["type: question", "status: needs-triage"]
assignees: ''
---
```

### Template Content

```markdown
## ❓ Support Request

**Question Type:**
- [ ] How-to question
- [ ] Configuration help
- [ ] Troubleshooting
- [ ] Best practices
- [ ] Integration guidance
- [ ] Other

---

## 🎯 What are you trying to achieve?

**Goal:**
<!-- Describe what you're trying to accomplish -->

**Context:**
<!-- Provide background information about your use case -->

---

## 🔧 Current Situation

**What have you tried:**
<!-- List the approaches you've already attempted -->

**Current behavior:**
<!-- What's happening now? -->

**Expected outcome:**
<!-- What would you like to happen? -->

---

## 📱 Environment

**System Information:**
- **Platform:** [PLATFORM_TYPE]
- **Version:** [APPLICATION_VERSION]
- **Configuration:** [RELEVANT_CONFIGURATION_SETTINGS]

---

## 📚 Research Done

**Documentation consulted:**
- [ ] README
- [ ] Official documentation
- [ ] FAQ
- [ ] Community forums
- [ ] Stack Overflow

**Search terms used:**
<!-- What did you search for? -->

---

## 🤝 Additional Information

**Urgency:**
- [ ] Blocking my work
- [ ] Important but not urgent
- [ ] Nice to know
- [ ] Just curious

**Willing to contribute:**
- [ ] Yes, I can help improve documentation based on the answer
- [ ] Yes, I can test solutions
- [ ] No, just need help

---

*Thank you for reaching out! We'll do our best to help you quickly.*
```

---

## 🛠️ Configuration & Setup

### GitHub Issue Template Configuration

Create a `.github/ISSUE_TEMPLATE/config.yml` file:

```yaml
blank_issues_enabled: false
contact_links:
  - name: 💬 Community Discussion
    url: [COMMUNITY_DISCUSSION_URL]
    about: Ask questions and discuss ideas with the community
  - name: 📖 Documentation
    url: [PROJECT_DOCUMENTATION_URL]
    about: Check our comprehensive documentation
  - name: 🔒 Security Issues
    url: [SECURITY_CONTACT_EMAIL]
    about: Report security vulnerabilities privately
```

### Automated Labeling

Set up GitHub Actions for automatic issue processing:

```yaml
name: Issue Triage
on:
  issues:
    types: [opened]

jobs:
  triage:
    runs-on: ubuntu-latest
    steps:
      - name: Add triage label
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.addLabels({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              labels: ['status: needs-triage']
            });
```

---

## 📊 Community Guidelines

### Issue Management Best Practices

1. **Response Time Goals**
   - Acknowledge new issues within [ACKNOWLEDGMENT_TIME]
   - Provide initial triage within [TRIAGE_TIME]
   - Regular updates on progress for complex issues

2. **Labeling Strategy**
   - **Type:** [TYPE_LABELS_LIST]
   - **Status:** [STATUS_LABELS_LIST]
   - **Priority:** [PRIORITY_LABELS_LIST]
   - **Area:** [AREA_LABELS_LIST]

3. **Community Engagement**
   - Welcome first-time contributors
   - Provide clear next steps for issue resolution
   - Encourage community discussion and collaboration
   - Recognize and thank contributors

### Contributor Recognition

- Use GitHub's contributor recognition features
- Mention contributors in release notes
- Create "good first issue" labels for newcomers
- Maintain a contributors file or hall of fame

---

## 📈 Template Effectiveness Metrics

### Success Indicators
- **Reduced back-and-forth:** [SUCCESS_METRIC_1]
- **Faster triage:** [SUCCESS_METRIC_2]
- **Higher quality reports:** [SUCCESS_METRIC_3]
- **Community engagement:** [SUCCESS_METRIC_4]
- **Resolution time:** [SUCCESS_METRIC_5]

### Regular Review Process
- [REVIEW_FREQUENCY_1] review of template effectiveness
- [REVIEW_FREQUENCY_2] updates based on community feedback
- [REVIEW_FREQUENCY_3] comprehensive review and refresh
- Continuous monitoring of [MONITORING_METRICS]

---

*These templates are designed to create a welcoming, efficient, and productive environment for all contributors. Thank you for helping make our project better!*
