FROM node:18-alpine

# Set the working directory
WORKDIR .

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files to the container
COPY . .

# Start the application
CMD ["npm", "run", "dev"]
