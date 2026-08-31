# Calorie Tracker Frontend

Frontend application for a calorie tracker built with Vite, React, TypeScript, and Material UI.

-----------

## Requirements

- Node.js 24 
- Package manager (npm, yarn, etc...)

-----------

## Installation

Clone the repository and enter the project directory:


```bash
git clone https://github.com/Heitor-Guerra/calorie-tracker.git
cd calorie-tracker/frontend
```

Install the dependencies:

### npm
```bash
npm install
```

### yarn
```bash
yarn install
```

-----------

## Environment Variables

Create a .env file in the root directory of the project:

```env
VITE_API_URL=http://127.0.0.1:8000
```

Update the API URL if the backend is running on a different host or port.

-------------

## Running the Application


_From now on, all commands will be shown on npm. For other package manager, switch `npm run` for `yarn` or `pnpm_

To start the Vite development server, run:

```bash
npm run dev
```

The application will, then, be available at:

`
http://localhost:5173/
`

--------------

## Building for Production

To create a production production build, run:

```bash
npm run build
```

The production files will be generated in the dist directory.

------------

## Previewing the Production Build

After creating a production build, preview it locally:

```bash
npm run preview
```

The preview server will be available at the address displayed in the terminal.

---------

## Backend Connection

Make sure the Calorie Tracker Backend is running before using features that require API access.

By default, the frontend expects the backend API to be available at:

`
http://127.0.0.1:8000/
`

If the backend uses a different URL, update the VITE_API_URL value in the .env file and restart the development server.

-----------

## Advise

The project is kind of unfinished. It would have some more things, like a page for the users to see their order, and a page for admins to Create, Edit and Delete items/categorie. 
The Django admin dashboard works great, though.
