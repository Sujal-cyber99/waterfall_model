# waterfall_model

The **Waterfall Model** is a **linear, sequential** software development methodology. Each phase must be completed before moving on to the next—there's little room for revisiting earlier stages.

## Phases

1. **Requirement Analysis**
   - Define inputs: `a`, `b`, `c`, `time`
   - Desired output: `Temperature`

2. **System Design**
   - Design user interface (UI)
   - Define function:  
     ```
     T(t) = at^2 + bt + c
     ```

3. **Implementation**
   - Write Python code to implement the function and UI

4. **Testing**
   - Test using different coefficients
   - Check edge cases (e.g., `t = 0`, `t = 24`)

5. **Deployment**
   - Run on target systems
   - Collect user feedback

6. **Maintenance**
   - Fix bugs
   - Improve usability and performance

## Pros
- Clear, structured process
- Easy to manage for **simple, well-defined projects**

## Cons
Add Waterfall Model overview

- **Inflexible**: Difficult to adapt if requirements change
- Late discovery of issues (testing comes late)
