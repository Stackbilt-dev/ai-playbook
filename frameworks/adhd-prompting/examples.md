# ADHD Prompting Examples

## Example 1: API Development

### Traditional Prompt
```
I need help creating a REST API for a user management system. It should handle standard CRUD operations and include authentication. The API should be built with Node.js and Express, and I'd like to use MongoDB for the database. Please include proper error handling and validation.
```

### ADHD-Optimized
```markdown
🎯 TASK: Build user management API
🔧 STACK: Node.js, Express, MongoDB
📋 ENDPOINTS: 
- POST /users (create)
- GET /users/:id (read)
- PUT /users/:id (update)
- DELETE /users/:id (delete)
- POST /auth/login
✅ INCLUDE: JWT auth, validation, error handling
⚡ OUTPUT: Working code with comments
```

## Example 2: Debugging

### Traditional Prompt
```
My React application is showing a white screen after deployment. It works fine locally but when I deploy to Vercel, nothing renders. I've checked the console and there are no obvious errors. Could you help me figure out what might be wrong?
```

### ADHD-Optimized
```markdown
🐛 BUG: React app white screen
📍 WHERE: Vercel deployment only  
✅ WORKS: Local development
🔍 CHECKED: Console (no errors)
💭 SUSPECTS: Build config, env vars, routing
❓ NEED: Debug steps + fix
```

## Example 3: Learning Request

### Traditional Prompt
```
I want to learn about implementing real-time features in my web application. I've heard about WebSockets but I'm not sure how they differ from regular HTTP requests or when I should use them. Can you explain the concepts and maybe show me how to get started?
```

### ADHD-Optimized
```markdown
📚 LEARN: WebSockets basics
🎓 CURRENT: Know REST/HTTP
🎯 GOAL: Add real-time chat
⏱️ TIME: 30 minutes
💡 NEED: 
- WebSockets vs HTTP (quick)
- When to use (bullets)
- Starter code (Socket.io)
```

## Example 4: Complex Feature

### Traditional Prompt
```
I need to implement a file upload feature that supports multiple files, shows progress bars, validates file types and sizes, and stores the files in AWS S3. The frontend is React and the backend is Node.js. Security is important so please include proper validation.
```

### ADHD-Optimized
```markdown
🎯 FEATURE: Multi-file upload

📋 REQUIREMENTS:
- Multiple files
- Progress bars  
- Type validation (images only)
- Size limit (5MB)
- Store in S3

🔧 STACK:
- Frontend: React
- Backend: Node.js
- Storage: AWS S3

⚠️ CRITICAL: Security validation

✅ DELIVERABLES:
1. React component
2. API endpoint
3. S3 integration
4. Progress tracking
```

## Example 5: Code Review

### Traditional Prompt
```
Can you review this function and suggest improvements? It's supposed to process user data and return formatted results, but I feel like it could be more efficient and easier to read.

[code block]
```

### ADHD-Optimized
```markdown
🔍 REVIEW: User data processor

📋 CURRENT ISSUES:
- Performance concerns
- Readability problems

🎯 GOALS:
- Faster execution
- Cleaner code
- Same output

📊 METRICS:
- Current: 500ms/1000 records
- Target: <100ms

✅ FOCUS ON:
1. Algorithm efficiency
2. Code clarity
3. Edge cases
```

## Key Patterns Demonstrated

1. **Visual Hierarchy** - Emojis create scannable structure
2. **Information Density** - More info in less space
3. **Clear Boundaries** - Each section has one purpose
4. **No Ambiguity** - Explicit requirements, no inference needed
5. **Action-Oriented** - Always clear what's needed

## Results

### Token Efficiency
- Traditional: ~50-100 tokens average
- ADHD-Optimized: ~30-60 tokens average
- **Savings**: 40% fewer tokens

### Output Quality
- More consistent results
- Fewer clarification requests
- Better constraint adherence
- Cleaner code structure

### Cognitive Load
- Easier to verify completeness
- Quick to modify/iterate
- Clear success criteria
- Less mental overhead