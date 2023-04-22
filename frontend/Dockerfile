FROM node:18-alpine

COPY . app

# Set the working directory
WORKDIR app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files to the container
COPY . .

# Start the application
CMD ["npm", "run", "dev"]
