# Growth Path — Dashboard & Learning Platform (Dept 14 & 15)

**Project Owner:** Paul (Secretarial Notes)
**Date:** October 29, 2026
**Status:** New project — dashboard build for Dept 14 & 15

---

## Purpose

Build a single dashboard for Department 14 and Department 15 to track:

- Staff training paths & certifications
- Attendance tracking
- Education/training event ads (Google Ads / outreach)
- Connection to MCP server endpoints for OTA results
- Completion status pulled into the dashboard automatically
- Simple to view — one place for everything

---

## Features Needed

### 1. Admin Stuff
- Admin panel for setup/configuration
- User management (who's who)
- Role-based access

### 2. Attendance Tracker
- Track attendance at training events
- Log attendance by person/date
- Simple view — see who attended what

### 3. Training Path + Tip
- Show each person's training path
- Add tips/notes for each step
- Progress indicators

### 4. Login — Own Account + Google Auth
- Users log in with their own account
- Google Auth (OAuth) for sign-in
- Simple, single sign-on

### 5. Certifications / Help Requests
- Department 15 can request certifications
- Department 15 can request help/helpdesk tickets
- Track requests and status

### 6. LMS Connections
- Link to Moodle (training platform)
- Pull OTA results and completion status into the dashboard
- MCP server endpoints for real-time data

### 7. Dashboard View
- Simple, clean, easy to view
- Shows:
  - Who's done what (certifications)
  - Who needs help
  - Attendance at the last events
  - Next training events (with ads)

---

## Key Decisions

| Item | Decision |
|---|---|
| **Moodle** | Connect via API for course completion data |
| **MCP server** | Pull OTA results via MCP endpoints |
| **Auth** | Google OAuth for user login |
| **Dashboard** | Simple, one-page view per user |
| **Department 15** | Requests certifications + help through the dashboard |

---

## Action Items

- [ ] **Build dashboard** for Dept 14 & 15
- [ ] **Admin panel** for setup and user management
- [ ] **Attendance tracker** module
- [ ] **Training path** view with tips
- [ ] **Google Auth** for login
- [ ] **Certifications/help request** form (Dept 15)
- [ ] **Moodle integration** for course completions
- [ ] **MCP server endpoints** for OTA results
- [ ] **Simple dashboard view** per user
- [ ] **Training event ads** (Google Ads) for upcoming events

---

## Notes

- This is a **new project** filed today.
- Will be tracked in `Projects/Growth Path/` folder.
- Next steps: scope the dashboard, decide on Moodle vs. direct integration, build MVP.

---

## Source

Filed 2026-10-29 — growth path project for Dept 14 & 15 dashboard.
