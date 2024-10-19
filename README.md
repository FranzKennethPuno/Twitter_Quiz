# Platform Specification Document

## Overview
This document outlines the specifications for a platform where users can post content once, with various features for user management, post management, and admin functionalities.

## User Model
The User Model should include the following fields:
- **Email**: Unique identifier for user login.
- **Username**: Unique name chosen by the user.
- **Contact #**: User's contact number.

## Post Model
The Post Model must have the following fields:
- **User **: Reference to the User who created the post.
- **Content**: Text content of the post.
- **Created At**: Timestamp of when the post was created.

## User Registration
User  registration must collect the following information:
- **Email**
- **Username**
- **Contact #**
- **Password**
- **Confirm Password**

### Important Note
- Newly registered users should **NOT** be able to log in until an Admin approves/activates their account.

## Notifications
Proper messages should be displayed after actions, such as:
- Post created successfully
- Account successfully created
- Account approval notifications

## Reporting
Users should have the ability to report posts or other users. The report should include:
- A message describing the issue.

## Post List View
The Post List View must include:
- **Content of the post**: If the content exceeds 100 characters, it should be truncated with a "see more" option.
- **Username display**: Should be formatted as `admin123 > ad***123`.
- **Post creation date**: Must be in the format `YYYY-MM-DD`.
- **Pagination**: Display 3 posts per page.

## Admin Dashboard
The Admin Dashboard must include functionalities for:
- User registration approval
- Post management
- Post/User reports
- **Pagination**: Display 5 objects per page.

## Responsive Design
- Use **Bootstrap** to ensure the platform is responsive for both Desktop and Mobile devices.

## Dark Mode
- Implement a separate model for Dark Mode settings.

## Requirements
Create a `requirements.txt` file that lists all necessary packages for the project.

## README File
A detailed `README.md` file should be included with:
- Installation instructions
- Usage guidelines
- Available routes/links in the project

---

This document serves as a foundational guide for the development of the platform. Each section can be expanded upon as needed during the implementation phase.
