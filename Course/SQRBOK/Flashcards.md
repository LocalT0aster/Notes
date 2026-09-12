# SQRBOK Flashcards

Generated from the SQRBOK source repository. **423 cards.**

> [!tip] Active recall
> Answer the question aloud before opening the answer callout. Cards labelled `source notes` provide relevant handbook cues, not an official model answer.

## Quality Models (10)

### Card 001 — Question 1: Garvin's Views — Definitions

> [!question] Question
> **Question 1: Garvin's Views — Definitions**
>
> Explain the difference between the **user-based** and **manufacturing-based** views of quality according to Garvin.
>
> Give one software example for each view that illustrates why they can lead to different quality assessments of the same product.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Garvin's Five Views of Quality
>
> David Garvin  identified five distinct perspectives on quality (see [Views](views.md) for full details). Each leads to different quality management approaches.
>
> | View | Definition | Example | Approach |
> |------|------------|---------|----------|
> | **Transcendent** | "I know it when I see it" | Rolex watch, Monet painting | Subjective judgment |
> | **Product-based** | More of attribute X is better | Smartphone specs, diamond carats | Measurable attributes |
> | **User-based** | Fitness for purpose | Toyota Corolla (reliable, low-maintenance) | Customer satisfaction |
> | **Manufacturing** | Conformance to specifications | Zero defects in assembly | Process control |
> | **Value-based** | Quality at acceptable cost | Budget airline ticket | ROI analysis |
>
> #### Detailed View Descriptions
>
> **1. Transcendent View**
> - Quality is absolute and universally recognizable but cannot be precisely defined
> - Often associated with excellence or "innate goodness"
> - *Example:* A luxury watch like a Rolex is recognized as high quality because of its superior craftsmanship and prestige
> - *Criticism:* Subjective and difficult to measure or operationalize
>
> **2. Product-Based View**
> - Quality is a precise and measurable variable based on product attributes
> - More features or better performance equals higher quality
> - *Example:* A smartphone with better resolution, longer battery life, and faster processing speed
> - *Criticism:* Assumes all improvements are desirable, ignoring trade-offs like cost
>
> …
>
> #### 3. **User-Based View** 👥
>
> - **Definition**: Quality is determined by the extent to which a product or service satisfies customer needs and preferences.
> - **Example**: A budget-friendly car like a Toyota Corolla is high quality to a customer who values reliability and low maintenance.
> - **Criticism**: Highly subjective and dependent on individual expectations, which can vary widely.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/foundations/RQ-L1-QM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/foundations/RQ-L1-QM.md)

### Card 002 — Question 2: Garvin's Views — Application

> [!question] Question
> **Question 2: Garvin's Views — Application**
>
> For ONE of the following development methodologies, identify which Garvin view is dominant and justify your answer:
> - SCRUM
> - XP (Extreme Programming)
> - RUP (Rational Unified Process)
> - Waterfall with FDA validation requirements

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Garvin's Five Views of Quality
>
> David Garvin  identified five distinct perspectives on quality (see [Views](views.md) for full details). Each leads to different quality management approaches.
>
> | View | Definition | Example | Approach |
> |------|------------|---------|----------|
> | **Transcendent** | "I know it when I see it" | Rolex watch, Monet painting | Subjective judgment |
> | **Product-based** | More of attribute X is better | Smartphone specs, diamond carats | Measurable attributes |
> | **User-based** | Fitness for purpose | Toyota Corolla (reliable, low-maintenance) | Customer satisfaction |
> | **Manufacturing** | Conformance to specifications | Zero defects in assembly | Process control |
> | **Value-based** | Quality at acceptable cost | Budget airline ticket | ROI analysis |
>
> #### Detailed View Descriptions
>
> **1. Transcendent View**
> - Quality is absolute and universally recognizable but cannot be precisely defined
> - Often associated with excellence or "innate goodness"
> - *Example:* A luxury watch like a Rolex is recognized as high quality because of its superior craftsmanship and prestige
> - *Criticism:* Subjective and difficult to measure or operationalize
>
> **2. Product-Based View**
> - Quality is a precise and measurable variable based on product attributes
> - More features or better performance equals higher quality
> - *Example:* A smartphone with better resolution, longer battery life, and faster processing speed
> - *Criticism:* Assumes all improvements are desirable, ignoring trade-offs like cost
>
> …
>
> #### 6-Step Process: From ISO to Requirements
>
> **Source:** Firesmith 2009
>
> | Step | Action | Purpose |
> |------|--------|---------|
> | 1 | **Determine Relevance** | Which ISO characteristics matter for this project? |
> | 2 | **Consider Context** | Review functional, data, interface requirements |
> | 3 | **Produce Criteria** | Define quality criteria for each characteristic |
> | 4 | **Select Measures** | Choose how to measure each criterion |
> | 5 | **Specify Requirements** | Write testable requirements with thresholds |
> | 6 | **Evaluate** | Validate completeness, testability, feasibility |
>
> > **Warning:** Skipping steps leads to vague requirements like "the system shall be fast."

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/foundations/RQ-L1-QM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/foundations/RQ-L1-QM.md)

### Card 003 — Question 3: McCall's Model Structure

> [!question] Question
> **Question 3: McCall's Model Structure**
>
> McCall's quality model has three levels: **factors**, **criteria**, and **metrics**.
>
> Explain the purpose of each level and describe how they relate to each other. Use **Maintainability** as an example to illustrate all three levels.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### McCall's Quality Model
>
> McCall  developed the first comprehensive software quality model for the US Air Force (see [Models](models.md) for full details).
>
> **Innovation:** First structured approach to software quality
> **Structure:** 11 quality factors in 3 categories
>
> #### The Three Categories
>
> | Category | Focus Question | What It Covers |
> |----------|---------------|----------------|
> | **Product Operation** | How well does it run? | Day-to-day functionality |
> | **Product Revision** | Can we change it? | Maintenance and evolution |
> | **Product Transition** | Can we move it? | Portability and integration |
>
> #### McCall's 11 Quality Factors
>
> | Category | Factors | Description |
> |----------|---------|-------------|
> | **Product Operation** | Correctness | Meets specified requirements |
> | | Reliability | Performs without failure |
> | | Efficiency | Uses minimal resources |
> | | Integrity | Protected from unauthorized access |
> | | Usability | Easy to learn and operate |
> | **Product Revision** | Maintainability | Easy to modify for corrections |
> | | Flexibility | Easy to modify for enhancements |
> | | Testability | Easy to validate and verify |
> | **Product Transition** | Portability | Runs in different environments |
> | | Reusability | Components can be reused |
> | | Interoperability | Works with other systems |
>
> #### Three-Level Structure
>
> McCall's model has three levels:
>
> 1. **Factor** — External view (what users see)
>    - Example: Reliability
> 2. **Criteria** — Internal view (what developers control)
>    - Example: Simplicity, Modularity
> 3. **Metric** — Measurement
>    - Example: Cyclomatic complexity
>
> **Key Insight:** Same criterion can affect multiple factors!
> - *Example:* Modularity → Maintainability AND Testability
>
> #### McCall's Quality Factors (1977)
>
> McCall's Quality Factors  are a set of characteristics introduced by Jim McCall in 1977 to measure and assess the quality of software systems. These factors help to evaluate software based on various attributes, contributing to a well-rounded understanding of software quality. McCall identified 11 quality factors, divided into three categories: **product operation**, **product revision**, and **product transition**.
>
> ```mermaid
> flowchart LR
>   A[McCall's Quality Factors]
>   A --> B[Product Operation 📊]
>   A --> C[Product Revision 🔧]
>   A --> D[Product Transition 🌐]
>
>   B --> B1[Correctness ✅<br>Reliability 🔒<br>Efficiency ⚡<br>Integrity 🔐<br>Usability 🖥️]
>   C --> C1[Maintainability 🔄<br>Flexibility 🛠️<br>Testability 🧪]
>   D --> D1[Portability 🌍<br>Reusability ♻️<br>Interoperability 🔗]
> ```
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/foundations/RQ-L1-QM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/foundations/RQ-L1-QM.md)

### Card 004 — Question 4: McCall's Categories

> [!question] Question
> **Question 4: McCall's Categories**
>
> McCall organized his 11 quality factors into three categories: Product Operation, Product Revision, and Product Transition.
>
> Pick **one** category and list its factors. For each factor, write one sentence explaining what it means in the context of a mobile banking app.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### McCall's Quality Factors (1977)
>
> McCall's Quality Factors  are a set of characteristics introduced by Jim McCall in 1977 to measure and assess the quality of software systems. These factors help to evaluate software based on various attributes, contributing to a well-rounded understanding of software quality. McCall identified 11 quality factors, divided into three categories: **product operation**, **product revision**, and **product transition**.
>
> ```mermaid
> flowchart LR
>   A[McCall's Quality Factors]
>   A --> B[Product Operation 📊]
>   A --> C[Product Revision 🔧]
>   A --> D[Product Transition 🌐]
>
>   B --> B1[Correctness ✅<br>Reliability 🔒<br>Efficiency ⚡<br>Integrity 🔐<br>Usability 🖥️]
>   C --> C1[Maintainability 🔄<br>Flexibility 🛠️<br>Testability 🧪]
>   D --> D1[Portability 🌍<br>Reusability ♻️<br>Interoperability 🔗]
> ```
>
> …
>
> #### McCall's Quality Model
>
> McCall  developed the first comprehensive software quality model for the US Air Force (see [Models](models.md) for full details).
>
> **Innovation:** First structured approach to software quality
> **Structure:** 11 quality factors in 3 categories
>
> #### The Three Categories
>
> | Category | Focus Question | What It Covers |
> |----------|---------------|----------------|
> | **Product Operation** | How well does it run? | Day-to-day functionality |
> | **Product Revision** | Can we change it? | Maintenance and evolution |
> | **Product Transition** | Can we move it? | Portability and integration |
>
> #### McCall's 11 Quality Factors
>
> | Category | Factors | Description |
> |----------|---------|-------------|
> | **Product Operation** | Correctness | Meets specified requirements |
> | | Reliability | Performs without failure |
> | | Efficiency | Uses minimal resources |
> | | Integrity | Protected from unauthorized access |
> | | Usability | Easy to learn and operate |
> | **Product Revision** | Maintainability | Easy to modify for corrections |
> | | Flexibility | Easy to modify for enhancements |
> | | Testability | Easy to validate and verify |
> | **Product Transition** | Portability | Runs in different environments |
> | | Reusability | Components can be reused |
> | | Interoperability | Works with other systems |
>
> #### Three-Level Structure
>
> McCall's model has three levels:
>
> 1. **Factor** — External view (what users see)
>    - Example: Reliability
> 2. **Criteria** — Internal view (what developers control)
>    - Example: Simplicity, Modularity
> 3. **Metric** — Measurement
>    - Example: Cyclomatic complexity
>
> **Key Insight:** Same criterion can affect multiple factors!
> - *Example:* Modularity → Maintainability AND Testability

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/foundations/RQ-L1-QM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/foundations/RQ-L1-QM.md)

### Card 005 — Question 5: Quality Attribute Tradeoffs

> [!question] Question
> **Question 5: Quality Attribute Tradeoffs**
>
> Perry showed that some quality attributes have **inverse relationships** (tradeoffs).
>
> Pick one of the following pairs and explain the tradeoff with a concrete software example:
> - Integrity vs Efficiency
> - Usability vs Efficiency
> - Flexibility vs Integrity

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Perry's Quality Attribute Relationships
>
> Perry  showed that quality attributes are **not independent** — they have relationships:
>
> | Relationship Type | Symbol | Meaning |
> |-------------------|--------|---------|
> | Direct | + | Both improve together |
> | Inverse | − | Tradeoff (one improves, other worsens) |
> | Neutral | (blank) | No relationship |
>
> #### Key Tradeoffs to Know
>
> | Attribute Pair | Relationship | Explanation |
> |----------------|--------------|-------------|
> | Integrity vs Efficiency | Inverse (−) | Access control adds overhead |
> | Usability vs Efficiency | Inverse (−) | Better UI requires more code |
> | Flexibility vs Integrity | Inverse (−) | Flexible data = security risks |
> | Portability vs Reusability | Direct (+) | Both benefit from good structure |
> | Maintainability vs Testability | Direct (+) | Well-structured code is easier to test |
>
> #### Perry's Tradeoff Matrix (Selected)
>
> | Attribute | Efficiency | Maintainability | Reusability |
> |-----------|:----------:|:---------------:|:-----------:|
> | **Integrity** | − | | − |
> | **Usability** | − | + | |
> | **Testability** | − | + | + |
> | **Portability** | − | + | + |
>
> > **Key Takeaway:** You cannot maximize all quality attributes simultaneously. Quality engineering is about **informed tradeoffs**.
>
> #### Perry’s Model of Quality Attribute Relationships
>
> Perry’s model  defines three types of relationships:
>
> 1. **Direct (+)**: If one attribute improves, the other improves too.
> 2. **Inverse (−)**: If one attribute improves, the other worsens.
> 3. **Neutral (N)**: The attributes are independent of each other.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/foundations/RQ-L1-QM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/foundations/RQ-L1-QM.md)

### Card 006 — Question 6: ISO 25010 Characteristics

> [!question] Question
> **Question 6: ISO 25010 Characteristics**
>
> Describe in your own words the following ISO 25010 quality characteristics:
> - **Security**
> - **Reliability**
> - **Maintainability**
>
> For each, give one example of a testable requirement.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### ISO/IEC 25010:2024 — 9 Characteristics
>
> Use ISO 25010 as a **checklist** when writing requirements:
>
> | # | Characteristic | Question It Answers |
> |---|----------------|---------------------|
> | 1 | **Functional Suitability** | Does it do what it should? |
> | 2 | **Performance Efficiency** | Is it fast/efficient enough? |
> | 3 | **Compatibility** | Does it work with others? |
> | 4 | **Usability** | Can users use it easily? |
> | 5 | **Reliability** | Does it keep working? |
> | 6 | **Security** | Is it protected? |
> | 7 | **Maintainability** | Can we change it? |
> | 8 | **Portability** | Can we move it? |
> | 9 | **Quality in Use** | Do users succeed? |
>
> #### Sub-Characteristics (Selected)
>
> | Characteristic | Sub-Characteristics |
> |----------------|---------------------|
> | **Functional Suitability** | Completeness, Correctness, Appropriateness |
> | **Performance Efficiency** | Time Behavior, Resource Utilization, Capacity |
> | **Reliability** | Maturity, Availability, Fault Tolerance, Recoverability |
> | **Security** | Confidentiality, Integrity, Non-repudiation, Accountability, Authenticity |
> | **Maintainability** | Modularity, Reusability, Analyzability, Modifiability, Testability |
>
> #### Quality Attributes in ISO/IEC 25002:2024
>
> ISO/IEC 25002:2024 builds on the previous work in quality models, particularly ISO/IEC 25010 (which defines product quality characteristics), but offers a more comprehensive overview for different contexts. The standard provides an organized structure for understanding and evaluating quality across systems, software, and IT services. Here are the primary quality attributes within the model:
>
> ```mermaid
> flowchart LR
>   A[ISO/IEC 25002:2024 Quality Model]
>
>   A --> B[Functional Suitability ✅]
>   A --> C[Performance Efficiency ⚡]
>   A --> D[Compatibility 🔗]
>   A --> E[Usability 🖥️]
>   A --> F[Reliability 🔒]
>   A --> G[Security 🔐]
>   A --> H[Maintainability 🔄]
>   A --> I[Portability 🌍]
>   A --> J[Quality in Use ⭐]
>
>   B --> B1[Functional Completeness<br>Functional Correctness<br>Functional Appropriateness]
>   C --> C1[Time Behavior<br>Resource Utilization<br>Capacity]
>   D --> D1[Coexistence<br>Interoperability]
>   E --> E1[Appropriateness Recognizability<br>Learnability<br>Operability<br>User Error Protection<br>User Interface Aesthetics]
>   F --> F1[Maturity<br>Availability<br>Fault Tolerance<br>Recoverability]
>   G --> G1[Confidentiality<br>Integrity<br>Non-repudiation<br>Accountability<br>Authenticity]
>   H --> H1[Modularity<br>Reusability<br>Analyzability<br>Modifiability<br>Testability]
>   I --> I1[Adaptability<br>Installability<br>Replaceability]
>   J --> J1[Effectiveness<br>Efficiency<br>Satisfaction<br>Freedom from Risk]
> ```
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/foundations/RQ-L1-QM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/foundations/RQ-L1-QM.md)

### Card 007 — Question 7: Quality Requirements — 6-Step Process

> [!question] Question
> **Question 7: Quality Requirements — 6-Step Process**
>
> Apply Firesmith's 6-step process to write a **testable performance requirement** for a search API that must respond quickly under normal load.
>
> Show your work for each step.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Worked Example: Search API Performance
>
> **Goal:** Write a performance requirement for a search API
>
> | Step | Action | Result |
> |------|--------|--------|
> | 1. Relevance | Performance Efficiency matters for UX | Selected |
> | 2. Context | Users expect quick search results | Search is critical |
> | 3. Criteria | Response time for search queries | Time-based criterion |
> | 4. Measure | P95 latency (95th percentile) | Measurable metric |
> | 5. Requirement | Write with template | Testable spec |
> | 6. Evaluate | Testable? Feasible? Complete? | Approved |
>
> **Resulting Requirement:**
> ```
> While under normal load (< 1000 concurrent users), the Search API
> shall respond in < 200ms, 95% of the time.
> ```
>
> #### 6-Step Process: From ISO to Requirements
>
> **Source:** Firesmith 2009
>
> | Step | Action | Purpose |
> |------|--------|---------|
> | 1 | **Determine Relevance** | Which ISO characteristics matter for this project? |
> | 2 | **Consider Context** | Review functional, data, interface requirements |
> | 3 | **Produce Criteria** | Define quality criteria for each characteristic |
> | 4 | **Select Measures** | Choose how to measure each criterion |
> | 5 | **Specify Requirements** | Write testable requirements with thresholds |
> | 6 | **Evaluate** | Validate completeness, testability, feasibility |
>
> > **Warning:** Skipping steps leads to vague requirements like "the system shall be fast."

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/foundations/RQ-L1-QM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/foundations/RQ-L1-QM.md)

### Card 008 — Question 8: Quality Requirements — Template

> [!question] Question
> **Question 8: Quality Requirements — Template**
>
> A developer writes: *"The system shall be fast and reliable."*
>
> Explain why this is a **poor quality requirement**. Rewrite it as **two separate testable requirements** using the template:
>
> ```
> While in [condition], the [component] shall exhibit [attribute] of [threshold] [measurement].
> ```

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Quality Requirements Template
>
> **Template:**
> ```
> While in [condition], the [component] shall exhibit
> [quality attribute] of [threshold] [measurement].
> ```
>
> **Examples:**
>
> | Requirement | Condition | Attribute | Threshold |
> |-------------|-----------|-----------|-----------|
> | API response time | Normal operation | Performance | < 200ms, 95% |
> | Data integrity | Production | Reliability | 99.99% |
> | System availability | Under load | Availability | > 99.9% |
> | Login authentication | All users | Security | 0 unauthorized access |
>
> #### 6-Step Process: From ISO to Requirements
>
> **Source:** Firesmith 2009
>
> | Step | Action | Purpose |
> |------|--------|---------|
> | 1 | **Determine Relevance** | Which ISO characteristics matter for this project? |
> | 2 | **Consider Context** | Review functional, data, interface requirements |
> | 3 | **Produce Criteria** | Define quality criteria for each characteristic |
> | 4 | **Select Measures** | Choose how to measure each criterion |
> | 5 | **Specify Requirements** | Write testable requirements with thresholds |
> | 6 | **Evaluate** | Validate completeness, testability, feasibility |
>
> > **Warning:** Skipping steps leads to vague requirements like "the system shall be fast."

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/foundations/RQ-L1-QM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/foundations/RQ-L1-QM.md)

### Card 009 — Question 9: Quality in Use vs Product Quality

> [!question] Question
> **Question 9: Quality in Use vs Product Quality**
>
> Explain the difference between **Product Quality** and **Quality in Use** according to ISO 25010.
>
> Give an example where a software product has high product quality (e.g., maintainability, reliability) but low quality in use.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### ISO/IEC 25010:2024 — 9 Characteristics
>
> Use ISO 25010 as a **checklist** when writing requirements:
>
> | # | Characteristic | Question It Answers |
> |---|----------------|---------------------|
> | 1 | **Functional Suitability** | Does it do what it should? |
> | 2 | **Performance Efficiency** | Is it fast/efficient enough? |
> | 3 | **Compatibility** | Does it work with others? |
> | 4 | **Usability** | Can users use it easily? |
> | 5 | **Reliability** | Does it keep working? |
> | 6 | **Security** | Is it protected? |
> | 7 | **Maintainability** | Can we change it? |
> | 8 | **Portability** | Can we move it? |
> | 9 | **Quality in Use** | Do users succeed? |
>
> #### Sub-Characteristics (Selected)
>
> | Characteristic | Sub-Characteristics |
> |----------------|---------------------|
> | **Functional Suitability** | Completeness, Correctness, Appropriateness |
> | **Performance Efficiency** | Time Behavior, Resource Utilization, Capacity |
> | **Reliability** | Maturity, Availability, Fault Tolerance, Recoverability |
> | **Security** | Confidentiality, Integrity, Non-repudiation, Accountability, Authenticity |
> | **Maintainability** | Modularity, Reusability, Analyzability, Modifiability, Testability |
>
> #### Quality Attributes in ISO/IEC 25002:2024
>
> ISO/IEC 25002:2024 builds on the previous work in quality models, particularly ISO/IEC 25010 (which defines product quality characteristics), but offers a more comprehensive overview for different contexts. The standard provides an organized structure for understanding and evaluating quality across systems, software, and IT services. Here are the primary quality attributes within the model:
>
> ```mermaid
> flowchart LR
>   A[ISO/IEC 25002:2024 Quality Model]
>
>   A --> B[Functional Suitability ✅]
>   A --> C[Performance Efficiency ⚡]
>   A --> D[Compatibility 🔗]
>   A --> E[Usability 🖥️]
>   A --> F[Reliability 🔒]
>   A --> G[Security 🔐]
>   A --> H[Maintainability 🔄]
>   A --> I[Portability 🌍]
>   A --> J[Quality in Use ⭐]
>
>   B --> B1[Functional Completeness<br>Functional Correctness<br>Functional Appropriateness]
>   C --> C1[Time Behavior<br>Resource Utilization<br>Capacity]
>   D --> D1[Coexistence<br>Interoperability]
>   E --> E1[Appropriateness Recognizability<br>Learnability<br>Operability<br>User Error Protection<br>User Interface Aesthetics]
>   F --> F1[Maturity<br>Availability<br>Fault Tolerance<br>Recoverability]
>   G --> G1[Confidentiality<br>Integrity<br>Non-repudiation<br>Accountability<br>Authenticity]
>   H --> H1[Modularity<br>Reusability<br>Analyzability<br>Modifiability<br>Testability]
>   I --> I1[Adaptability<br>Installability<br>Replaceability]
>   J --> J1[Effectiveness<br>Efficiency<br>Satisfaction<br>Freedom from Risk]
> ```
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/foundations/RQ-L1-QM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/foundations/RQ-L1-QM.md)

### Card 010 — Question 10: Kano Model — Must-Haves vs Delighters

> [!question] Question
> **Question 10: Kano Model — Must-Haves vs Delighters**
>
> What is the difference between **must-have attributes** and **delighters** in the Kano model?
>
> Give two software examples of each type for a video streaming application (like Netflix).

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Quality Model Definitions
>
> **Simple Definition:**
> > A model with the objective to describe, assess, and/or predict quality.
>
> **ISO 25000 Definition:**
> > A defined set of characteristics, and of relationships between them, which provides a framework for specifying quality requirements and evaluating quality.
>
> **Full Definition:**
> > A structured specification of quality in terms of characteristics, attributes, their relationships, and corresponding measurement scales and methods.
>
> #### Quality Model Hierarchy
>
> ```
> Quality Model
> ├── Quality Characteristic (e.g., Reliability)
> │   ├── Quality Attribute (e.g., Fault Tolerance)
> │   │   ├── Measurement Scale
> │   │   └── Measurement Method
> │   └── Quality Attribute (e.g., Recoverability)
> └── Quality Characteristic (e.g., Usability)
>     └── ...
> ```
>
> **Key Distinction:**
> - **Characteristics** are high-level (not directly measurable)
> - **Attributes** can be measured

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/foundations/RQ-L1-QM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/foundations/RQ-L1-QM.md)

## Quality Measurement (12)

### Card 011 — Question 1: Measurement Definitions

> [!question] Question
> **Question 1: Measurement Definitions**
>
> State **Hubbard's definition** of measurement. Compare it with **Garvin's Transcendent view** of quality.
>
> How does Hubbard's argument ("everything is measurable") challenge the transcendent view ("I know it when I see it")?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Hubbard's Argument: Everything is Measurable
>
> Hubbard  provides a logical argument:
>
> **If X is something we care about:**
> 1. X must be detectable somehow (or why would we care?)
> 2. If detectable, it exists in some amount
> 3. If it exists in some amount, it can be measured
>
> > **Implication:** "Intangibles" like quality, risk, and user satisfaction ARE measurable.
>
> > **Key Insight:** We don't need perfect measurement. Reducing uncertainty, even a little, has value.
>
> #### Everything is Measurable
>
> {: .highlight }
> "Everything is measurable."
>
> *(D. Hubbard, How to Measure Anything, 2010) *
>
> If **X** is something we care about, then **X**, by definition, must be detectable. Consider concepts like “quality,” “risk,” “security,” or “public image.” If these concepts were entirely undetectable, how could we care about them? The very act of caring about these concepts implies they correspond to desirable or undesirable outcomes.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/measurement/RQ_L2_Metrics.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/measurement/RQ_L2_Metrics.md)

### Card 012 — Question 2: Resolution, Accuracy, Precision

> [!question] Question
> **Question 2: Resolution, Accuracy, Precision**
>
> Define **resolution**, **accuracy**, and **precision** in the context of measurement.
>
> A tool consistently reports cyclomatic complexity as 10, but manual calculation shows 12. Is the tool accurate? Is it precise?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Resolution, Accuracy, Precision
>
> | Property | Definition | Example |
> |----------|------------|---------|
> | **Resolution** | Smallest detectable change | Timer with 1ms vs 1s granularity |
> | **Accuracy** | How close to true value | Thermometer reads 20.5°C when actual is 20°C |
> | **Precision** | Repeatability of measurements | Same code analyzed twice gives same cyclomatic complexity |
>
> > **Exam Tip:** High precision with low accuracy = consistent but wrong! A ruler that always measures 1cm short is precise (repeatable) but inaccurate.
>
> #### Practice Questions
>
> 1. According to Hubbard, what is the purpose of measurement?
> 2. What are the three components of an IEEE 1061 metric?
> 3. A tool consistently reports cyclomatic complexity as 10, but manual calculation shows 12. Is the tool accurate? Is it precise?

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/measurement/RQ_L2_Metrics.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/measurement/RQ_L2_Metrics.md)

### Card 013 — Question 3: Three Measurement Pitfalls

> [!question] Question
> **Question 3: Three Measurement Pitfalls**
>
> **Case:** A company mandates 80% code coverage for all releases. After 6 months, coverage is 85% but production defects have not decreased. Developers complain about "writing tests just to hit the number."
>
> Using Hoffman's three dangers (bad statistics, bad decisions, bad incentives), analyze what went wrong in this scenario.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Three Dangers in Metrics
>
> Hoffman  identified three ways metrics can go wrong:
>
> | Danger | Description | Example |
> |--------|-------------|---------|
> | **Bad Statistics** | Misunderstanding measurement theory | Using mean on ordinal data |
> | **Bad Decisions** | Incorrect use of data | Ignoring confounding variables |
> | **Bad Incentives** | Disregard for human factors | Developers "gaming" coverage metrics |
>
> > "People's behaviors change in predictable ways to provide the answers management asks for when metrics are applied." — Hoffman (2000)
>
> #### Why Measurement Matters
>
> We measure software to make informed decisions about:
> - **Quality** — Is the product good enough to release?
> - **Productivity** — Are we delivering value efficiently?
> - **Risk** — What areas need attention?
> - **Improvement** — Are our changes working?
>
> Metrics feed into critical business decisions: release approval, resource allocation, process improvement, and performance evaluation.
>
> > **Warning:** "You can't manage what you can't measure" — but bad metrics lead to bad management!

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/measurement/RQ_L2_Metrics.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/measurement/RQ_L2_Metrics.md)

### Card 014 — Question 4: McNamara Fallacy and Streetlight Effect

> [!question] Question
> **Question 4: McNamara Fallacy and Streetlight Effect**
>
> **Case:** A manager evaluates developer performance using: commits/week, LOC added, and bugs closed. Developer A scores high on all metrics. Developer B scores lower but mentors juniors, improves architecture, and reduces technical debt. Developer A gets promoted.
>
> Which fallacy (McNamara or Streetlight) applies here? Could both apply?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The McNamara Fallacy
>
> Named for Robert McNamara, US Secretary of Defense 1961-1968.
>
> **Definition:** Making decisions based solely on quantitative observations while ignoring those that are difficult to measure.
>
> **Vietnam War Example:**
> - Strategy based on "body counts" (quantifiable)
> - Ignored morale, political will, terrain (hard to measure)
> - Quantifiable metrics ≠ important metrics
>
> **In Software:**
> - Tracking defect counts because they're easy to measure
> - Ignoring code quality, technical debt, developer satisfaction
>
> > "To omit [unmeasurable] variables is equivalent to saying that they have zero effect... Probably the only value known to be wrong." — Forrester (1961)
>
> Forrester  emphasized that ignoring hard-to-measure variables doesn't make them irrelevant.
>
> #### The Streetlight Effect
>
> **The Parable:** A man searches for his keys under a streetlight, not where he dropped them, because "the light is better here."
>
> **In Software Metrics:**
> - Measuring what tools report automatically, not what matters
> - Tracking code coverage because it's easy to automate
> - Ignoring usability because it's hard to quantify
>
> > **Antidote:** Start with goals (GQM), then find measures. Not the reverse!

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/measurement/RQ_L2_Metrics.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/measurement/RQ_L2_Metrics.md)

### Card 015 — Question 5: Measurement Scales (NOIR)

> [!question] Question
> **Question 5: Measurement Scales (NOIR)**
>
> Explain Stevens' four measurement scales: Nominal, Ordinal, Interval, and Ratio.
>
> For each scale give a software metric example.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Stevens' Measurement Scales
>
> Stevens  defined four measurement scales in his seminal 1946 paper. The mnemonic **NOIR** (French for "black") helps remember them:
>
> | Scale | Properties | Valid Operations | Software Example |
> |-------|------------|------------------|------------------|
> | **N**ominal | Categories only | =, ≠, count | Bug type (UI, logic, data) |
> | **O**rdinal | Categories + order | <, >, rank | Severity (Low, Med, High, Critical) |
> | **I**nterval | Order + magnitude | +, -, mean | Temperature change |
> | **R**atio | True zero | ×, ÷, all | LOC, defect count, time |
>
> #### Measurement Scales
>
> Understanding measurement scales is critical for proper analysis:
>
> | Scale | Properties | Examples | Valid Operations |
> |-------|-----------|----------|------------------|
> | **Nominal** | Categories, no order | Bug types, OS platforms | Count, mode |
> | **Ordinal** | Ordered categories | Severity (low/med/high), priority | Median, percentile |
> | **Interval** | Equal intervals, no true zero | Dates, temperatures | Mean, std deviation |
> | **Ratio** | Equal intervals, true zero | LOC, defects, time | All arithmetic |
>
> **Why it matters**: You can't calculate the mean of bug severity levels (ordinal), but you can find the median.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/measurement/RQ_L2_Metrics.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/measurement/RQ_L2_Metrics.md)

### Card 016 — Question 6: Mean vs Median

> [!question] Question
> **Question 6: Mean vs Median**
>
> When should you use **mean** vs **median** for software metrics?
>
> If 9 bugs take 1 hour each and 1 bug takes 100 hours, calculate both and explain which better represents "typical" bug fix time.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Central Tendency: Mean, Median, Mode
>
> | Measure | When to Use | Software Example |
> |---------|-------------|------------------|
> | **Mean** | Symmetric data, ratio scale | Average response time |
> | **Median** | Skewed data, outliers present | Bug fix time |
> | **Mode** | Categorical data, most frequent | Most common defect type |
>
> **Example: Bug Fix Times**
>
> If 9 bugs take 1 hour each and 1 bug takes 100 hours:
> - Mean: (9×1 + 1×100) / 10 = **10.9 hours**
> - Median: **1 hour** ← Better representation!
>
> > **Exam Tip:** For software metrics with outliers (bug fix time, response time, effort), prefer median over mean.
>
> #### Averages: Mean, Median, and Mode
>
> - **Arithmetic Mean**: The sum of values divided by the count. Commonly referred to as the "average."
> - **Median**: The middle value in a sorted dataset. Useful for skewed distributions.
> - **Mode**: The most frequently occurring value in the dataset.
>
> #### Additional Types:
> - **Geometric Mean**: Useful when averaging rates or ratios. It normalizes differences in numeric ranges.
> - **Harmonic Mean**: Appropriate for averaging rates (e.g., speed, productivity). It is always the smallest of the three Pythagorean means (arithmetic, geometric, harmonic).
>
> **Example of Geometric Mean**:
> Comparing two companies based on environmental sustainability (0–5 scale) and financial viability (0–100 scale). The geometric mean prevents the larger numeric range (financial viability) from dominating the result.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/measurement/RQ_L2_Metrics.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/measurement/RQ_L2_Metrics.md)

### Card 017 — Question 7: Confounding Variables

> [!question] Question
> **Question 7: Confounding Variables**
>
> What is a **confounding variable**? Why is it important in metrics research?
>
> El Emam et al. (2001) found that class size confounds OO metrics. Explain this finding and its implications.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The Hidden Variable Problem
>
> El Emam et al.  conducted a landmark study on object-oriented metrics:
>
> > "Only four, out of twenty-four commonly used object-oriented metrics, were actually useful in predicting the quality of a software module when the effect of the module size was accounted for."
>
> **Common Confounders in Software Research:**
>
> | Confounder | What It Affects |
> |------------|-----------------|
> | Module/class size | Almost everything! |
> | Developer experience | Defect rates, productivity |
> | Time pressure | Quality, technical debt |
> | Technology stack | Performance, maintainability |
>
> > **Solution:** Control for confounders in analysis, or use randomized experiments (A/B testing).
>
> #### Chidamber-Kemerer OO Metrics Suite
>
> Chidamber and Kemerer  defined six metrics for object-oriented design:
>
> | Metric | Full Name | Measures | High Value Indicates |
> |--------|-----------|----------|---------------------|
> | **WMC** | Weighted Methods per Class | Sum of method complexities | Complex class, hard to test |
> | **DIT** | Depth of Inheritance Tree | Distance from root class | Complex hierarchy |
> | **NOC** | Number of Children | Immediate subclasses | High influence, careful changes needed |
> | **CBO** | Coupling Between Objects | External class dependencies | Hard to reuse, ripple effects |
> | **RFC** | Response For Class | Methods callable from class | Difficult to test |
> | **LCOM** | Lack of Cohesion in Methods | Method dissimilarity | Class should be split |
>
> > **Exam Tip:** Remember that El Emam et al. found only 4 of 24 OO metrics useful after controlling for class size!

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/measurement/RQ_L2_Metrics.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/measurement/RQ_L2_Metrics.md)

### Card 018 — Question 8: GQM Framework

> [!question] Question
> **Question 8: GQM Framework**
>
> Apply Basili's **Goal-Question-Metric (GQM)**to define metrics for the goal: "Improve maintainability of the codebase."

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Basili's GQM Framework
>
> Basili  developed the Goal-Question-Metric paradigm to ensure metrics serve real purposes:
>
> | Level | Purpose | Example |
> |-------|---------|---------|
> | **Goal** | Define business/project objective | Improve code maintainability |
> | **Question** | What do we need to know? | How complex is each module? |
> | **Metric** | How do we quantify the answer? | Cyclomatic complexity |
>
> #### Goal Template
>
> Write goals using this structure:
>
> | Element | Description | Example |
> |---------|-------------|---------|
> | **Object** | What are we studying? | The code base |
> | **Purpose** | Why? (Improve, understand, control) | Improve |
> | **Focus** | What quality aspect? | Maintainability |
> | **Stakeholder** | For whom? | Development team |
> | **Context** | Environment/constraints | New team members joining |
>
> **Complete Goal:** "Improve maintainability of the code base from the perspective of the development team in the context of new team members joining."
>
> #### GQM Example
>
> | Goal | Improve code maintainability for new team members |
> |------|--------------------------------------------------|
> | **Question 1** | How complex are modules? |
> | **Metric 1a** | Cyclomatic complexity |
> | **Metric 1b** | Lines of code |
> | **Question 2** | Are modules well-documented? |
> | **Metric 2a** | Comment ratio |
> | **Metric 2b** | Documentation coverage |
>
> #### Maintainability Metrics:
>
> - **Cyclomatic Complexity**: Again used to assess maintainability.
> - **Tech Debt**: Metrics like SQALE and SONAR evaluate technical debt.
> - **Dependency Analysis**: Helps to understand and manage code dependencies and change impacts using methods like Design Structure Matrix.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/measurement/RQ_L2_Metrics.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/measurement/RQ_L2_Metrics.md)

### Card 019 — Question 9: Maintainability Index

> [!question] Question
> **Question 9: Maintainability Index**
>
> Explain the **Maintainability Index (MI)** formula and its components.
>
> What does MI = 171 − 5.2×ln(HV) − 0.23×CC − 16.2×ln(LOC) tell us? What are its limitations?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Maintainability Index (1992)
>
> Oman and Hagemeister  developed the Maintainability Index using empirical data from HP C and Pascal codebases.
>
> **Formula (Visual Studio normalized variant):**
>
> ```
> MI = max(0, (171 - 5.2×ln(HV) - 0.23×CC - 16.2×ln(LOC)) × 100/171)
> ```
>
> The original Oman & Hagemeister (1992) formula produces values on a 0–171 scale. Visual Studio normalizes this to 0–100 by multiplying by 100/171 and clamping at 0.
>
> Where:
> - HV = Halstead Volume
> - CC = Cyclomatic Complexity
> - LOC = Lines of Code
>
> **Interpretation:**
>
> | MI Score | Color | Meaning |
> |----------|-------|---------|
> | 20-100 | Green | Good maintainability |
> | 10-19 | Yellow | Moderate, needs attention |
> | 0-9 | Red | Poor, difficult to maintain |
>
> > **Key Insight:** MI uses McCabe CC as a component! High complexity directly reduces maintainability.
>
> #### Lines of Code (LOC)
>
> **Definition:** Physical count of source lines (typically via `wc -l`)
>
> | Project | LOC | Category |
> |---------|-----|----------|
> | Expression Evaluator | 450 | Small utility |
> | Sudoku Solver | 2,000 | Small application |
> | Linux Kernel | 6,000,000 | Large system |
> | Windows XP | 45,000,000 | Massive codebase |
>
> **Cautions:**
> - Physical LOC ≠ Logical LOC (statements vs lines)
> - Doesn't measure functionality
> - Varies by coding style and language
> - More code ≠ more value

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/measurement/RQ_L2_Metrics.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/measurement/RQ_L2_Metrics.md)

### Card 020 — Question 10: Chidamber-Kemerer OO Metrics

> [!question] Question
> **Question 10: Chidamber-Kemerer OO Metrics**
>
> List **five** CK OO metrics (1994) and explain what each measures.
>
> For each metric, state what a high value indicates about the class.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Chidamber-Kemerer OO Metrics Suite
>
> Chidamber and Kemerer  defined six metrics for object-oriented design:
>
> | Metric | Full Name | Measures | High Value Indicates |
> |--------|-----------|----------|---------------------|
> | **WMC** | Weighted Methods per Class | Sum of method complexities | Complex class, hard to test |
> | **DIT** | Depth of Inheritance Tree | Distance from root class | Complex hierarchy |
> | **NOC** | Number of Children | Immediate subclasses | High influence, careful changes needed |
> | **CBO** | Coupling Between Objects | External class dependencies | Hard to reuse, ripple effects |
> | **RFC** | Response For Class | Methods callable from class | Difficult to test |
> | **LCOM** | Lack of Cohesion in Methods | Method dissimilarity | Class should be split |
>
> > **Exam Tip:** Remember that El Emam et al. found only 4 of 24 OO metrics useful after controlling for class size!
>
> #### Object-Oriented Metrics
>
> When working with object-oriented programming, several key metrics help evaluate software quality:
>
> 1. **Number of Methods per Class**: Indicates the complexity of a class.
> 2. **Depth of Inheritance Tree**: Measures how deeply a class is inherited.
> 3. **Number of Child Classes**: Tracks the number of subclasses for a class.
> 4. **Coupling Between Object Classes**: Evaluates how interconnected different classes are.
> 5. **Calls to Methods in Unrelated Classes**: Measures the extent of cross-class interactions.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/measurement/RQ_L2_Metrics.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/measurement/RQ_L2_Metrics.md)

### Card 021 — Question 11: Operational Definitions

> [!question] Question
> **Question 11: Operational Definitions**
>
> Park (1992) defines two criteria for operational definitions: **communication** and **repeatability**.
>
> Team A reports 15 defects/KLOC, Team B reports 8 defects/KLOC. Before concluding Team B has better quality, what operational definition questions must you ask? (Consider: what counts as a defect? when is it counted? what's included in KLOC?)

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Criteria for a Good Operational Definition:
>
> 1. **Communication**: Does the definition clearly describe what is being measured, how it is measured, and what is included/excluded?
> 2. **Repeatability**: Can others replicate the measurement process and achieve the same results?
>
> **Examples of Operational Definitions**:
>
> - Software Quality Measurement: Counting problems and defects.
> - Software Effort and Schedule Measurement: Counting staff-hours and reporting schedule data.
> - Software Size Measurement: Counting source statements.
>
> References:
>
> - *Software Quality Measurement* (CMU/SEI-92-TR-22, ADA258556)
> - *Software Effort and Schedule Measurement* (CMU/SEI-92-TR-21, ADA258279)
> - *Software Size Measurement* (CMU/SEI-92-TR-20, ADA258304)
>
> #### Operational Definitions
>
> Park  established two criteria for operational definitions:
>
> | Criterion | Question |
> |-----------|----------|
> | **Communication** | Would others know exactly what was measured? |
> | **Repeatability** | Could others repeat the measurement and get the same result? |
>
> **Example: "Hours Worked on Project"**
>
> Without operational definition, this is ambiguous:
>
> | Ambiguity | Options |
> |-----------|---------|
> | **Source** | Time reporting system or estimates? |
> | **Labor type** | Direct (developers) or indirect (sponsors)? |
> | **Hours** | Paid only or include unpaid overtime? |
> | **Activities** | Include meetings? Training? |
>
> **Good Operational Definition:**
> > "Hours worked: Paid hours logged in the time tracking system by direct development staff (developers, testers, architects) for activities classified as 'development' or 'testing', excluding meetings and training."

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/measurement/RQ_L2_Metrics.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/measurement/RQ_L2_Metrics.md)

### Card 022 — Question 12: From Quality Models to Metrics

> [!question] Question
> **Question 12: From Quality Models to Metrics**
>
> Explain the hierarchy: Characteristic → Sub-characteristic → Measure (using ISO 25010/25023).
>
> Give an example showing how "Maintainability" leads to a specific measurable metric.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Metrics and Quality Models
>
> Metrics operationalize quality models:
>
> **ISO/IEC 25010 Quality Model → Metrics:**
> - Reliability → Defect density, MTBF, availability
> - Performance → Response time, throughput, resource utilization
> - Maintainability → Cyclomatic complexity, coupling, cohesion
> - Security → Vulnerability count, OWASP compliance score
>
> **GQM Bridges Goals and Metrics:**
> - Start with quality model dimensions as goals
> - Derive questions about each dimension
> - Select metrics that answer those questions
>
> #### Maintainability Metrics:
>
> - **Cyclomatic Complexity**: Again used to assess maintainability.
> - **Tech Debt**: Metrics like SQALE and SONAR evaluate technical debt.
> - **Dependency Analysis**: Helps to understand and manage code dependencies and change impacts using methods like Design Structure Matrix.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/define/measurement/RQ_L2_Metrics.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/define/measurement/RQ_L2_Metrics.md)

## Verification Methods (11)

### Card 023 — Question 1: Four Verification Techniques — Definitions

> [!question] Question
> **Question 1: Four Verification Techniques — Definitions**
>
> List the four verification techniques (INCOSE taxonomy) and provide a one-sentence definition for each.
>
> For each technique, give one example of when it would be the most appropriate choice.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The Four Verification Techniques
>
> | Technique | Definition | Best For |
> |-----------|------------|----------|
> | **Inspection** | Human examination of artifacts | Faults of omission, style, early detection |
> | **Analysis** | Model-based evaluation without execution | Formal properties, concurrency, security |
> | **Testing** | Execution under controlled conditions | Dynamic behavior, integration issues |
> | **Demonstration** | Operation in real/production environment | User acceptance, performance validation |
>
> **Defense in Depth:** No single technique finds all defects. Combine them!
>
> #### INCOSE Definitions
>
> | Technique | INCOSE Definition |
> |-----------|-------------------|
> | **Inspection** | Determining performance by examining engineering documentation or the item itself using visual means or simple measurements |
> | **Analysis** | Verification method of determining performance or other properties from analytical evidence |
> | **Testing** | Verification by operating the system under controlled conditions and analyzing results |
> | **Demonstration** | Verification by observing the item's operation under natural or production-like conditions |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/overview/RQ_L03_Verification.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/overview/RQ_L03_Verification.md)

### Card 024 — Question 2: Inspection Techniques Spectrum

> [!question] Question
> **Question 2: Inspection Techniques Spectrum**
>
> Inspection techniques range from formal (Fagan) to informal (ad-hoc).
>
> Name **four** different inspection techniques in order from most formal to least formal. For each, describe when it would be appropriate to use.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Inspection Techniques — From Formal to Informal
>
> | Technique | Description | Overhead |
> |-----------|-------------|----------|
> | **Fagan Inspections** | Well-defined entry/exit conditions. Presenter ≠ author. | High |
> | **Team Review** | Formal meeting with project personnel, managers, stakeholders. | Medium-High |
> | **Walkthrough** | Author leads team through artifact. Questions encouraged. | Medium |
> | **Tool-Assisted Code Review** | Line-by-line critique via diff, annotations, GitHub PRs. | Low-Medium |
> | **Pair Programming** | Real-time review. Two developers at one workstation. | Built-in |
> | **Ad-hoc Review** | Unstructured, spontaneous. Least formal. | Lowest |
>
> #### The Four Verification Techniques
>
> | Technique | Definition | Best For |
> |-----------|------------|----------|
> | **Inspection** | Human examination of artifacts | Faults of omission, style, early detection |
> | **Analysis** | Model-based evaluation without execution | Formal properties, concurrency, security |
> | **Testing** | Execution under controlled conditions | Dynamic behavior, integration issues |
> | **Demonstration** | Operation in real/production environment | User acceptance, performance validation |
>
> **Defense in Depth:** No single technique finds all defects. Combine them!

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/overview/RQ_L03_Verification.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/overview/RQ_L03_Verification.md)

### Card 025 — Question 3: Inspection vs Testing

> [!question] Question
> **Question 3: Inspection vs Testing**
>
> Inspection and testing are complementary verification techniques.
>
> Compare and contrast inspection and testing across **three** dimensions (e.g., what they find, timing, detection method). Explain why using both is recommended.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Inspection vs Testing — Complementary Techniques
>
> | Aspect | Inspection | Testing |
> |--------|------------|---------|
> | **Finds** | Static, localized faults | Dynamic, interaction faults |
> | **Detection** | Direct observation | Failure → trace to fault |
> | **Timing** | Early (requirements, design) | Later (code exists) |
> | **Hidden faults** | Can find (e.g., platform issues) | Won't trigger if untested |
> | **Cost** | Higher per-session | Higher for test creation |
>
> **Empirical guidance:** Use both! Studies show they find different defect populations.
>
> #### The Four Verification Techniques
>
> | Technique | Definition | Best For |
> |-----------|------------|----------|
> | **Inspection** | Human examination of artifacts | Faults of omission, style, early detection |
> | **Analysis** | Model-based evaluation without execution | Formal properties, concurrency, security |
> | **Testing** | Execution under controlled conditions | Dynamic behavior, integration issues |
> | **Demonstration** | Operation in real/production environment | User acceptance, performance validation |
>
> **Defense in Depth:** No single technique finds all defects. Combine them!

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/overview/RQ_L03_Verification.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/overview/RQ_L03_Verification.md)

### Card 026 — Question 4: Safety vs Liveness Properties

> [!question] Question
> **Question 4: Safety vs Liveness Properties**
>
> Static analysis can verify different types of properties.
>
> Define **safety properties** and **liveness properties**. Give one concrete software example of each type of property.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 🧰 **Uses of Static Analysis**
>
> The Static Analysis
>
> - Identifies:
>   - Style issues or unsafe coding practices (e.g., use of dangerous constructs).
>   - Security vulnerabilities (e.g., buffer overflows).
>   - Resource usage (e.g., excessive memory allocation).
> - Verifies:
>   - **Safety properties** (e.g., no crashes).
>   - **Liveness properties** (e.g., tasks complete).
>   - **Temporal properties** (e.g., real-time deadlines).
>
> #### What is Static Analysis?
>
> **INCOSE Definition:**
> > Verification method of determining performance or other properties from analytical evidence.
>
> **Types of Analysis:**
> - **Static Analysis:** Examining source code, bytecode, or binaries without execution
> - **Model Checking:** Exploring all states of a formal model exhaustively
> - **Theorem Proving:** Mathematical proof of properties
>
> **Key Insight:** Static analysis is **automated inspection**. Model checking is **exhaustive exploration**.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/overview/RQ_L03_Verification.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/overview/RQ_L03_Verification.md)

### Card 027 — Question 5: Rice's Theorem — Sound vs Complete

> [!question] Question
> **Question 5: Rice's Theorem — Sound vs Complete**
>
> Explain the trade-off between **soundness** and **completeness** in static analysis tools.
>
> What does Rice's Theorem tell us about the fundamental limitations of static analysis? How do commercial tools typically handle this trade-off?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 🔍 **Soundness vs. Completeness in Analysis**
>
> - **Sound Analysis**: Ensures no errors are missed but may include false positives.
> - **Complete Analysis**: Reports only real issues but might miss some defects.
>
> > **Key Insight**: No static analysis can achieve soundness, completeness, and termination simultaneously due to **Rice’s Theorem**.
>
> #### Rice's Theorem — Why No Tool Is Perfect
>
> **Terminology (confusion matrix):** In analysis tools, *positive* = "the tool reports a defect"; *negative* = "the tool says nothing to flag." Therefore:
> - **False positive (FP):** tool fires → no real bug (false alarm, noise)
> - **False negative (FN):** tool is silent → real bug exists (missed bug)
>
> Note: "positive" here does **not** mean "good outcome" — it simply means "the tool flagged something."
>
> **The Theorem:**
> > No analysis can be sound, complete, AND terminate on all programs.
>
> **The Trade-off:**
>
> | Property | Description | Consequence |
> |----------|-------------|-------------|
> | **Sound** | Finds ALL bugs of a type (FN = 0) | May report false positives (FP > 0) |
> | **Complete** | All reports are real bugs (FP = 0) | May miss some real bugs (FN > 0) |
>
> **Practical Implications:**
>
> | Tool Strategy | Focus |
> |---------------|-------|
> | Academic tools | Soundness (catch all) |
> | Commercial tools | Low false positives (usability) |
>
> **Commercial tools prioritize usability over soundness** — they accept some missed bugs to avoid overwhelming developers with false alarms.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/overview/RQ_L03_Verification.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/overview/RQ_L03_Verification.md)

### Card 028 — Question 6: Test Levels

> [!question] Question
> **Question 6: Test Levels**
>
> Describe the four test levels: Unit, Integration, System, and Acceptance.
>
> For each level, identify: (a) what is being tested, (b) who typically performs the testing, and (c) one example of a defect that would be found at that level.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Test Doubles — Isolation for Unit Testing
>
> | Type | Purpose |
> |------|---------|
> | **Stub** | Returns canned answers |
> | **Mock** | Verifies interactions |
> | **Fake** | Simplified implementation |
> | **Spy** | Records calls for later verification |
>
> **Why isolate?**
> - Fast execution (milliseconds)
> - Deterministic results
> - Test single unit of behavior
> - Pinpoint failures precisely
>
> **Key Insight:** Mocking isolates the unit under test. Otherwise you're doing integration testing.
>
> #### Test Levels
>
> | Level | Scope | Owner | Adequacy Criteria |
> |-------|-------|-------|-------------------|
> | **Unit** | Single function/method | Developer | Statement/branch coverage |
> | **Integration** | Component interactions | Dev/QA | Interface coverage |
> | **Thread/Function** | End-to-end workflow | QA | Path coverage |
> | **System** | Complete integrated system | QA/UAT | Requirements coverage |
>
> **V-Model alignment:** Unit ↔ Design, Integration ↔ Architecture, System ↔ Requirements

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/overview/RQ_L03_Verification.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/overview/RQ_L03_Verification.md)

### Card 029 — Question 7: Test Doubles

> [!question] Question
> **Question 7: Test Doubles**
>
> Unit testing often requires isolating the unit under test using test doubles.
>
> What is the role of mocks?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Test Doubles — Isolation for Unit Testing
>
> | Type | Purpose |
> |------|---------|
> | **Stub** | Returns canned answers |
> | **Mock** | Verifies interactions |
> | **Fake** | Simplified implementation |
> | **Spy** | Records calls for later verification |
>
> **Why isolate?**
> - Fast execution (milliseconds)
> - Deterministic results
> - Test single unit of behavior
> - Pinpoint failures precisely
>
> **Key Insight:** Mocking isolates the unit under test. Otherwise you're doing integration testing.
>
> #### What is Testing?
>
> **INCOSE Definition:**
> > Verification method by which a system or component is executed under specified conditions, outputs are observed, and evaluation is made.
>
> **Testing involves:**
> 1. **Inputs:** Prepared test data
> 2. **Execution:** Running the system
> 3. **Observation:** Recording actual outputs
> 4. **Evaluation:** Comparing to expected results (oracle)
>
> > "Testing can show the presence of bugs, but never their absence."
> > — Edsger Dijkstra
>
> **Key distinction:** Testing requires execution. Analysis does not.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/overview/RQ_L03_Verification.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/overview/RQ_L03_Verification.md)

### Card 030 — Question 8: Black Box vs White Box

> [!question] Question
> **Question 8: Black Box vs White Box**
>
> Compare **black box** testing and **white box** testing.
>
> For each approach, describe: (a) what knowledge the tester needs, (b) what types of defects it finds, and (c) one testing technique associated with it.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Black Box vs White Box Testing
>
> | Aspect | Black Box | White Box |
> |--------|-----------|-----------|
> | **Knowledge** | Specification only | Source code visible |
> | **Focus** | What it does | How it does it |
> | **Techniques** | Equivalence classes, boundary values | Statement, branch, path coverage |
> | **Who** | Tester (any) | Developer (code access) |
> | **Finds** | Missing features, wrong behavior | Dead code, untested paths |
>
> **Key Insight:** Black box tests the **contract**. White box tests the **implementation**. Both are needed.
>
> #### Black Box vs. White Box
>
> - **Black box**: Based on specifications, no knowledge of internals
> - **White box**: Based on code structure and implementation

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/overview/RQ_L03_Verification.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/overview/RQ_L03_Verification.md)

### Card 031 — Question 9: Google's Test Pyramid

> [!question] Question
> **Question 9: Google's Test Pyramid**
>
> Google recommends a test pyramid with a 70/20/10 ratio.
>
> What do these percentages represent? Explain **why** this ratio is recommended. What is the "ice cream cone" anti-pattern and why is it problematic?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Google's Test Pyramid — 70/20/10
>
> | Level | Name | Scope | Speed | Ratio |
> |-------|------|-------|-------|-------|
> | Base | Small (Unit) | Single function/class | Milliseconds | **70%** |
> | Middle | Medium (Integration) | 2+ modules | Seconds | **20%** |
> | Top | Large (E2E) | Entire system | Minutes | **10%** |
>
> **Google Scale:** 150M tests/day, 5.5M test targets, 1 commit/sec
>
> **Anti-pattern:** Ice cream cone (many UI tests, few unit tests) → slow, flaky, expensive
>
> #### Test Doubles — Isolation for Unit Testing
>
> | Type | Purpose |
> |------|---------|
> | **Stub** | Returns canned answers |
> | **Mock** | Verifies interactions |
> | **Fake** | Simplified implementation |
> | **Spy** | Records calls for later verification |
>
> **Why isolate?**
> - Fast execution (milliseconds)
> - Deterministic results
> - Test single unit of behavior
> - Pinpoint failures precisely
>
> **Key Insight:** Mocking isolates the unit under test. Otherwise you're doing integration testing.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/overview/RQ_L03_Verification.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/overview/RQ_L03_Verification.md)

### Card 032 — Question 10: Demonstration

> [!question] Question
> **Question 10: Demonstration**
>
> Define demonstration and explain when it is the **only** appropriate verification method. Give **two** examples of demonstration activities in software development.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### What is Demonstration?
>
> **INCOSE Definition:**
> > Verification method by which the system is observed during operation in its intended environment.
>
> **Key Insight:** Some properties can **only** be verified by demonstration. "Works on my machine" isn't sufficient.
>
> #### Verification and Validation Overview
>
> Software verification and validation (V&V) encompasses all activities that help ensure software quality through systematic examination and testing. This section provides a comprehensive overview of V&V techniques, their purposes, and when to apply them.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/overview/RQ_L03_Verification.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/overview/RQ_L03_Verification.md)

### Card 033 — Question 11: Defense in Depth

> [!question] Question
> **Question 11: Defense in Depth**
>
> Different verification techniques are suited to different quality characteristics.
>
> For the following quality characteristics, identify which verification technique(s) are most effective and explain why:
> - **Maintainability**
> - **Usability**
> - **Security**

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The Four Verification Techniques
>
> | Technique | Definition | Best For |
> |-----------|------------|----------|
> | **Inspection** | Human examination of artifacts | Faults of omission, style, early detection |
> | **Analysis** | Model-based evaluation without execution | Formal properties, concurrency, security |
> | **Testing** | Execution under controlled conditions | Dynamic behavior, integration issues |
> | **Demonstration** | Operation in real/production environment | User acceptance, performance validation |
>
> **Defense in Depth:** No single technique finds all defects. Combine them!
>
> #### 🛠️ **Techniques of Software Verification**
>
> 1. **Inspection**
> 2. **Analysis**
> 3. **Testing**
> 4. **Demonstration**
>
> Each technique addresses specific aspects of verification, and combining them ensures robust software quality.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/overview/RQ_L03_Verification.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/overview/RQ_L03_Verification.md)

## Adequacy Criteria (32)

### Card 034 — Question 1: Coverage Categories

> [!question] Question
> **Question 1: Coverage Categories**
>
> Match each coverage category with its focus area:
>
> | Category | Focus |
> |----------|-------|
> | A. White Box | 1. Input space |
> | B. Black Box | 2. Code structure |
> | C. Mutation | 3. Specification |
> | D. Requirements | 4. Fault detection |

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.2 Categories of Coverage Criteria
>
> | Category | Criteria | Focus | Code Needed? |
> |----------|----------|-------|--------------|
> | **White Box** | Statement, Branch, Path, MC/DC | Code structure | Yes |
> | **Black Box** | Equivalence, Boundary, Combinatorial | Input space | No |
> | **Mutation** | Mutation score | Fault detection | Yes |
> | **Requirements** | N-switch, State coverage | Specification | No |
>
> **Selection Factors:**
> - Purpose of testing (unit, integration, system)
> - Code availability (open source vs. compiled)
> - Targeted fault types
> - Compliance requirements (DO-178C, ISO 26262)
>
> > **Exam Tip:** Know which criteria require source code access (white box, mutation) vs. those that don't (black box, requirements-based).
>
> #### 6.3 What Actually Predicts Fault Detection?
>
> **Assertions > Coverage** :
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "width": 350,
>   "height": 150,
>   "title": {"text": "Correlation with Fault Detection Effectiveness", "subtitle": "Source: Zhang & Mesbah 2015"},
>   "data": {
>     "values": [
>       {"factor": "Assertion Count", "correlation": 0.95, "order": 1},
>       {"factor": "Test Count", "correlation": 0.65, "order": 2},
>       {"factor": "Statement Coverage", "correlation": 0.35, "order": 3}
>     ]
>   },
>   "mark": {"type": "bar", "cornerRadiusEnd": 4},
>   "encoding": {
>     "y": {"field": "factor", "type": "nominal", "sort": {"field": "order"}, "axis": {"title": null}},
>     "x": {"field": "correlation", "type": "quantitative", "title": "Correlation Coefficient", "scale": {"domain": [0, 1]}},
>     "color": {"condition": {"test": "datum.factor === 'Assertion Count'", "value": "#019546"}, "value": "#c8e6c9"}
>   },
>   "config": {"font": "Tahoma, sans-serif", "view": {"stroke": null}}
> }
> ```
>
> | Factor | Correlation with Effectiveness |
> |--------|-------------------------------|
> | **Assertion quantity** | **0.927 - 0.973** |
> | Statement coverage (alone) | Weak |
>
> > "The correlation between size and effectiveness is driven by assertions, not coverage."
>
> **What this means practically:**
> A test that executes 100 lines but checks nothing (no assertions) is almost worthless. A test that executes 10 lines but has strong assertions on the output is valuable. **Coverage measures exploration; assertions measure verification.**
>
> **Coverage Criteria Compared** :
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 035 — Question 2: Coverage Formula

> [!question] Question
> **Question 2: Coverage Formula**
>
> A test suite executes 45 out of 60 statements. What is the statement coverage?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.2 Statement Coverage (C0)
>
> **Definition:** Each statement must be executed at least once.
>
> **Formula:**
>
> $$\text{Statement Coverage} = \frac{\text{Statements Executed}}{\text{Total Statements}} \times 100\%$$
>
> **Example - The Hidden Bug:**
>
> ```python
> x = 0           # S1
> if A < 5:       # Decision
>     x = 4       # S2
> y = z / x       # S3 ← Potential division by zero!
> ```
>
> **Test: A = 3**
> - Executes: S1, S2, S3
> - Coverage: **100%** ✓
> - **Problem:** Misses `A >= 5` path where `x = 0` causes division by zero!
>
> **Why Statement Coverage Is Weak:**
>
> | Advantage | Disadvantage |
> |-----------|--------------|
> | Simple to measure | Insensitive to control flow |
> | Low test count | Misses branch-specific faults |
> | Easy to achieve | Ignores predicate structure |
>
> > **Key Rule:** Statement coverage is the **floor**, not the **ceiling**. Never rely on it alone!
>
> #### What is Test Coverage?
>
> **Test coverage** measures the degree to which source code, requirements, or design specifications are exercised by a test suite. It answers questions like:
> - Which parts of the code have been executed?
> - Which branches and paths have been taken?
> - Which requirements have been verified?
>
> Coverage serves two purposes:
> 1. **Generator** — create test cases by targeting untested elements
> 2. **Measure** — evaluate existing tests by computing what percentage of a criterion is covered
>
> **Key insight**: High coverage doesn't guarantee quality, but low coverage almost certainly indicates insufficient testing.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 036 — Question 3: Two Uses of Coverage

> [!question] Question
> **Question 3: Two Uses of Coverage**
>
> What are the two ways coverage criteria can be used? Explain each with an example.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.2 Categories of Coverage Criteria
>
> | Category | Criteria | Focus | Code Needed? |
> |----------|----------|-------|--------------|
> | **White Box** | Statement, Branch, Path, MC/DC | Code structure | Yes |
> | **Black Box** | Equivalence, Boundary, Combinatorial | Input space | No |
> | **Mutation** | Mutation score | Fault detection | Yes |
> | **Requirements** | N-switch, State coverage | Specification | No |
>
> **Selection Factors:**
> - Purpose of testing (unit, integration, system)
> - Code availability (open source vs. compiled)
> - Targeted fault types
> - Compliance requirements (DO-178C, ISO 26262)
>
> > **Exam Tip:** Know which criteria require source code access (white box, mutation) vs. those that don't (black box, requirements-based).
>
> #### Test Coverage Criteria
>
> How do you know when you've tested enough? Coverage criteria provide objective measures of test completeness by defining what portions of the software must be exercised by tests.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 037 — Question 4: Statement Coverage Weakness

> [!question] Question
> **Question 4: Statement Coverage Weakness**
>
> Consider this code:
>
> ```python
> x = 0
> if condition:
>     x = 4
> y = z / x
> ```
>
> A test with `condition=True` achieves 100% statement coverage. Why is this problematic?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.2 Statement Coverage (C0)
>
> **Definition:** Each statement must be executed at least once.
>
> **Formula:**
>
> $$\text{Statement Coverage} = \frac{\text{Statements Executed}}{\text{Total Statements}} \times 100\%$$
>
> **Example - The Hidden Bug:**
>
> ```python
> x = 0           # S1
> if A < 5:       # Decision
>     x = 4       # S2
> y = z / x       # S3 ← Potential division by zero!
> ```
>
> **Test: A = 3**
> - Executes: S1, S2, S3
> - Coverage: **100%** ✓
> - **Problem:** Misses `A >= 5` path where `x = 0` causes division by zero!
>
> **Why Statement Coverage Is Weak:**
>
> | Advantage | Disadvantage |
> |-----------|--------------|
> | Simple to measure | Insensitive to control flow |
> | Low test count | Misses branch-specific faults |
> | Easy to achieve | Ignores predicate structure |
>
> > **Key Rule:** Statement coverage is the **floor**, not the **ceiling**. Never rely on it alone!
>
> #### 4.1 Condition Coverage Types Compared
>
> | Coverage Type | Definition | Tests for `if (A && B)` |
> |---------------|------------|-------------------------|
> | **Basic Condition** | Each condition true/false once | 2: (T,T), (F,F) |
> | **Decision Coverage** | Each decision true/false | 2: (T,T), (F,any) |
> | **Condition/Decision** | Both above combined | 2-3 tests |
> | **Multiple Condition** | All combinations | 4: TT, TF, FT, FF |
> | **MC/DC** | Each condition independently affects outcome | 3: TT, TF, FT |
>
> **Multiple Condition Problem:** Exponential growth — $2^n$ test cases!
>
> | Conditions | Multiple Condition | MC/DC |
> |------------|-------------------|-------|
> | 2 | 4 | 3 |
> | 3 | 8 | 4 |
> | 4 | 16 | 5 |
> | n | $2^n$ | **n+1** |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 038 — Question 5: Branch vs Statement

> [!question] Question
> **Question 5: Branch vs Statement**
>
> How many tests are needed for 100% branch coverage on an `if-else` statement? How does this compare to statement coverage?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.1 Branch Coverage (C1)
>
> **Definition:** Each branch of every decision must be traversed at least once.
>
> **Formula:**
>
> $$\text{Branch Coverage} = \frac{\text{Branches Executed}}{\text{Total Branches}} \times 100\%$$
>
> **Example - Catching the Bug:**
>
> ```python
> x = 0
> if A < 5:      # 2 branches
>     x = 4
> y = z / x
> ```
>
> | Test | A | Path | Catches Bug? |
> |------|---|------|--------------|
> | T1 | 3 | True branch | No |
> | T2 | 6 | False branch | **Yes!** x=0 triggers error |
>
> > **Key Insight:** Branch coverage catches faults that statement coverage misses.
>
> #### 2.2 Statement Coverage (C0)
>
> **Definition:** Each statement must be executed at least once.
>
> **Formula:**
>
> $$\text{Statement Coverage} = \frac{\text{Statements Executed}}{\text{Total Statements}} \times 100\%$$
>
> **Example - The Hidden Bug:**
>
> ```python
> x = 0           # S1
> if A < 5:       # Decision
>     x = 4       # S2
> y = z / x       # S3 ← Potential division by zero!
> ```
>
> **Test: A = 3**
> - Executes: S1, S2, S3
> - Coverage: **100%** ✓
> - **Problem:** Misses `A >= 5` path where `x = 0` causes division by zero!
>
> **Why Statement Coverage Is Weak:**
>
> | Advantage | Disadvantage |
> |-----------|--------------|
> | Simple to measure | Insensitive to control flow |
> | Low test count | Misses branch-specific faults |
> | Easy to achieve | Ignores predicate structure |
>
> > **Key Rule:** Statement coverage is the **floor**, not the **ceiling**. Never rely on it alone!

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 039 — Question 6: Compound Predicate Problem

> [!question] Question
> **Question 6: Compound Predicate Problem**
>
> For `if (A && B)`, branch coverage requires only 2 tests. What combination is never tested, and why is this a problem?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.2 Branch Coverage Limitations
>
> **Problem:** Compound predicates `if (A && B)` — branch coverage needs only 2 tests:
>
> | Test | A | B | Outcome | Note |
> |------|---|---|---------|------|
> | T1 | true | true | True branch | ✓ |
> | T2 | false | any | False branch | Short-circuit! |
>
> **Missing:** `A=true, B=false` — never tested!
>
> **Fault Example:**
> ```python
> if A and B:    # Should be: A or B
>     x = 1
> ```
>
> The `AND` vs `OR` error remains **undetected**.
>
> #### 3.1 Branch Coverage (C1)
>
> **Definition:** Each branch of every decision must be traversed at least once.
>
> **Formula:**
>
> $$\text{Branch Coverage} = \frac{\text{Branches Executed}}{\text{Total Branches}} \times 100\%$$
>
> **Example - Catching the Bug:**
>
> ```python
> x = 0
> if A < 5:      # 2 branches
>     x = 4
> y = z / x
> ```
>
> | Test | A | Path | Catches Bug? |
> |------|---|------|--------------|
> | T1 | 3 | True branch | No |
> | T2 | 6 | False branch | **Yes!** x=0 triggers error |
>
> > **Key Insight:** Branch coverage catches faults that statement coverage misses.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 040 — Question 7: Cyclomatic Complexity Calculation

> [!question] Question
> **Question 7: Cyclomatic Complexity Calculation**
>
> A control flow graph has 10 edges and 8 nodes. Calculate $V(G)$.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.1 Control Flow Graph (CFG) Terminology
>
> | Term | Definition | Example |
> |------|------------|---------|
> | **Statement** | Single executable instruction | `x = x + 1` |
> | **Basic Block** | Sequence with single entry/exit | Multiple statements, no branches |
> | **Decision** | Point with multiple outcomes | `if`, `while`, `switch` |
> | **Condition** | Boolean sub-expression | `a > b` in `a > b && c == 1` |
> | **Branch** | Edge from decision to target | True/False paths |
> | **Path** | Sequence from entry to exit | Complete execution trace |
>
> **CFG Construction:**
> - **Nodes** = Basic blocks
> - **Edges** = Control flow transitions
> - **Entry/Exit** = Special start and end nodes
>
> **Example CFG: If-Then (no else)**
>
> ```python
> x = 0           # Block 1
> if A < 5:       # Decision (D)
>     x = 4       # Block 2 (True branch only)
> y = z / x       # Block 3 (merge point)
> ```
>
> ```mermaid
> flowchart TD
>     B1["x = 0"] --> D{"A < 5?"}
>     D -->|True| B2["x = 4"]
>     D -->|False| B3["y = z / x"]
>     B2 --> B3
>
>     style B1 fill:#f0f8f0,stroke:#019546
>     style D fill:#fff3cd,stroke:#2D6E2A
>     style B2 fill:#c8e6c9,stroke:#019546
>     style B3 fill:#019546,stroke:#2D6E2A,color:#fff
> ```
>
> **CFG Metrics:** Nodes=4, Edges=4, V(G) = 4 − 4 + 2 = **2**
>
> > **Note:** An if-then (no else) has **no empty node** on the false path — the false edge goes directly to the merge block. Adding a phantom "skip" node keeps V(G) the same (5−5+2=2) but is non-standard and risks a counting mismatch if the empty node is forgotten while counting edges.
>
> #### 3.3 Cyclomatic Complexity & Basis Path
>
> **Cyclomatic Complexity** :
>
> $$V(G) = E - N + 2$$
>
> Where:
> - E = Number of edges
> - N = Number of nodes
> - V(G) = Minimum number of independent paths
>
> **Alternative formula:** V(G) = D + 1 (where D = number of decisions)
>
> **Why McCabe Invented This:**
> McCabe observed that code with many decision points is harder to test and more error-prone. His metric gives:
> 1. **Upper bound** on tests needed for basis path coverage
> 2. **Complexity threshold** for refactoring (typically V(G) ≤ 10)
> 3. **Risk indicator** — high V(G) correlates with defects
>
> **Why Basis Path Instead of All Paths?**
>
> | Decisions | All-Path ($2^n$) | Basis Path (n+1) |
> |-----------|-----------------|------------------|
> | 2 | 4 | **3** |
> | 4 | 16 | **5** |
> | 8 | 256 | **9** |
> | 10 | 1,024 | **11** |
>
> All-path coverage is **exponential** — infeasible for real code.
>
> **Basis Path Advantages:**
> - **Linear** growth in test count
> - Covers all independent control flow paths
> - Covers every edge at least once
> - V(G) gives **upper bound** on required tests
>
> **Example: Binary Search CFG**
>
> ```python
> def binary_search(arr, target):
>     low, high = 0, len(arr) - 1
>     while low <= high:         # D1
>         mid = (low + high) // 2
>         if arr[mid] == target: # D2
>             return mid         # P1: found
>         elif arr[mid] < target: # D3
>             low = mid + 1      # P3: right
>         else:
>             high = mid - 1     # P2: left
>     return -1                  # P4: not found
> ```
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 041 — Question 8: Alternative Formula

> [!question] Question
> **Question 8: Alternative Formula**
>
> A function has 5 decision points (if, while, etc.). What is its cyclomatic complexity?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.3 Cyclomatic Complexity & Basis Path
>
> **Cyclomatic Complexity** :
>
> $$V(G) = E - N + 2$$
>
> Where:
> - E = Number of edges
> - N = Number of nodes
> - V(G) = Minimum number of independent paths
>
> **Alternative formula:** V(G) = D + 1 (where D = number of decisions)
>
> **Why McCabe Invented This:**
> McCabe observed that code with many decision points is harder to test and more error-prone. His metric gives:
> 1. **Upper bound** on tests needed for basis path coverage
> 2. **Complexity threshold** for refactoring (typically V(G) ≤ 10)
> 3. **Risk indicator** — high V(G) correlates with defects
>
> **Why Basis Path Instead of All Paths?**
>
> | Decisions | All-Path ($2^n$) | Basis Path (n+1) |
> |-----------|-----------------|------------------|
> | 2 | 4 | **3** |
> | 4 | 16 | **5** |
> | 8 | 256 | **9** |
> | 10 | 1,024 | **11** |
>
> All-path coverage is **exponential** — infeasible for real code.
>
> **Basis Path Advantages:**
> - **Linear** growth in test count
> - Covers all independent control flow paths
> - Covers every edge at least once
> - V(G) gives **upper bound** on required tests
>
> **Example: Binary Search CFG**
>
> ```python
> def binary_search(arr, target):
>     low, high = 0, len(arr) - 1
>     while low <= high:         # D1
>         mid = (low + high) // 2
>         if arr[mid] == target: # D2
>             return mid         # P1: found
>         elif arr[mid] < target: # D3
>             low = mid + 1      # P3: right
>         else:
>             high = mid - 1     # P2: left
>     return -1                  # P4: not found
> ```
>
> …
>
> #### Example 2 – Two Decision Points
>
> ```fortran
> input(x)
>
> if x > 0 then
>    if x < 10 then
>       y = 1
>    else
>       y = 2
>    end if
> else
>    y = -1
> end if
>
> print(y)
> ```
>
> **CFG:**
>
> ```mermaid
> flowchart TD
>   Start((Start))
>   D1{ x > 0 }
>   D2{ x < 10 }
>   S1[ y = 1 ]
>   S2[ y = 2 ]
>   S3[ y = -1 ]
>   P[ print y ]
>   End((End))
>
>   Start --> D1
>   D1 -->|true| D2
>   D1 -->|false| S3 --> P
>   D2 -->|true| S1 --> P
>   D2 -->|false| S2 --> P
>   P --> End
> ```
>
> **Cyclomatic Complexity:**
>
> $$
> V(G) = 8 - 7 + 2 = 3
> $$
>
> same with
>
> $$
> V(G) = 2+1 = 3
> $$
>
> **Basis Paths:**
>
> 1. `x > 0`, `x < 10` ⇒ `Start → D1(true) → D2(true) → S1 → P → End`
> 2. `x > 0`, `x ≥ 10` ⇒ `Start → D1(true) → D2(false) → S2 → P → End`
> 3. `x ≤ 0` ⇒ `Start → D1(false) → S3 → P → End`
>
> ✅ 3 test cases needed (e.g., `x = 5`, `x = 15`, `x = -2`)

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 042 — Question 9: Basis Path vs All Paths

> [!question] Question
> **Question 9: Basis Path vs All Paths**
>
> Why is basis path coverage preferred over all-path coverage? Complete this table:
>
> | Decisions | All Paths | Basis Paths |
> |-----------|-----------|-------------|
> | 4 | ? | ? |
> | 10 | ? | ? |

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Comparison: Basis Path vs All Path Coverage
>
> | Property            | Basis Path Coverage                           | All Path Coverage                                            |
> | ------------------- | --------------------------------------------- | ------------------------------------------------------------ |
> | **# of test cases** | Linear in number of decisions (n+1)         | Exponential: $$2^n$$ for n decisions                           |
> | **Goal**            | Cover all **edges** and **independent paths** | Cover **every possible execution path**                      |
> | **Feasibility**     | Practical                                     | Often infeasible (many paths may be redundant or untestable) |
> | **Redundancy**      | Minimal                                       | High (many paths may test the same logic repeatedly)         |
> | **Example (n=3)**   | \~4 tests                                     | 8 tests (if all paths feasible)                              |
>
> So, for **n decision points**, Basis Path typically requires only $$n + 1$$ test cases, while All Path Coverage requires $$2^n$$ — which grows very quickly.
>
> #### Basis Path Coverage
>
> {: .highlight }
> Basis Path coverage is a practical alternative when All Path coverage requires too many test cases (almost everytime).

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 043 — Question 10: Unfeasible Paths

> [!question] Question
> **Question 10: Unfeasible Paths**
>
> What is an unfeasible path? Give an example.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.4 Unfeasible Paths
>
> **Problem:** Semantic dependencies prevent execution of some paths.
>
> ```python
> if x > 0:
>     y = 1
> if x > 0:     # Same condition!
>     z = y + 1
> ```
>
> **Impossible Path:** `x > 0` → `y = 1` → `x ≤ 0` → skip z
>
> The CFG shows 4 possible paths, but only 2 are actually executable:
> - `x > 0`: Execute both if-blocks
> - `x ≤ 0`: Skip both if-blocks
>
> The paths where the first condition is true but the second is false (or vice versa) are **semantically impossible** because `x` doesn't change between checks.
>
> **Real-World Example - Login System:**
>
> ```python
> is_valid = validate_password(password)
> if is_valid:
>     log_success()
> if not is_valid:  # Mutually exclusive with above
>     log_failure()
> ```
>
> CFG shows 4 paths, but only 2 are feasible. You can never execute both `log_success()` AND `log_failure()` in the same run.
>
> **Practical Rule:** Target 85-90% path coverage; remaining may be unfeasible.
>
> #### Unfeasible Paths
>
> Some paths **can’t be executed** due to **semantic constraints**, even though they appear valid in the CFG.
>
> #### Example:
>
> ```mermaid
> flowchart TD
>     Start((Start))
>     A{Condition A?}
>     B[Block S1]
>     C[Block S2]
>     D{Condition A again?}
>     E[Block S3]
>     F[Block S4]
>     End((End))
>
>     Start --> A
>     A -->|True| B --> D
>     A -->|False| C --> D
>     D -->|True| E --> End
>     D -->|False| F --> End
>
>     style A fill:#ffdddd,stroke:#ff0000
>     style D fill:#ffdddd,stroke:#ff0000
> ```
>
> Here, Condition A is checked **twice**, making some path combinations logically impossible (e.g., A true first, then false later).

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 044 — Question 11: Condition Coverage Test Count

> [!question] Question
> **Question 11: Condition Coverage Test Count**
>
> For predicate `if (A && B)`, how many tests does each coverage type require?
>
> | Coverage Type | Tests Required |
> |---------------|----------------|
> | Basic Condition | ? |
> | Multiple Condition | ? |
> | MC/DC | ? |

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.1 Condition Coverage Types Compared
>
> | Coverage Type | Definition | Tests for `if (A && B)` |
> |---------------|------------|-------------------------|
> | **Basic Condition** | Each condition true/false once | 2: (T,T), (F,F) |
> | **Decision Coverage** | Each decision true/false | 2: (T,T), (F,any) |
> | **Condition/Decision** | Both above combined | 2-3 tests |
> | **Multiple Condition** | All combinations | 4: TT, TF, FT, FF |
> | **MC/DC** | Each condition independently affects outcome | 3: TT, TF, FT |
>
> **Multiple Condition Problem:** Exponential growth — $2^n$ test cases!
>
> | Conditions | Multiple Condition | MC/DC |
> |------------|-------------------|-------|
> | 2 | 4 | 3 |
> | 3 | 8 | 4 |
> | 4 | 16 | 5 |
> | n | $2^n$ | **n+1** |
>
> #### Test Coverage Criteria
>
> How do you know when you've tested enough? Coverage criteria provide objective measures of test completeness by defining what portions of the software must be exercised by tests.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 045 — Question 12: MC/DC Requirements

> [!question] Question
> **Question 12: MC/DC Requirements**
>
> What are the three requirements for MC/DC coverage?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.2 Categories of Coverage Criteria
>
> | Category | Criteria | Focus | Code Needed? |
> |----------|----------|-------|--------------|
> | **White Box** | Statement, Branch, Path, MC/DC | Code structure | Yes |
> | **Black Box** | Equivalence, Boundary, Combinatorial | Input space | No |
> | **Mutation** | Mutation score | Fault detection | Yes |
> | **Requirements** | N-switch, State coverage | Specification | No |
>
> **Selection Factors:**
> - Purpose of testing (unit, integration, system)
> - Code availability (open source vs. compiled)
> - Targeted fault types
> - Compliance requirements (DO-178C, ISO 26262)
>
> > **Exam Tip:** Know which criteria require source code access (white box, mutation) vs. those that don't (black box, requirements-based).
>
> #### 1.3 Industry Coverage Gates
>
> **Google Test Certified Program** :
>
> | Level | Total Coverage | Small Tests | Requirements |
> |-------|----------------|-------------|--------------|
> | L2 | 50% incremental | 10% | Continuous build |
> | L4 | 40% | 25% | No red tests at release |
> | **L5** | **60%** | **40%** | All code reviewed |
>
> **Microsoft Milestone Gates** :
>
> | Stage | Coverage Requirement |
> |-------|---------------------|
> | Pre-submit | **80%** for new features |
> | Milestone 2 | 65% |
> | Milestone 3 | 70% |
>
> > **Key Insight:** Even Google acknowledges: 100% coverage ≠ no bugs.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 046 — Question 13: MC/DC Test Count

> [!question] Question
> **Question 13: MC/DC Test Count**
>
> How many tests are needed for MC/DC coverage of a predicate with 5 conditions? Compare to Multiple Condition coverage ($2^5$).

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### [Condition Coverage](conditions.md)
>
> Fine-grained condition testing: **multiple condition coverage** and **MC/DC** for safety-critical systems (DO-178C).
>
> #### 4.1 Condition Coverage Types Compared
>
> | Coverage Type | Definition | Tests for `if (A && B)` |
> |---------------|------------|-------------------------|
> | **Basic Condition** | Each condition true/false once | 2: (T,T), (F,F) |
> | **Decision Coverage** | Each decision true/false | 2: (T,T), (F,any) |
> | **Condition/Decision** | Both above combined | 2-3 tests |
> | **Multiple Condition** | All combinations | 4: TT, TF, FT, FF |
> | **MC/DC** | Each condition independently affects outcome | 3: TT, TF, FT |
>
> **Multiple Condition Problem:** Exponential growth — $2^n$ test cases!
>
> | Conditions | Multiple Condition | MC/DC |
> |------------|-------------------|-------|
> | 2 | 4 | 3 |
> | 3 | 8 | 4 |
> | 4 | 16 | 5 |
> | n | $2^n$ | **n+1** |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 047 — Question 14: MC/DC Independence Pairs

> [!question] Question
> **Question 14: MC/DC Independence Pairs**
>
> For `if (A && B && C)`, construct a minimal MC/DC test suite showing which pairs demonstrate each condition's independence.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Test Suite:
>
> ```text
> { (A=T, B=T), (A=F, B=F) }
> ```
>
> - **Branch coverage**: 100%
>
> - **Basis path coverage**: 100%
>
> - ❌ **Fails to detect the bug**
>
>
> **Why?**
> Because the compound predicate uses multiple conditions (`A` and `B`), but the test cases don’t independently evaluate each one. We need **Multiple Condition Coverage** or **MC/DC** to reveal such faults.
>
> #### 1.1 What is Test Adequacy?
>
> **The Core Question:**
> > "How do you know when you've tested enough?"
>
> Test adequacy criteria provide objective measures of test suite completeness. Coverage metrics answer: *What portion of the testable elements have been exercised?*
>
> **Real-World Example - The Therac-25 Disaster:**
> The Therac-25 radiation therapy machine killed three patients and injured three others (1985-1987). Post-mortem analysis revealed that testing focused on "normal" operation paths. The fatal race condition only occurred when operators typed commands rapidly—a path never exercised during testing. Better path coverage might have revealed the deadly bug.
>
> **Why Adequacy Matters:**
> - **Without criteria:** Testing stops when time/budget runs out
> - **With criteria:** Testing stops when measurable goals are met
> - **The gap:** What you test vs. what could fail
>
> **Two Uses of Coverage:**
>
> | Use | Purpose | Example |
> |-----|---------|---------|
> | **Generator** | Create tests to satisfy criterion | Write tests until 80% branch coverage |
> | **Measure** | Evaluate existing tests | Report current coverage percentage |
>
> **The Coverage Formula:**
>
> $$\text{Coverage} = \frac{\text{Measured Items Executed}}{\text{Total Measured Items}} \times 100\%$$
>
> **Concrete Example:**
> ```python
> def grade(score):          # Line 1
>     if score >= 90:        # Line 2 (decision)
>         return "A"         # Line 3
>     elif score >= 70:      # Line 4 (decision)
>         return "B"         # Line 5
>     else:                  # Line 6
>         return "C"         # Line 7
> ```
>
> | Test | Input | Statements Hit | Coverage |
> |------|-------|----------------|----------|
> | T1 | 95 | 1,2,3 | 3/7 = 43% |
> | T1+T2 | 95, 75 | 1,2,3,4,5 | 5/7 = 71% |
> | T1+T2+T3 | 95, 75, 50 | All 7 | 7/7 = 100% |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 048 — Question 15: MC/DC Standards

> [!question] Question
> **Question 15: MC/DC Standards**
>
> Which safety-critical standards require or recommend MC/DC? Match standard to domain:
>
> | Standard | Domain |
> |----------|--------|
> | DO-178C | ? |
> | ISO 26262 | ? |
> | IEC 62304 | ? |

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.3 MC/DC in Safety-Critical Standards
>
> | Standard | Domain | Requirement |
> |----------|--------|-------------|
> | **DO-178C** | Aerospace | Level A requires MC/DC |
> | **ISO 26262** | Automotive | Recommends MC/DC for ASIL D |
> | **IEC 62304** | Medical | Considers MC/DC for Class C |
>
> **Advantages:**
> - Strong fault detection capability
> - Linear test growth (n+1)
> - Catches masking in compound predicates
>
> **Challenges:**
> - Manual generation is laborious
> - Requires tool support
> - Some combinations may be infeasible
>
> > **Exam Tip:** Know the n+1 formula for MC/DC and be able to construct independence pairs.
>
> #### 1.2 Categories of Coverage Criteria
>
> | Category | Criteria | Focus | Code Needed? |
> |----------|----------|-------|--------------|
> | **White Box** | Statement, Branch, Path, MC/DC | Code structure | Yes |
> | **Black Box** | Equivalence, Boundary, Combinatorial | Input space | No |
> | **Mutation** | Mutation score | Fault detection | Yes |
> | **Requirements** | N-switch, State coverage | Specification | No |
>
> **Selection Factors:**
> - Purpose of testing (unit, integration, system)
> - Code availability (open source vs. compiled)
> - Targeted fault types
> - Compliance requirements (DO-178C, ISO 26262)
>
> > **Exam Tip:** Know which criteria require source code access (white box, mutation) vs. those that don't (black box, requirements-based).

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 049 — Question 16: Mutation Score

> [!question] Question
> **Question 16: Mutation Score**
>
> A test suite kills 72 mutants out of 100 total. 10 are equivalent mutants. What is the mutation score?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Mutation Score Workflow
>
> ```mermaid
> flowchart TD
>     A[/System Under Test - SUT/]:::sut --> B(Create Mutants):::process
>     B -- Apply mutation operators --> C[/Mutant SUTs/]:::mutant
>     D[/Test Suite/]:::test --> E(Execute Tests):::process
>     C --> E
>     E --> F{Mutant Fails Any Test?}:::decision
>     F -- Yes --> G[Mutant Killed]:::killed
>     G --> H(Increment KilledMutants):::process
>     F -- No --> I(Check Equivalence):::decision
>     I -- Not Equivalent --> J[Mutant Survives]:::survive
>     I -- Equivalent --> K(Remove from Total Count):::equiv
>     H & K --> L(Calculate Mutation Score):::score
>
>     %% Styles
>     classDef sut fill:#b3e5fc,stroke:#0277bd,stroke-width:2px;
>     classDef test fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px;
>     classDef mutant fill:#fce4ec,stroke:#ad1457,stroke-width:2px;
>     classDef process fill:#fff9c4,stroke:#f9a825,stroke-width:2px;
>     classDef decision fill:#ffe0b2,stroke:#ef6c00,stroke-width:2px;
>     classDef killed fill:#ffcdd2,stroke:#c62828,stroke-width:2px;
>     classDef survive fill:#d1c4e9,stroke:#4527a0,stroke-width:2px;
>     classDef equiv fill:#e0e0e0,stroke:#616161,stroke-width:2px;
>     classDef score fill:#dcedc8,stroke:#558b2f,stroke-width:2px;
>
> ```
>
> #### Equivalent Mutants
>
> Some mutants may be **equivalent** to the original—they result in the **same behavior** despite being syntactically different.
> **These mutants cannot be killed by any test.**
>
> {: .important }
> 🧠 _Understanding equivalence is crucial during analysis!_

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 050 — Question 17: Mutation Operators

> [!question] Question
> **Question 17: Mutation Operators**
>
> Name five categories of mutation operators and give an example of each.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.2 Mutation Operators
>
> | Category | Operator | Example |
> |----------|----------|---------|
> | **Arithmetic** | Replace + with - | `a + b` → `a - b` |
> | **Relational** | Replace < with <= | `x < 5` → `x <= 5` |
> | **Logical** | Replace && with \|\| | `A && B` → `A \|\| B` |
> | **Constant** | Change value | `x = 0` → `x = 1` |
> | **Statement** | Delete statement | `x++` → (removed) |
>
> > **Key Insight:** If a mutant survives, you need better tests!
>
> #### Mutation Operators
>
> Mutants are created by making small changes to the original program. Common types include:

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 051 — Question 18: Pairwise Testing

> [!question] Question
> **Question 18: Pairwise Testing**
>
> 4 parameters x 3 values each = 81 exhaustive combinations. How many tests does pairwise testing typically require? Why is this sufficient?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Combinatorial Testing
>
> **Problem:** Too many input combinations to test exhaustively.
>
> **Example:** 4 parameters × 3 values each = $3^4$ = **81 combinations**
>
> **Pairwise (2-way) Testing:**
> Cover all pairs of parameter values.
>
> | Test | Browser | OS | Screen | Theme |
> |------|---------|-----|--------|-------|
> | 1 | Chrome | Win | Desktop | Light |
> | 2 | Chrome | Mac | Mobile | Dark |
> | 3 | Firefox | Win | Mobile | Dark |
> | 4 | Firefox | Mac | Desktop | Light |
>
> **Result:** ~9 tests instead of 81
>
> **Research shows:** Most bugs involve ≤ 2-way interactions.
>
> **Tools:** ACTS (NIST), Pairwise.org generators
>
> #### 5.1 Mutation Testing
>
> **The Core Idea:**
> If your tests are good, they should detect small changes (mutations) to the code. If a mutant "survives" (tests still pass), your tests aren't checking something important.
>
> **Process:**
> 1. **Create mutants:** Inject small faults into code
> 2. **Execute tests:** Run test suite against each mutant
> 3. **Classify results:**
>    - **Killed:** Test fails → Good!
>    - **Survived:** Test passes → Test suite weak
>    - **Equivalent:** Mutant behaves identically → Exclude
>
> **Concrete Example:**
>
> ```python

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 052 — Question 19: N-Switch Coverage

> [!question] Question
> **Question 19: N-Switch Coverage**
>
> What is the difference between 0-switch, 1-switch, and 2-switch coverage?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.4 N-Switch State Coverage
>
> **Definition:** Cover all sequences of N state transitions.
>
> | N | Coverage | Tests |
> |---|----------|-------|
> | 0-switch | All states | Few |
> | 1-switch | All transitions | Moderate |
> | 2-switch | All transition pairs | Many |
>
> **Use for:** Protocol testing, UI workflows, embedded systems
>
> #### 1.2 Categories of Coverage Criteria
>
> | Category | Criteria | Focus | Code Needed? |
> |----------|----------|-------|--------------|
> | **White Box** | Statement, Branch, Path, MC/DC | Code structure | Yes |
> | **Black Box** | Equivalence, Boundary, Combinatorial | Input space | No |
> | **Mutation** | Mutation score | Fault detection | Yes |
> | **Requirements** | N-switch, State coverage | Specification | No |
>
> **Selection Factors:**
> - Purpose of testing (unit, integration, system)
> - Code availability (open source vs. compiled)
> - Targeted fault types
> - Compliance requirements (DO-178C, ISO 26262)
>
> > **Exam Tip:** Know which criteria require source code access (white box, mutation) vs. those that don't (black box, requirements-based).

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 053 — Question 20: Coverage Limitations

> [!question] Question
> **Question 20: Coverage Limitations**
>
> What does coverage measure, and what does it NOT measure? Complete the table:
>
> | Coverage Measures | Does NOT Measure |
> |-------------------|------------------|
> | ? | Oracle correctness |
> | ? | Missing code |
> | ? | Requirements coverage |

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.2 Branch Coverage Limitations
>
> **Problem:** Compound predicates `if (A && B)` — branch coverage needs only 2 tests:
>
> | Test | A | B | Outcome | Note |
> |------|---|---|---------|------|
> | T1 | true | true | True branch | ✓ |
> | T2 | false | any | False branch | Short-circuit! |
>
> **Missing:** `A=true, B=false` — never tested!
>
> **Fault Example:**
> ```python
> if A and B:    # Should be: A or B
>     x = 1
> ```
>
> The `AND` vs `OR` error remains **undetected**.
>
> #### What is Test Coverage?
>
> **Test coverage** measures the degree to which source code, requirements, or design specifications are exercised by a test suite. It answers questions like:
> - Which parts of the code have been executed?
> - Which branches and paths have been taken?
> - Which requirements have been verified?
>
> Coverage serves two purposes:
> 1. **Generator** — create test cases by targeting untested elements
> 2. **Measure** — evaluate existing tests by computing what percentage of a criterion is covered
>
> **Key insight**: High coverage doesn't guarantee quality, but low coverage almost certainly indicates insufficient testing.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 054 — Question 21: Size Confounding

> [!question] Question
> **Question 21: Size Confounding**
>
> Inozemtseva & Holmes (2014) found that coverage-effectiveness correlation drops to ~0 when controlling for what variable? What percentage of the coverage effect does test suite size explain?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The Size Confounding Problem
>
> *Reference: Inozemtseva & Holmes 2014 (ICSE Landmark)*
>
> The most important finding of the past decade:
>
> > "Coverage is NOT strongly correlated with test suite effectiveness when the size of the test suite is controlled for."
>
> | Condition | Correlation |
> |-----------|-------------|
> | Size ignored | 0.79 - 0.95 (appears strong) |
> | **Size controlled** | **~0** (essentially none) |
>
> **What this means:** The perceived correlation between coverage and fault detection is largely an artifact of test suite size. Larger suites have both higher coverage AND find more faults—but coverage isn't the cause.
>
> Lu et al. (2025)  quantified this effect:
> - Statement coverage: **69%** of observed effect explained by size
> - Branch coverage: **81.9%** explained by size
>
> #### 6.2 The Size Confounding Problem
>
> **Landmark Finding** :
>
> > "Coverage is NOT strongly correlated with test suite effectiveness when size is controlled."
>
> | Condition | Correlation |
> |-----------|-------------|
> | Size ignored | 0.79 - 0.95 (appears strong) |
> | **Size controlled** | **~0** (essentially none) |
>
> **Lu et al. 2025**  quantified:
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "width": 350,
>   "height": 200,
>   "title": {"text": "How Much of Coverage Effect is Actually Test Suite Size?", "subtitle": "Source: Lu et al. 2025"},
>   "data": {
>     "values": [
>       {"metric": "Statement Coverage", "size_effect": 69, "independent_effect": 31},
>       {"metric": "Branch Coverage", "size_effect": 81.9, "independent_effect": 18.1}
>     ]
>   },
>   "transform": [
>     {"fold": ["size_effect", "independent_effect"], "as": ["component", "value"]}
>   ],
>   "mark": {"type": "bar"},
>   "encoding": {
>     "y": {"field": "metric", "type": "nominal", "axis": {"title": null}},
>     "x": {"field": "value", "type": "quantitative", "title": "% of Correlation", "stack": "normalize", "axis": {"format": ".0%"}},
>     "color": {"field": "component", "type": "nominal", "scale": {"range": ["#d32f2f", "#019546"]}, "legend": {"title": null, "labelExpr": "datum.value === 'size_effect' ? 'Explained by Size' : 'Independent Effect'"}}
>   },
>   "config": {"font": "Tahoma, sans-serif", "view": {"stroke": null}}
> }
> ```
>
> | Metric | % Explained by Size |
> |--------|---------------------|
> | Statement Coverage | **69%** |
> | Branch Coverage | **81.9%** |
>
> **The Hidden Variable:**
> More tests → Higher coverage AND more faults found (Correlation, not causation!)
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 055 — Question 22: Assertions vs Coverage

> [!question] Question
> **Question 22: Assertions vs Coverage**
>
> According to Zhang & Mesbah (2015), what has a stronger correlation with test effectiveness: coverage or assertion quantity?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Assertions Matter More Than Coverage
>
> *Reference: Zhang & Mesbah 2015*
>
> | Factor | Correlation with Effectiveness |
> |--------|-------------------------------|
> | **Assertion quantity** | **0.927 - 0.973** |
> | Statement coverage (alone) | Weak when assertions controlled |
>
> > "The strong correlation often observed between test suite size and effectiveness is actually driven by the number and quality of assertions within those tests."
>
> **Practical implication:** Focus on assertion quality, not just coverage percentage. A test that executes code without checking results provides false confidence.
>
> #### 6.3 What Actually Predicts Fault Detection?
>
> **Assertions > Coverage** :
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "width": 350,
>   "height": 150,
>   "title": {"text": "Correlation with Fault Detection Effectiveness", "subtitle": "Source: Zhang & Mesbah 2015"},
>   "data": {
>     "values": [
>       {"factor": "Assertion Count", "correlation": 0.95, "order": 1},
>       {"factor": "Test Count", "correlation": 0.65, "order": 2},
>       {"factor": "Statement Coverage", "correlation": 0.35, "order": 3}
>     ]
>   },
>   "mark": {"type": "bar", "cornerRadiusEnd": 4},
>   "encoding": {
>     "y": {"field": "factor", "type": "nominal", "sort": {"field": "order"}, "axis": {"title": null}},
>     "x": {"field": "correlation", "type": "quantitative", "title": "Correlation Coefficient", "scale": {"domain": [0, 1]}},
>     "color": {"condition": {"test": "datum.factor === 'Assertion Count'", "value": "#019546"}, "value": "#c8e6c9"}
>   },
>   "config": {"font": "Tahoma, sans-serif", "view": {"stroke": null}}
> }
> ```
>
> | Factor | Correlation with Effectiveness |
> |--------|-------------------------------|
> | **Assertion quantity** | **0.927 - 0.973** |
> | Statement coverage (alone) | Weak |
>
> > "The correlation between size and effectiveness is driven by assertions, not coverage."
>
> **What this means practically:**
> A test that executes 100 lines but checks nothing (no assertions) is almost worthless. A test that executes 10 lines but has strong assertions on the output is valuable. **Coverage measures exploration; assertions measure verification.**
>
> **Coverage Criteria Compared** :
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 056 — Question 23: Coverage Criteria Effectiveness

> [!question] Question
> **Question 23: Coverage Criteria Effectiveness**
>
> According to Hemmati (2015), what percentage of faults does statement coverage detect? What about data-flow coverage?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Data-Flow Coverage Outperforms Control-Flow
>
> *Reference: Hemmati 2015*
>
> Empirical study on 274 real-world faults from Defects4J:
>
> | Criterion | Faults Detected |
> |-----------|-----------------|
> | Statement Coverage | **10%** |
> | Branch Coverage | 19% |
> | MC/DC | 19% |
> | All control-flow combined | 28% |
> | **+ Data-flow (def-use pairs)** | **85%** |
>
> **Key finding:** Statement coverage misses **90%** of real faults. Adding data-flow coverage detects an additional **79%** of faults that control-flow criteria miss entirely.
>
> See [Data-Flow Coverage](data-flow.md) for details on DU pairs and coverage criteria.
>
> #### 1.2 Categories of Coverage Criteria
>
> | Category | Criteria | Focus | Code Needed? |
> |----------|----------|-------|--------------|
> | **White Box** | Statement, Branch, Path, MC/DC | Code structure | Yes |
> | **Black Box** | Equivalence, Boundary, Combinatorial | Input space | No |
> | **Mutation** | Mutation score | Fault detection | Yes |
> | **Requirements** | N-switch, State coverage | Specification | No |
>
> **Selection Factors:**
> - Purpose of testing (unit, integration, system)
> - Code availability (open source vs. compiled)
> - Targeted fault types
> - Compliance requirements (DO-178C, ISO 26262)
>
> > **Exam Tip:** Know which criteria require source code access (white box, mutation) vs. those that don't (black box, requirements-based).

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 057 — Question 24: Coverage Anti-Patterns

> [!question] Question
> **Question 24: Coverage Anti-Patterns**
>
> List three coverage anti-patterns and explain why each is problematic.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 6.4 Coverage Anti-Patterns
>
> | Anti-Pattern | Problem |
> |--------------|---------|
> | Tests designed FOR coverage | Uniformly weak test suite |
> | Quick tests to satisfy tool | Misses faults of omission |
> | 85% as shipping gate | People cluster at threshold |
> | Ignoring low coverage | Missing the process signal |
>
> **Example of "Gaming Coverage":**
>
> ```python
>
> #### Coverage Anti-Patterns: Clues, Not Commands
>
> *Reference: Brian Marick, "How to Misuse Code Coverage", 1997*
>
> Marick identified fundamental limitations and misuses of coverage that remain relevant today.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 058 — Question 25: Coverage Level Selection

> [!question] Question
> **Question 25: Coverage Level Selection**
>
> Match each context with the appropriate coverage criterion:
>
> | Context | Criterion |
> |---------|-----------|
> | A. Minimum bar for any code | 1. MC/DC |
> | B. Default for unit tests | 2. Statement |
> | C. Safety-critical (DO-178C Level A) | 3. Branch |
> | D. Complex control flow | 4. Basis Path |

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 7.1 Choosing the Right Coverage Level
>
> | Criterion | Strength | Tests | Use When |
> |-----------|----------|-------|----------|
> | Statement (C0) | Weak | Low | Minimum bar |
> | Branch (C1) | Moderate | ~2×D | Default |
> | Basis Path | Good | V(G) | Complex flow |
> | MC/DC | Strong | n+1 | Safety-critical |
> | All Paths | Exhaustive | $2^n$ | Infeasible |
>
> #### Beyond Statement, Branch, and Path
>
> These criteria cover the foundational structural measures. For deeper coverage of specific criteria, see:
>
> - [Basis Path Testing](basis.md) — Cyclomatic complexity and independent paths
> - [Multiple Conditions & MC/DC](conditions.md) — Compound predicate coverage for safety-critical systems
> - [Data Flow Coverage](data-flow.md) — Definition-Use pairs and variable lifecycle testing
> - [Mutation Testing](mutation.md) — Measuring test effectiveness through fault injection

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 059 — Question 26: Coverage Targets

> [!question] Question
> **Question 26: Coverage Targets**
>
> What are the recommended minimum and target coverage levels?
>
> | Coverage | Min | Target |
> |----------|-----|--------|
> | Statement | ? | ? |
> | Branch | ? | ? |
> | Mutation | ? | ? |

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 7.2 Recommended Targets
>
> | Coverage | Min | Target | Note |
> |----------|-----|--------|------|
> | Statement | 70% | 80% | Diminishing >90% |
> | Branch | 75% | 85% | Good balance |
> | MC/DC | 100%* | 100%* | *Safety-critical |
> | Mutation | 60% | 80% | Expensive >80% |
>
> #### 3.1 Branch Coverage (C1)
>
> **Definition:** Each branch of every decision must be traversed at least once.
>
> **Formula:**
>
> $$\text{Branch Coverage} = \frac{\text{Branches Executed}}{\text{Total Branches}} \times 100\%$$
>
> **Example - Catching the Bug:**
>
> ```python
> x = 0
> if A < 5:      # 2 branches
>     x = 4
> y = z / x
> ```
>
> | Test | A | Path | Catches Bug? |
> |------|---|------|--------------|
> | T1 | 3 | True branch | No |
> | T2 | 6 | False branch | **Yes!** x=0 triggers error |
>
> > **Key Insight:** Branch coverage catches faults that statement coverage misses.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 060 — Question 27: Tool Matching

> [!question] Question
> **Question 27: Tool Matching**
>
> Match the coverage tool to its language:
>
> | Tool | Language |
> |------|----------|
> | A. JaCoCo | 1. Python |
> | B. Coverage.py | 2. Java |
> | C. LLVM-cov | 3. JavaScript |
> | D. c8 | 4. C/C++ |

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 7.3 Coverage Tools by Language
>
> | Language | Tool | Coverage Types |
> |----------|------|----------------|
> | Java | **JaCoCo** | Stmt, Branch, Line, Method, Complexity |
> | Python | **Coverage.py** | Stmt, Branch |
> | C/C++ | **LLVM-cov**, gcov | Stmt, Branch |
> | C# | **Coverlet**, dotCover | Stmt, Branch |
> | JavaScript/TS | **c8**, Vitest | Stmt, Branch, Func |
> | Go | `go test -cover` | Stmt |
> | Rust | **cargo-llvm-cov** | Stmt, Branch |
>
> **Integration Pipeline:** IDE plugins → Pre-commit hooks → CI/CD gates → PR comments
>
> #### Coverage Tool Support
>
> | Language | Tools |
> |----------|-------|
> | **Java** | JaCoCo, Cobertura, Clover |
> | **Python** | Coverage.py, pytest-cov |
> | **JavaScript** | Istanbul, NYC, c8 |
> | **C/C++** | gcov, lcov, OpenCppCoverage |
> | **C#** | dotCover, OpenCover, Coverlet |
> | **Go** | go test -cover |
>
> **Integration:** CI/CD pipelines, IDE visualization, code review reports (SonarQube, Codecov).

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 061 — Question 28: Oracle Problem

> [!question] Question
> **Question 28: Oracle Problem**
>
> What is the oracle problem in software testing? What are some mitigations?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Combinatorial Testing
>
> **Problem:** Too many input combinations to test exhaustively.
>
> **Example:** 4 parameters × 3 values each = $3^4$ = **81 combinations**
>
> **Pairwise (2-way) Testing:**
> Cover all pairs of parameter values.
>
> | Test | Browser | OS | Screen | Theme |
> |------|---------|-----|--------|-------|
> | 1 | Chrome | Win | Desktop | Light |
> | 2 | Chrome | Mac | Mobile | Dark |
> | 3 | Firefox | Win | Mobile | Dark |
> | 4 | Firefox | Mac | Desktop | Light |
>
> **Result:** ~9 tests instead of 81
>
> **Research shows:** Most bugs involve ≤ 2-way interactions.
>
> **Tools:** ACTS (NIST), Pairwise.org generators
>
> #### [Basis Path Testing](basis.md)
>
> Cyclomatic complexity-based testing: calculating V(G), deriving independent paths, McCabe's method with 3 worked examples.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 062 — Question 29: Branch Coverage and Mutation Relation

> [!question] Question
> **Question 29: Branch Coverage and Mutation Relation**
>
> What is the relationship between branch coverage and mutation testing? Does one subsume the other?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.1 Branch Coverage (C1)
>
> **Definition:** Each branch of every decision must be traversed at least once.
>
> **Formula:**
>
> $$\text{Branch Coverage} = \frac{\text{Branches Executed}}{\text{Total Branches}} \times 100\%$$
>
> **Example - Catching the Bug:**
>
> ```python
> x = 0
> if A < 5:      # 2 branches
>     x = 4
> y = z / x
> ```
>
> | Test | A | Path | Catches Bug? |
> |------|---|------|--------------|
> | T1 | 3 | True branch | No |
> | T2 | 6 | False branch | **Yes!** x=0 triggers error |
>
> > **Key Insight:** Branch coverage catches faults that statement coverage misses.
>
> #### 3.2 Branch Coverage Limitations
>
> **Problem:** Compound predicates `if (A && B)` — branch coverage needs only 2 tests:
>
> | Test | A | B | Outcome | Note |
> |------|---|---|---------|------|
> | T1 | true | true | True branch | ✓ |
> | T2 | false | any | False branch | Short-circuit! |
>
> **Missing:** `A=true, B=false` — never tested!
>
> **Fault Example:**
> ```python
> if A and B:    # Should be: A or B
>     x = 1
> ```
>
> The `AND` vs `OR` error remains **undetected**.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 063 — Question 30: Branch vs Statement Coverage (Practical)

> [!question] Question
> **Question 30: Branch vs Statement Coverage (Practical)**
>
> Explain why branch coverage is considered stronger than statement coverage. Provide a code example where 100% statement coverage fails to detect a fault that branch coverage would catch.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.1 Branch Coverage (C1)
>
> **Definition:** Each branch of every decision must be traversed at least once.
>
> **Formula:**
>
> $$\text{Branch Coverage} = \frac{\text{Branches Executed}}{\text{Total Branches}} \times 100\%$$
>
> **Example - Catching the Bug:**
>
> ```python
> x = 0
> if A < 5:      # 2 branches
>     x = 4
> y = z / x
> ```
>
> | Test | A | Path | Catches Bug? |
> |------|---|------|--------------|
> | T1 | 3 | True branch | No |
> | T2 | 6 | False branch | **Yes!** x=0 triggers error |
>
> > **Key Insight:** Branch coverage catches faults that statement coverage misses.
>
> #### 2.2 Statement Coverage (C0)
>
> **Definition:** Each statement must be executed at least once.
>
> **Formula:**
>
> $$\text{Statement Coverage} = \frac{\text{Statements Executed}}{\text{Total Statements}} \times 100\%$$
>
> **Example - The Hidden Bug:**
>
> ```python
> x = 0           # S1
> if A < 5:       # Decision
>     x = 4       # S2
> y = z / x       # S3 ← Potential division by zero!
> ```
>
> **Test: A = 3**
> - Executes: S1, S2, S3
> - Coverage: **100%** ✓
> - **Problem:** Misses `A >= 5` path where `x = 0` causes division by zero!
>
> **Why Statement Coverage Is Weak:**
>
> | Advantage | Disadvantage |
> |-----------|--------------|
> | Simple to measure | Insensitive to control flow |
> | Low test count | Misses branch-specific faults |
> | Easy to achieve | Ignores predicate structure |
>
> > **Key Rule:** Statement coverage is the **floor**, not the **ceiling**. Never rely on it alone!

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 064 — Question 31: MC/DC Calculation (Practical)

> [!question] Question
> **Question 31: MC/DC Calculation (Practical)**
>
> Given predicate `if ((A || B) && C)`:
> a) How many tests for Multiple Condition coverage?
> b) Construct a minimal MC/DC test suite
> c) Show independence pairs for each condition

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.1 Condition Coverage Types Compared
>
> | Coverage Type | Definition | Tests for `if (A && B)` |
> |---------------|------------|-------------------------|
> | **Basic Condition** | Each condition true/false once | 2: (T,T), (F,F) |
> | **Decision Coverage** | Each decision true/false | 2: (T,T), (F,any) |
> | **Condition/Decision** | Both above combined | 2-3 tests |
> | **Multiple Condition** | All combinations | 4: TT, TF, FT, FF |
> | **MC/DC** | Each condition independently affects outcome | 3: TT, TF, FT |
>
> **Multiple Condition Problem:** Exponential growth — $2^n$ test cases!
>
> | Conditions | Multiple Condition | MC/DC |
> |------------|-------------------|-------|
> | 2 | 4 | 3 |
> | 3 | 8 | 4 |
> | 4 | 16 | 5 |
> | n | $2^n$ | **n+1** |
>
> #### Test Suite:
>
> ```text
> { (A=T, B=T), (A=F, B=F) }
> ```
>
> - **Branch coverage**: 100%
>
> - **Basis path coverage**: 100%
>
> - ❌ **Fails to detect the bug**
>
>
> **Why?**
> Because the compound predicate uses multiple conditions (`A` and `B`), but the test cases don’t independently evaluate each one. We need **Multiple Condition Coverage** or **MC/DC** to reveal such faults.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

### Card 065 — Question 32: Critical Analysis (Practical)

> [!question] Question
> **Question 32: Critical Analysis (Practical)**
>
> A project manager claims: "We achieved 95% code coverage, so our software is thoroughly tested." Critically evaluate this claim using evidence from recent research.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### [Code Coverage](code.md)
>
> Basic structural coverage: **statement coverage**, **branch coverage**, and **all-path coverage** with worked examples.
>
> #### Types of Code Coverage
>
> ```mermaid
> flowchart TD
>
>   subgraph DF["Data Flow"]
>     direction TB
>     DU["All DU Paths"]
>     Uses["All Uses"]
>     Defs["All Defs"]
>     DU --> Uses --> Defs
>   end
>
>   subgraph CF["Control Flow"]
>     direction TB
>     Paths["All Paths"]
>     Basis["All Basis Paths"]
>     LCSAJ["All LCSAJ"]
>     Branches["All Branches"]
>     Stmts["All Statements"]
>     Paths --> Basis
>     Paths --> LCSAJ
>     Paths --> Branches
>     Basis --> Branches
>     LCSAJ --> Branches
>     Branches --> Stmts
>   end
>
>   subgraph PRED["Predicates"]
>     direction TB
>     Comp["All Compound Conditions"]
>     MCDC["MC/DC"]
>     Basic["All Basic Conditions"]
>     Comp --> MCDC --> Basic
>     MCDC --> Branches
>   end
>
>   Uses --> Branches
>
>   style DU fill:#f0f0f0,stroke:#999
>   style Uses fill:#f0f0f0,stroke:#999
>   style Defs fill:#f0f0f0,stroke:#999
>   style Comp fill:#f0f0f0,stroke:#999
>   style MCDC fill:#f0f0f0,stroke:#999
>   style Basic fill:#f0f0f0,stroke:#999
> ```

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/coverage/RQ_L04_Coverage.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/coverage/RQ_L04_Coverage.md)

## Software Inspection (28)

### Card 066 — Question 1: Evolution of Inspection

> [!question] Question
> **Question 1: Evolution of Inspection**
>
> Fagan developed formal inspection at IBM in 1976, and the practice evolved significantly over 50 years.
>
> Trace the evolution from 1976 to 2025 through 4 key milestones. What changed at each stage? What principles remained constant?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.1 The Origins: Fagan Inspection (1976)
>
> Michael Fagan  at IBM developed the first formal inspection process in 1976. His key insight was that **systematic human review of code can find defects more cost-effectively than testing**.
>
> **Original Fagan findings:**
> - 67% of all errors found by inspections
> - 38% reduction in machine test time
> - Error-free code sections: 23% before inspections → 60% after
>
> #### Fagan Inspection Process
>
> Michael Fagan introduced formal software inspection at IBM in 1976, establishing a rigorous method that became the foundation for all subsequent inspection techniques . The process achieved remarkable results: **90% of lifecycle defects detected** and **23% productivity improvement**.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 067 — Question 2: Inspection Types Comparison

> [!question] Question
> **Question 2: Inspection Types Comparison**
>
> Laitenberger (2002) compares Fagan Inspection, Code Review, Walkthrough, and Audit.
>
> Compare these four types across: purpose, formality, team size, and cost. When would you choose each type?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.1 Types Comparison
>
> Laitenberger  provides a comprehensive comparison of inspection types:
>
> | Attribute | **Fagan Inspection** | **Code Review** | **Walkthrough** | **Audit** |
> |-----------|---------------------|-----------------|-----------------|-----------|
> | **Purpose** | Defect identification | Defect identification | Design evaluation | Process verification |
> | **Formality** | Very high | Medium | Low | Very high |
> | **Team size** | 4-5 | 1-2 | 5-15 | ~5 |
> | **Cost** | High | Low | Medium | Very high |
> | **Efficiency** | Very high | Average | Low | Low |
> | **Rework** | Mandatory | Optional | Optional | Mandatory |
>
> #### Inspection Techniques (Formality Spectrum)
>
> > *Adapted from K. Wiegers, Peer Reviews in Software (2002) *
>
> ```mermaid
> timeline
>     title Inspection Techniques (Most Formal → Least Formal)
>     Fagan inspections: Well-defined entry/exit conditions, non-author presentation
>     Team review: Formal meeting with stakeholders for comment/approval
>     Walkthrough: Designer leads team through product for questions/comments
>     Tool-assisted code review: Line-by-line critique with diff, annotations, commenting
>     Pair programming: Two developers share writing and reviewing in real-time
>     Ad hoc review: Unstructured, spontaneous reviews
> ```

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 068 — Question 3: Cost-Benefit of Inspection

> [!question] Question
> **Question 3: Cost-Benefit of Inspection**
>
> Research shows inspection finds defects at 1.4-1.75 hours per defect, while testing takes 6-17 hours per defect.
>
> Explain why inspection is more cost-effective than testing. What is the cost multiplier for fixing defects at different stages (review, testing, production)?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.3 Cost-Benefit Evidence
>
> **Cost per defect found:**
>
> | Method | Hours/Defect |
> |--------|-------------|
> | Design inspection | 1.4-1.75 |
> | Code inspection | 1.46-1.58 |
> | Testing | 6.0-17.0 |
>
> **Cost to fix by stage:**
>
> | Stage | Multiplier |
> |-------|-----------|
> | During review | 1× |
> | During testing | 8-12× |
> | In production | 30-100× |
>
> **ROI:** Inspection finds defects 4-10× faster than testing, and fixing them costs 10-100× less than in production .
>
> #### Inspection vs Testing
>
> | Aspect | Inspection | Testing |
> |--------|------------|---------|
> | Timing | Earlier (requirements, design, code) | Later (executable code) |
> | Finds | Omissions, design issues, style | Runtime failures |
> | Cost per defect | 1× | 10-34× |
> | Hours per defect | 1.4-1.75 | 6-17 |
>
> **Key insight:** Inspection and testing are **complementary** — use both for comprehensive verification.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 069 — Question 4: Fagan's Six Phases

> [!question] Question
> **Question 4: Fagan's Six Phases**
>
> Fagan (1976) defined 6 phases for formal inspection: Planning, Overview, Preparation, Inspection Meeting, Rework, and Follow-up.
>
> Describe what happens in each phase. Why are entry and exit criteria important for each phase?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.1 The Six Phases
>
> Fagan  defined six structured phases:
>
> 1. **Planning** — Moderator schedules, distributes materials
> 2. **Overview** — Author presents scope and context
> 3. **Preparation** — Inspectors study materials individually
> 4. **Inspection Meeting** — Team examines artifact systematically
> 5. **Rework** — Author fixes identified defects
> 6. **Follow-up** — Moderator verifies all fixes
>
> **Entry/exit criteria** at each phase ensure quality gates are enforced.
>
> ```mermaid
> %%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#019546', 'lineColor': '#2D6E2A', 'clusterBkg': '#fffef0', 'clusterBorder': '#ccc'}}}%%
> flowchart LR
>     subgraph prep["Preparation Phase"]
>         P1["1. Planning<br>Moderator"]
>         P2["2. Overview<br>Author"]
>         P3["3. Preparation<br>All"]
>     end
>
>     subgraph exec["Execution Phase"]
>         P4["4. Inspection<br>Team"]
>         P5["5. Rework<br>Author"]
>         P6["6. Follow-up<br>Moderator"]
>     end
>
>     P1 --> P2 --> P3 --> P4 --> P5 --> P6
>
>     style P1 fill:#e3f2fd,stroke:#1976d2,color:#000
>     style P2 fill:#e3f2fd,stroke:#1976d2,color:#000
>     style P3 fill:#e3f2fd,stroke:#1976d2,color:#000
>     style P4 fill:#c8e6c9,stroke:#388e3c,color:#000
>     style P5 fill:#fff3e0,stroke:#f57c00,color:#000
>     style P6 fill:#c8e6c9,stroke:#388e3c,color:#000
> ```
>
> #### 1.1 The Origins: Fagan Inspection (1976)
>
> Michael Fagan  at IBM developed the first formal inspection process in 1976. His key insight was that **systematic human review of code can find defects more cost-effectively than testing**.
>
> **Original Fagan findings:**
> - 67% of all errors found by inspections
> - 38% reduction in machine test time
> - Error-free code sections: 23% before inspections → 60% after

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 070 — Question 5: The Four Roles

> [!question] Question
> **Question 5: The Four Roles**
>
> Fagan inspection uses four roles: Moderator, Author, Reader, and Inspector.
>
> Describe the responsibility of each role. Why is it critical that management does NOT participate in inspections?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.2 The Four Roles
>
> | Role | Responsibility |
> |------|----------------|
> | **Moderator** | Facilitates meeting, tracks issues, verifies fixes |
> | **Author** | Clarifies (not justifies), fixes defects afterward |
> | **Reader** | Paraphrases material, leads walk-through |
> | **Inspector** | Identifies discrepancies, votes on issues |
>
> **Critical rule:** Management does NOT participate in examining subordinates' work.
>
> #### The Four Roles
>
> | Role | Responsibility | Key Activities |
> |------|----------------|----------------|
> | **Moderator** | Process owner | Schedule, lead meeting, follow-up, final report |
> | **Author** | Artifact creator | Overview, clarifications, rework |
> | **Reader** | Presentation lead | Paraphrase artifact in meeting (NOT the author) |
> | **Tester** | Testing perspective | Review from functional coverage viewpoint |
>
> **Recommended team size:** 4 people

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 071 — Question 6: Ground Rules for Effective Meetings

> [!question] Question
> **Question 6: Ground Rules for Effective Meetings**
>
> Fagan established ground rules including "Find problems, don't solve them" and "Maximum 2 hours."
>
> List at least 4 ground rules for effective inspection meetings. Explain why the "criticize product, not producer" rule is important for psychological safety.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.3 Ground Rules for Effective Meetings
>
> 1. **Focus on problems, not solutions** — Solutions waste meeting time
> 2. **Criticize product, not producer** — Psychological safety matters
> 3. **Author clarifies, doesn't justify** — Avoid defensive posture
> 4. **Maximum 2 hours duration** — Fatigue degrades detection
> 5. **Preparation is mandatory** — Cancel if team unprepared
>
> > **Key principle:** Your work will be inspected next. Treat others as you wish to be treated.
>
> #### 1.1 The Origins: Fagan Inspection (1976)
>
> Michael Fagan  at IBM developed the first formal inspection process in 1976. His key insight was that **systematic human review of code can find defects more cost-effectively than testing**.
>
> **Original Fagan findings:**
> - 67% of all errors found by inspections
> - 38% reduction in machine test time
> - Error-free code sections: 23% before inspections → 60% after

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 072 — Question 7: Reading Techniques

> [!question] Question
> **Question 7: Reading Techniques**
>
> Reading techniques range from ad hoc to Perspective-Based Reading (PBR).
>
> Compare ad hoc, checklist-based, and PBR techniques. Which technique showed +21-30% improvement? When does 90-95% of defect detection actually occur?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.2 Perspective-Based Reading (PBR)
>
> PBR  assigns stakeholder perspectives to inspectors:
>
> | Perspective | Focus | Work Product Created |
> |-------------|-------|---------------------|
> | **Tester** | Testability | Test plan outline |
> | **Designer** | Implementability | High-level design sketch |
> | **User** | Usability | Usage scenarios |
>
> **Key insight:** If you can't build the work product, there's a defect in the artifact!
>
> **Research results:**
> - Basili et al. (1996) : PBR found 21-30% more defects than traditional reading
> - Shull et al. (2000) : PBR consistently improved detection rates, especially for less-experienced reviewers in unfamiliar domains
>
> #### Inspection Reading Techniques
>
> The **reading technique** determines how inspectors analyze an artifact during preparation. Research shows that systematic techniques like Perspective-Based Reading (PBR) detect **21-30% more defects** than ad hoc approaches .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 073 — Question 8: Perspective-Based Reading (PBR)

> [!question] Question
> **Question 8: Perspective-Based Reading (PBR)**
>
> PBR assigns stakeholder perspectives: Tester, Designer, and User.
>
> For each perspective, explain the focus and work product created. Why is "If you can't build the work product, there's a defect" a key insight?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.2 Perspective-Based Reading (PBR)
>
> PBR  assigns stakeholder perspectives to inspectors:
>
> | Perspective | Focus | Work Product Created |
> |-------------|-------|---------------------|
> | **Tester** | Testability | Test plan outline |
> | **Designer** | Implementability | High-level design sketch |
> | **User** | Usability | Usage scenarios |
>
> **Key insight:** If you can't build the work product, there's a defect in the artifact!
>
> **Research results:**
> - Basili et al. (1996) : PBR found 21-30% more defects than traditional reading
> - Shull et al. (2000) : PBR consistently improved detection rates, especially for less-experienced reviewers in unfamiliar domains
>
> #### Perspective-Based Reading (PBR)
>
> PBR is the most researched and effective technique for requirements inspection  .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 074 — Question 9: Checklist Design

> [!question] Question
> **Question 9: Checklist Design**
>
> Cohen (2006) provides best practices for code review checklists.
>
> List at least 3 "Do" and 3 "Don't" recommendations for checklist design. Why are checklists most effective at detecting omissions?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.3 Checklist Best Practices
>
> Cohen  provides guidance for effective checklists:
>
> **Do:**
> - 10-20 items maximum
> - Focus on omissions (hardest to spot)
> - Include common error patterns
> - Update based on defect data
>
> **Don't:**
> - Overemphasize style (use linters)
> - Create checklist bureaucracy
> - Use for all review types
> - Ignore domain-specific issues
>
> > "Checklists are most effective at detecting omissions—the hardest errors for a reviewer to notice naturally" — Cohen 2006
>
> #### 5.3 Google Modern Code Review
>
> Sadowski  studied modern code review at Google:
>
> | Metric | Value |
> |--------|-------|
> | Median change size | 24 lines |
> | Median reviewers | 1 |
> | Median review latency | < 4 hours |
> | Changes needing ≤1 iteration | >80% |
> | Dev time on review | 3.2 hrs/week |
>
> **Key insights:**
> - Small changes = fast reviews
> - Single reviewer usually sufficient
> - Async works at scale
> - Integrate with CI/CD
>
> **Contrast:** Google's 24-line median vs Fagan's 200-300 NCSS sessions.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 075 — Question 10: Cisco Study - Size

> [!question] Question
> **Question 10: Cisco Study - Size**
>
> The Cisco study (Cohen 2006) analyzed 3.2 million lines of code reviewed by 50 programmers.
>
> What happens to defect detection when review size exceeds 400 LOC? What is the optimal review size range and why?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Cisco Study: Optimal Review Parameters
>
> The largest empirical study of code review effectiveness was conducted at Cisco Systems, involving **50 programmers** and **3.2 million lines of code** .
>
> #### 5.1 The Cisco Study
>
> Cohen  analyzed 50 programmers reviewing 3.2 million lines of code at Cisco Systems.
>
> **Finding 1: Size Matters**
>
> Defect density drops rapidly beyond 200 LOC. The optimal review size is 200-400 LOC :
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 076 — Question 11: Cisco Study - Rate

> [!question] Question
> **Question 11: Cisco Study - Rate**
>
> The Cisco study found that review rate strongly affects effectiveness.
>
> What is the threshold review rate above which reviewers are "rubber stamping"? What correlation exists between rushed reviews and post-release defects?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.1 The Cisco Study
>
> Cohen  analyzed 50 programmers reviewing 3.2 million lines of code at Cisco Systems.
>
> **Finding 1: Size Matters**
>
> Defect density drops rapidly beyond 200 LOC. The optimal review size is 200-400 LOC :
>
> …
>
> #### Cisco Study: Optimal Review Parameters
>
> The largest empirical study of code review effectiveness was conducted at Cisco Systems, involving **50 programmers** and **3.2 million lines of code** .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 077 — Question 12: The Magic Numbers

> [!question] Question
> **Question 12: The Magic Numbers**
>
> Three "magic numbers" summarize optimal code review parameters.
>
> State the three optimal parameters (size, rate, duration). How much did Cisco save by implementing these practices?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Cisco Study: Optimal Review Parameters
>
> The largest empirical study of code review effectiveness was conducted at Cisco Systems, involving **50 programmers** and **3.2 million lines of code** .
>
> #### 5.2 The Magic Numbers
>
> **Empirically validated optimal parameters:**
>
> | Parameter | Recommendation | Source |
> |-----------|----------------|--------|
> | **Review size** | 200-400 LOC max | Cisco study |
> | **Review rate** | < 500 LOC/hour | Cisco study |
> | **Session duration** | 60-90 minutes max | Fatigue research |
> | **Bug detection speed** | 1 bug / 10-15 min | Efficient teams |
>
> **Business impact:** Cisco saved $2.6M by reducing support calls from 50K to 20K per year.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 078 — Question 13: Google Modern Code Review

> [!question] Question
> **Question 13: Google Modern Code Review**
>
> Sadowski (2018) studied code review at Google.
>
> What are Google's median values for: change size, number of reviewers, and review latency? How does this compare to Fagan's original parameters?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Google Modern Code Review
>
> Sadowski  studied modern code review at Google:
>
> | Metric | Value |
> |--------|-------|
> | Median change size | 24 lines |
> | Median reviewers | 1 |
> | Median review latency | < 4 hours |
> | Changes needing ≤1 iteration | >80% |
> | Dev time on review | 3.2 hrs/week |
>
> **Key insights:**
> - Small changes = fast reviews
> - Single reviewer usually sufficient
> - Async works at scale
> - Integrate with CI/CD
>
> **Contrast:** Google's 24-line median vs Fagan's 200-300 NCSS sessions.
>
> #### Google (Sadowski 2018)
>
> | Metric | Value |
> |--------|-------|
> | Median review latency | **< 4 hours** |
> | Median change size | **24 lines** |
> | Median reviewers | **1** |
> | Changes needing ≤1 iteration | >80% |
> | Developer time on review | 3.2 hours/week |
>
> Source:

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 079 — Question 14: Microsoft Findings

> [!question] Question
> **Question 14: Microsoft Findings**
>
> Bosu (2015) studied what makes code review comments useful at Microsoft.
>
> What percentage of comments are marked useful? How does reviewer experience affect usefulness (first-time vs. experienced)? What correlation exists between "reviews without discussion" and defects?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.4 Microsoft Research
>
> Bosu  studied useful code review comments at Microsoft:
>
> | Metric | Value |
> |--------|-------|
> | Comments marked useful | 65.5% |
> | Experienced reviewer usefulness | 65-71% |
> | First-time reviewer usefulness | 32-37% |
> | Reviews without discussion | More defect-prone |
>
> **Key insight:** Participation quality matters more than coverage. Silent approvals and hasty reviews correlate with post-release defects .
>
> #### Microsoft (Bosu 2015)
>
> | Metric | Value |
> |--------|-------|
> | Comments marked useful | **65.5%** |
> | Experienced reviewer usefulness | 65-71% |
> | First-time reviewer usefulness | 32-37% |
>
> Source:

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 080 — Question 15: Anti-Patterns

> [!question] Question
> **Question 15: Anti-Patterns**
>
> Several anti-patterns can destroy inspection effectiveness.
>
> List at least 4 anti-patterns and explain why each is harmful. Why should review metrics never be used for performance evaluations?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.5 Anti-Patterns to Avoid
>
> | Anti-Pattern | Why It's Harmful |
> |--------------|------------------|
> | Management participation | Creates fear, kills honesty |
> | Using metrics for HR evaluation | Developers game the numbers |
> | Reviewing > 400 LOC | Effectiveness near zero |
> | Rushing (> 500 LOC/hr) | Missing critical defects |
> | LGTM without reading | False sense of security |
> | Author justifying, not clarifying | Defensive, unproductive |
>
> > "Never use review metrics for performance evaluations—developers will manipulate data if punished" — Cohen 2006
>
> #### Inspection Effectiveness Data
>
> Software inspection is consistently shown to be the **most cost-effective defect removal technique**, with detection rates of 60-90% and cost ratios of 1:10 to 1:34 compared to testing  .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 081 — Question 16: Fault Injection

> [!question] Question
> **Question 16: Fault Injection**
>
> Mills' fault injection (error seeding) method estimates total defects.
>
> Explain the 5 steps of the fault injection process. Given: 12 seeded defects injected, 4 seeded found, 11 original found. Calculate the estimated total defects.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 6.2 Fault Injection (Error Seeding)
>
> Mills' methodology (1970s) estimates total defects by measuring detection of known seeded defects.
>
> **Process:**
> 1. Inject **I** known defects into artifact
> 2. Run inspection process normally
> 3. Count: **i** = seeded defects found
> 4. Count: **n** = original defects found
> 5. Estimate total: **N = n × (I / i)**
>
> **Formula:**
> $$N = n \times \frac{I}{i}$$
>
> **Example:**
> - Inject 12 defects
> - Find 4 seeded + 11 original
> - N = 11 × (12/4) = **33 estimated**
> - Found 11, remaining: **22 unfound**
>
> **Challenge:** Seeded defects must have similar detectability to real defects—this is difficult to achieve in practice.
>
> #### Mills' Methodology (1970s)
>
> Fault injection estimates total defects by measuring how well inspectors detect **intentionally seeded** defects.
>
> **Process:**
> 1. Inject **I** known defects into the artifact
> 2. Run the inspection process normally
> 3. Count **i** = seeded defects found
> 4. Count **n** = original defects found
> 5. Estimate total original defects: **N = n × (I / i)**

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 082 — Question 17: Capture-Recapture Formula

> [!question] Question
> **Question 17: Capture-Recapture Formula**
>
> The capture-recapture method originates from wildlife biology.
>
> State the Lincoln-Petersen formula. Given: Inspector A finds 20 defects, Inspector B finds 15, both find 6. Calculate the estimated total and remaining defects.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 6.3 Capture-Recapture Method
>
> The capture-recapture method  originates from wildlife biology. In software inspection:
> - "Animals" = defects
> - "Capture sessions" = independent inspectors
> - "Marked and recaptured" = defects found by multiple inspectors
>
> ```mermaid
> %%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#019546', 'lineColor': '#2D6E2A', 'clusterBkg': '#fffef0', 'clusterBorder': '#ccc'}}}%%
> flowchart TB
>     subgraph inspectors["Two Independent Inspectors"]
>         I1["Inspector 1<br>Found: M = 12"]
>         I2["Inspector 2<br>Found: C = 15"]
>     end
>
>     subgraph overlap["Overlap"]
>         R["Recaptured: R = 4<br>(found by both)"]
>     end
>
>     subgraph estimate["Estimate"]
>         N["N = M × C / R<br>= 12 × 15 / 4<br>= 45 total defects"]
>     end
>
>     I1 --> R
>     I2 --> R
>     R --> N
>
>     style I1 fill:#bbdefb,stroke:#1976d2,color:#000
>     style I2 fill:#fff3e0,stroke:#f57c00,color:#000
>     style R fill:#c8e6c9,stroke:#388e3c,color:#000
>     style N fill:#c8e6c9,stroke:#388e3c,stroke-width:2px,color:#000
> ```
>
> **Lincoln-Petersen Formula:**
>
> $$\hat{N} = \frac{M \times C}{R}$$
>
> Where:
> - $\hat{N}$ = estimated total defects
> - $M$ = defects found by Inspector 1
> - $C$ = defects found by Inspector 2
> - $R$ = defects found by both (the overlap)
>
> **Example:**
> - Inspector A finds 20 defects
> - Inspector B finds 15 defects
> - Both find 6 of the same defects
> - N = (20 × 15) / 6 = **50 estimated**
> - Found 29 unique, remaining: **21 unfound**
>
> **Defect Distribution Visualization:**
>
> …
>
> #### The Lincoln-Petersen Formula
>
> For two independent inspectors, the estimated total defects is:
>
> $$\hat{N} = \frac{n_1 \times n_2}{m_2}$$
>
> Where:
> - $\hat{N}$ = estimated total defects
> - $n_1$ = defects found by inspector 1
> - $n_2$ = defects found by inspector 2
> - $m_2$ = defects found by **both** (the overlap)

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 083 — Question 18: Capture-Recapture Models

> [!question] Question
> **Question 18: Capture-Recapture Models**
>
> Briand (2000) evaluated four capture-recapture models: M₀, Mₜ, Mₕ, and Mₜₕ.
>
> Describe what each model assumes. Which model is recommended and with what estimator? What is the minimum number of inspectors for reliable estimates?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 6.4 Model Selection
>
> The basic Lincoln-Petersen assumes all defects are equally likely to be found. Briand  evaluated four models:
>
> | Model | Assumption | Use When |
> |-------|------------|----------|
> | **M₀** | All defects equal, all inspectors equal | Never (unrealistic) |
> | **Mₜ** | Inspectors vary in capability | Mixed experience levels |
> | **Mₕ** | Defects vary in visibility | **Recommended default** |
> | **Mₜₕ** | Both vary | Most realistic, needs 4+ inspectors |
>
> **Recommendation:** Use Model Mₕ with Jackknife estimator. Minimum 4 inspectors for reliable estimates.
>
> #### Model Selection
>
> The basic Lincoln-Petersen assumes all defects are equally likely to be found. In practice, some bugs are harder to find than others. Briand et al.  evaluated four models:
>
> | Model | Accounts For | Assumption |
> |-------|--------------|------------|
> | **M₀** | Nothing | All defects equal, all inspectors equal |
> | **Mₜ** | Inspector variation | Inspectors have different abilities |
> | **Mₕ** | Defect heterogeneity | Some defects harder to find |
> | **Mₜₕ** | Both | Inspector ability AND defect difficulty vary |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 084 — Question 19: Capture-Recapture Limitations

> [!question] Question
> **Question 19: Capture-Recapture Limitations**
>
> Capture-recapture has several limitations for defect estimation.
>
> List at least 3 limitations of the capture-recapture method. What happens when the overlap (R) equals zero? Why does the method tend to underestimate?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### [Defect Estimation](capture-recapture.md)
>
> Two methods to estimate remaining defects:
> - **Fault Injection**: Seed defects, measure detection rate
> - **Capture-Recapture**: Lincoln-Petersen formula, 4+ inspectors
> - Model selection (Mₕ with Jackknife)
>
> #### 6.3 Capture-Recapture Method
>
> The capture-recapture method  originates from wildlife biology. In software inspection:
> - "Animals" = defects
> - "Capture sessions" = independent inspectors
> - "Marked and recaptured" = defects found by multiple inspectors
>
> ```mermaid
> %%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#019546', 'lineColor': '#2D6E2A', 'clusterBkg': '#fffef0', 'clusterBorder': '#ccc'}}}%%
> flowchart TB
>     subgraph inspectors["Two Independent Inspectors"]
>         I1["Inspector 1<br>Found: M = 12"]
>         I2["Inspector 2<br>Found: C = 15"]
>     end
>
>     subgraph overlap["Overlap"]
>         R["Recaptured: R = 4<br>(found by both)"]
>     end
>
>     subgraph estimate["Estimate"]
>         N["N = M × C / R<br>= 12 × 15 / 4<br>= 45 total defects"]
>     end
>
>     I1 --> R
>     I2 --> R
>     R --> N
>
>     style I1 fill:#bbdefb,stroke:#1976d2,color:#000
>     style I2 fill:#fff3e0,stroke:#f57c00,color:#000
>     style R fill:#c8e6c9,stroke:#388e3c,color:#000
>     style N fill:#c8e6c9,stroke:#388e3c,stroke-width:2px,color:#000
> ```
>
> **Lincoln-Petersen Formula:**
>
> $$\hat{N} = \frac{M \times C}{R}$$
>
> Where:
> - $\hat{N}$ = estimated total defects
> - $M$ = defects found by Inspector 1
> - $C$ = defects found by Inspector 2
> - $R$ = defects found by both (the overlap)
>
> **Example:**
> - Inspector A finds 20 defects
> - Inspector B finds 15 defects
> - Both find 6 of the same defects
> - N = (20 × 15) / 6 = **50 estimated**
> - Found 29 unique, remaining: **21 unfound**
>
> **Defect Distribution Visualization:**
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 085 — Question 20: LLM Code Review

> [!question] Question
> **Question 20: LLM Code Review**
>
> Zeng (2025) evaluated LLM-based code review tools on real pull requests.
>
> What F1 score did the best LLM achieve? What is the main limitation of current LLM code review? Why is human review still essential?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 7.1 Current State (2025)
>
> Zeng  evaluated LLM-based code review on 1,000 pull requests from 12 Python projects.
>
> **Key Findings:**
>
> | Metric | Value |
> |--------|-------|
> | Best F1 score | 19.38% |
> | Human agreement | ~90% |
> | Main limitation | High false positives |
> | Aggregation boost | +43.67% F1 |
>
> #### 5.3 Google Modern Code Review
>
> Sadowski  studied modern code review at Google:
>
> | Metric | Value |
> |--------|-------|
> | Median change size | 24 lines |
> | Median reviewers | 1 |
> | Median review latency | < 4 hours |
> | Changes needing ≤1 iteration | >80% |
> | Dev time on review | 3.2 hrs/week |
>
> **Key insights:**
> - Small changes = fast reviews
> - Single reviewer usually sufficient
> - Async works at scale
> - Integrate with CI/CD
>
> **Contrast:** Google's 24-line median vs Fagan's 200-300 NCSS sessions.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 086 — Question 21: LLM Capabilities

> [!question] Question
> **Question 21: LLM Capabilities**
>
> Current LLM code review has varying capabilities across different task types.
>
> Rate LLM performance (good/moderate/poor) for: functional bugs, style issues, security vulnerabilities. What technique boosted F1 by 43%?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 7.3 Practical Implications
>
> | Capability | LLM Performance |
> |------------|-----------------|
> | Functional bug detection | Moderate |
> | Style/documentation | Poor |
> | Security vulnerabilities | Emerging |
> | False positive rate | High (main barrier) |
>
> > "State-of-the-art ACR tools and LLMs are not yet ready for deployment" — Zeng 2025
>
> **Practical advice:** Use LLM as assistant, not replacement. Human review remains essential for production code.
>
> #### 5.3 Google Modern Code Review
>
> Sadowski  studied modern code review at Google:
>
> | Metric | Value |
> |--------|-------|
> | Median change size | 24 lines |
> | Median reviewers | 1 |
> | Median review latency | < 4 hours |
> | Changes needing ≤1 iteration | >80% |
> | Dev time on review | 3.2 hrs/week |
>
> **Key insights:**
> - Small changes = fast reviews
> - Single reviewer usually sufficient
> - Async works at scale
> - Integrate with CI/CD
>
> **Contrast:** Google's 24-line median vs Fagan's 200-300 NCSS sessions.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 087 — Question 22: Inspection vs Testing

> [!question] Question
> **Question 22: Inspection vs Testing**
>
> Inspection and testing are complementary verification techniques.
>
> Create a comparison table with: timing, what each finds, cost per defect, and hours per defect. Why should you use both techniques?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Inspection vs Testing
>
> | Aspect | Inspection | Testing |
> |--------|------------|---------|
> | Timing | Earlier (requirements, design, code) | Later (executable code) |
> | Finds | Omissions, design issues, style | Runtime failures |
> | Cost per defect | 1× | 10-34× |
> | Hours per defect | 1.4-1.75 | 6-17 |
>
> **Key insight:** Inspection and testing are **complementary** — use both for comprehensive verification.
>
> #### Inspection vs. Testing
>
> | Aspect | Inspection | Testing |
> |--------|------------|---------|
> | Timing | Earlier (requirements, design, code) | Later (executable code) |
> | Finds | Omissions, design issues, style | Runtime failures |
> | Cost per defect | 1× | 10-34× |
> | Hours per defect | 1.4-1.75 | 6-17 |
>
> {: .highlight }
> > Inspection and testing are **complementary** — use both for comprehensive verification.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 088 — Question 23: Capture-Recapture Calculation (Practical)

> [!question] Question
> **Question 23: Capture-Recapture Calculation (Practical)**
>
> An inspection meeting results in the identification of 13 defects by four inspectors:
>
> | Line | Inspector A | Inspector B | Inspector C | Inspector D |
> |------|:-----------:|:-----------:|:-----------:|:-----------:|
> | 8    | x | | x | x |
> | 12   | | x | | x |
> | 33   | | x | | |
> | 55   | | x | | |
> | 56   | x | | | |
> | 78   | | | x | |
> | 120  | | x | | |
> | 145  | | | x | x |
> | 146  | | x | | |
> | 230  | | | | x |
> | 255  | | | | x |
> | 300  | | x | | |
> | 321  | x | | x | |
>
> Using Humphrey's capture-recapture procedure, how many latent defects can you estimate remain unidentified in this code? Show your calculation.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Estimating Remaining Defects
>
> How many defects remain after an inspection? Two statistical methods can estimate total defect content:
>
> 1. **Fault Injection (Error Seeding)** — Seed known defects, measure detection rate
> 2. **Capture-Recapture** — Use inspector overlap to estimate population
>
> #### 6.3 Capture-Recapture Method
>
> The capture-recapture method  originates from wildlife biology. In software inspection:
> - "Animals" = defects
> - "Capture sessions" = independent inspectors
> - "Marked and recaptured" = defects found by multiple inspectors
>
> ```mermaid
> %%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#019546', 'lineColor': '#2D6E2A', 'clusterBkg': '#fffef0', 'clusterBorder': '#ccc'}}}%%
> flowchart TB
>     subgraph inspectors["Two Independent Inspectors"]
>         I1["Inspector 1<br>Found: M = 12"]
>         I2["Inspector 2<br>Found: C = 15"]
>     end
>
>     subgraph overlap["Overlap"]
>         R["Recaptured: R = 4<br>(found by both)"]
>     end
>
>     subgraph estimate["Estimate"]
>         N["N = M × C / R<br>= 12 × 15 / 4<br>= 45 total defects"]
>     end
>
>     I1 --> R
>     I2 --> R
>     R --> N
>
>     style I1 fill:#bbdefb,stroke:#1976d2,color:#000
>     style I2 fill:#fff3e0,stroke:#f57c00,color:#000
>     style R fill:#c8e6c9,stroke:#388e3c,color:#000
>     style N fill:#c8e6c9,stroke:#388e3c,stroke-width:2px,color:#000
> ```
>
> **Lincoln-Petersen Formula:**
>
> $$\hat{N} = \frac{M \times C}{R}$$
>
> Where:
> - $\hat{N}$ = estimated total defects
> - $M$ = defects found by Inspector 1
> - $C$ = defects found by Inspector 2
> - $R$ = defects found by both (the overlap)
>
> **Example:**
> - Inspector A finds 20 defects
> - Inspector B finds 15 defects
> - Both find 6 of the same defects
> - N = (20 × 15) / 6 = **50 estimated**
> - Found 29 unique, remaining: **21 unfound**
>
> **Defect Distribution Visualization:**
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 089 — Question 24: Inspection Prioritization Under Budget

> [!question] Question
> **Question 24: Inspection Prioritization Under Budget**
>
> You need to inspect a large banking system comprising around 20,000 lines of COBOL and 25,000 lines of newly written Java code with regards to vulnerabilities, but only have enough budget to inspect 10,000 lines.
>
> How would you prioritize which components to inspect without overrunning the budget? What criteria would you use?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.2 When to Inspect
>
> **Inspect these (high-risk artifacts):**
> - Requirements (ambiguity, completeness)
> - Architecture (quality attributes)
> - Security-critical code
> - API contracts
> - Complex algorithms
>
> **Skip inspection for:**
> - Style issues (use linters)
> - Trivial changes
> - Throwaway/prototype code
> - Auto-generated code
> - Auto-formatted code
>
> #### 1.1 The Origins: Fagan Inspection (1976)
>
> Michael Fagan  at IBM developed the first formal inspection process in 1976. His key insight was that **systematic human review of code can find defects more cost-effectively than testing**.
>
> **Original Fagan findings:**
> - 67% of all errors found by inspections
> - 38% reduction in machine test time
> - Error-free code sections: 23% before inspections → 60% after

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 090 — Question 25: Egoless Programming

> [!question] Question
> **Question 25: Egoless Programming**
>
> Wiegers references Weinberg's concept of "egoless programming."
>
> What does Weinberg mean by this concept? Why is it relevant to peer review? How does this relate to Fagan's rule "criticize product, not producer"?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.1 The Origins: Fagan Inspection (1976)
>
> Michael Fagan  at IBM developed the first formal inspection process in 1976. His key insight was that **systematic human review of code can find defects more cost-effectively than testing**.
>
> **Original Fagan findings:**
> - 67% of all errors found by inspections
> - 38% reduction in machine test time
> - Error-free code sections: 23% before inspections → 60% after
>
> #### 5.3 Google Modern Code Review
>
> Sadowski  studied modern code review at Google:
>
> | Metric | Value |
> |--------|-------|
> | Median change size | 24 lines |
> | Median reviewers | 1 |
> | Median review latency | < 4 hours |
> | Changes needing ≤1 iteration | >80% |
> | Dev time on review | 3.2 hrs/week |
>
> **Key insights:**
> - Small changes = fast reviews
> - Single reviewer usually sufficient
> - Async works at scale
> - Integrate with CI/CD
>
> **Contrast:** Google's 24-line median vs Fagan's 200-300 NCSS sessions.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 091 — Question 26: Session Limits

> [!question] Question
> **Question 26: Session Limits**
>
> The literature suggests a number of limits on code review sessions.
>
> For each of the following, state a reasonable guideline with justification:
> a. Number of lines of code inspected in one sitting
> b. Number of lines of code inspected per hour (rate)
> c. Maximum inspection session length

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Google Modern Code Review
>
> Sadowski  studied modern code review at Google:
>
> | Metric | Value |
> |--------|-------|
> | Median change size | 24 lines |
> | Median reviewers | 1 |
> | Median review latency | < 4 hours |
> | Changes needing ≤1 iteration | >80% |
> | Dev time on review | 3.2 hrs/week |
>
> **Key insights:**
> - Small changes = fast reviews
> - Single reviewer usually sufficient
> - Async works at scale
> - Integrate with CI/CD
>
> **Contrast:** Google's 24-line median vs Fagan's 200-300 NCSS sessions.
>
> #### Key Finding: Review Rate Matters
>
> | Review Rate | Defect Detection |
> |-------------|------------------|
> | < 300 LOC/hour | **Thorough** review |
> | 300-500 LOC/hour | Acceptable |
> | > 500 LOC/hour | **Hasty** — misses defects |
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "title": "Defect Density vs. Review Rate",
>   "width": 450,
>   "height": 250,
>   "layer": [
>     {
>       "data": {
>         "values": [
>           {"rate": 50, "defects": 142}, {"rate": 100, "defects": 100},
>           {"rate": 150, "defects": 48}, {"rate": 200, "defects": 55},
>           {"rate": 250, "defects": 100}, {"rate": 300, "defects": 98},
>           {"rate": 350, "defects": 30}, {"rate": 400, "defects": 50},
>           {"rate": 450, "defects": 30}, {"rate": 550, "defects": 28},
>           {"rate": 650, "defects": 10}, {"rate": 750, "defects": 12},
>           {"rate": 850, "defects": 80}, {"rate": 950, "defects": 10},
>           {"rate": 1100, "defects": 12}, {"rate": 1300, "defects": 8}
>         ]
>       },
>       "mark": {"type": "point", "color": "#1976d2", "size": 50, "filled": true},
>       "encoding": {
>         "x": {"field": "rate", "type": "quantitative", "title": "Review Rate (LOC/hour)", "scale": {"domain": [0, 1400]}},
>         "y": {"field": "defects", "type": "quantitative", "title": "Defects Found / KSLOC", "scale": {"domain": [0, 160]}}
>       }
>     },
>     {
>       "data": {"values": [{"x": 500}]},
>       "mark": {"type": "rule", "color": "#d32f2f", "strokeWidth": 3},
>       "encoding": {"x": {"field": "x", "type": "quantitative"}}
>     }
>   ]
> }
> ```
>
> {: .note }
> > *Chart reconstructed to illustrate trend. See  for original data.*
>
> The red vertical line at 500 LOC/hour marks the threshold above which reviews become hasty and miss defects.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 092 — Question 27: Undesirable Attitudes

> [!question] Question
> **Question 27: Undesirable Attitudes**
>
> Mandatory code reviews can sometimes lead to negative programmer attitudes.
>
> List two undesirable attitudes that can emerge in an organization with mandatory code reviews. Describe three mechanisms that management, the organization, or programmers can use to prevent such attitudes from developing.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Google Modern Code Review
>
> Sadowski  studied modern code review at Google:
>
> | Metric | Value |
> |--------|-------|
> | Median change size | 24 lines |
> | Median reviewers | 1 |
> | Median review latency | < 4 hours |
> | Changes needing ≤1 iteration | >80% |
> | Dev time on review | 3.2 hrs/week |
>
> **Key insights:**
> - Small changes = fast reviews
> - Single reviewer usually sufficient
> - Async works at scale
> - Integrate with CI/CD
>
> **Contrast:** Google's 24-line median vs Fagan's 200-300 NCSS sessions.
>
> #### Design vs. Code Inspections
>
> | Type | Minimum | Most Likely | Maximum |
> |------|---------|-------------|---------|
> | **Design** | 25% | 57% | 84% |
> | **Code** | 19% | 57% | 70% |
>
> Source:

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

### Card 093 — Question 28: Good vs Bad Practices

> [!question] Question
> **Question 28: Good vs Bad Practices**
>
> Describe, in your own words:
> - Two good inspection practices and why they work
> - Two bad inspection practices and why they should be avoided

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.1 The Origins: Fagan Inspection (1976)
>
> Michael Fagan  at IBM developed the first formal inspection process in 1976. His key insight was that **systematic human review of code can find defects more cost-effectively than testing**.
>
> **Original Fagan findings:**
> - 67% of all errors found by inspections
> - 38% reduction in machine test time
> - Error-free code sections: 23% before inspections → 60% after
>
> #### Inspection vs Testing
>
> | Aspect | Inspection | Testing |
> |--------|------------|---------|
> | Timing | Earlier (requirements, design, code) | Later (executable code) |
> | Finds | Omissions, design issues, style | Runtime failures |
> | Cost per defect | 1× | 10-34× |
> | Hours per defect | 1.4-1.75 | 6-17 |
>
> **Key insight:** Inspection and testing are **complementary** — use both for comprehensive verification.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/inspection/RQ_A05_Inspection.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/inspection/RQ_A05_Inspection.md)

## Input Domain Testing (26)

### Card 094 — Question 1: Core Definitions

> [!question] Question
> **Question 1: Core Definitions**
>
> Match each testing term with its definition:
>
> | Term | Definition |
> |------|------------|
> | A. Test Case | 1. Mechanism to determine correct output |
> | B. Test Suite | 2. Values provided to system |
> | C. Oracle | 3. Input + expected output + oracle |
> | D. Test Input | 4. Collection of test cases |

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.1 Core Definitions
>
> | Term | Definition |
> |------|------------|
> | **Test Case** | Input + expected output + oracle |
> | **Test Suite** | Collection of test cases |
> | **Oracle** | Mechanism to determine correct output |
> | **Test Input** | Values provided to system |
>
> **The Oracle Problem:** How do we know what the output *should* be?
>
> **Testing Dimensions:**
>
> | Dimension | Options |
> |-----------|---------|
> | **Knowledge** | Black-box (specification) vs White-box (code) |
> | **Intent** | Positive (valid inputs) vs Negative (invalid inputs) |
> | **Level** | Unit, Integration, System |
>
> > **Key Insight:** Test input ≠ test case. Without an oracle, you cannot verify correctness!
>
> #### 4.4 Test Specification vs Test Case
>
> | Test Specification (What) | Test Case (How) |
> |--------------------------|----------------|
> | Array size > 1 | `["world", "father", "father", "country"]` |
> | Occurrences > 1 | `countWhat = "father"` |
> | Unsorted | (order is not sorted) |
> | Alphanumeric content | (strings contain letters) |
> | **Abstract -- many valid concrete values** | **Concrete -- one specific execution, expected: 2** |
>
> **Best practice:** Delay parameterization. One abstract spec can generate many valid concrete test cases .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 095 — Question 2: Positive Test Bias

> [!question] Question
> **Question 2: Positive Test Bias**
>
> What is positive test bias? How does it affect test coverage?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.2 Positive Test Bias
>
> **From Teasley et al. 1994** :
>
> > "Testers naturally gravitate toward inputs they expect to work."
>
> **Psychology Experiment:**
> - Group A: Rewarded for finding bugs
> - Group B: Penalized for false alarms
> - **Result:** Group A found significantly more real bugs
>
> **Implications:**
>
> | Mindset | Outcome |
> |---------|---------|
> | "Prove it works" | Miss edge cases |
> | "Find where it breaks" | Better coverage |
>
> > **Exam Tip:** The positive test bias research shows why **negative testing** (invalid inputs) must be explicitly planned. Testers will naturally under-test invalid partitions without conscious effort.
>
> #### The Positive Test Bias Problem
>
> Research by Teasley et al.  revealed a critical insight:
>
> > **Testers naturally gravitate toward inputs they expect to work.**
>
> **Experiment findings:**
> - Group rewarded for finding bugs → found significantly more bugs
> - Group penalized for false alarms → missed many real faults
>
> | Mindset | Outcome |
> |---------|---------|
> | "Prove it works" | Misses edge cases |
> | "Find where it breaks" | Better fault detection |
>
> **Implication:** Negative testing (invalid inputs) must be explicitly planned—it won't happen naturally.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 096 — Question 3: Black-Box vs White-Box

> [!question] Question
> **Question 3: Black-Box vs White-Box**
>
> A tester has no access to source code and must test a payment gateway API. What testing approach should they use and why?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Input Domain Testing
>
> Input domain testing applies **black-box techniques** to systematically select test inputs based on specifications, without access to source code. These techniques partition the vast input space into manageable, meaningful subsets.
>
> #### Integration with Other Testing
>
> Input domain testing complements structural (white-box) coverage:
>
> | Approach | Focus | Finds |
> |----------|-------|-------|
> | **Input Domain (Black-box)** | What should be tested | Missing functionality |
> | **Code Coverage (White-box)** | What has been tested | Unexecuted code |
>
> **Best practice:** Use input domain techniques to design tests, then measure structural coverage to find gaps.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 097 — Question 4: Partition Requirements

> [!question] Question
> **Question 4: Partition Requirements**
>
> What two properties must equivalence partitions satisfy?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.2 Aspects and Equivalence Classes
>
> An **aspect** is any property that might influence the test object's behavior. Use **probing questions** to discover them: "What inputs? What environment? What values differ? What boundaries? What can go wrong?"
>
> An **equivalence class** partitions aspect values into groups that produce **equivalent behavior**:
> 1. **Mutually exclusive** — no value belongs to multiple classes
> 2. **Collectively exhaustive** — every possible value is covered
>
> {: .exam-tip }
> > **Exam Tip:** Aspect identification is NOT mechanical — it requires creativity and domain insight. Use probing questions systematically.
>
> #### 2.2 Partition Types
>
> ```mermaid
> flowchart LR
>     subgraph Input Domain
>         A[All Possible Inputs]
>     end
>     subgraph Partitions
>         B[Invalid Low]
>         C[Valid Range 1]
>         D[Valid Range 2]
>         E[Invalid High]
>     end
>     A --> B
>     A --> C
>     A --> D
>     A --> E
>
>     style B fill:#ffcdd2
>     style C fill:#c8e6c9
>     style D fill:#c8e6c9
>     style E fill:#ffcdd2
> ```
>
> | Type | Description | Example |
> |------|-------------|---------|
> | **Range-Based** | Numeric ranges defined by comprehension | Age: {<0, 0-12, 13-19, 20-64, 65+} |
> | **Enumeration-Based** | Discrete set of values | State: {CA, TX, NY, ...} |
> | **Invalid** | Values outside valid domain | String when number expected |
>
> **Common Partition Dimensions:**
>
> | Attribute | Partition Values |
> |-----------|------------------|
> | String length | 0, 1, typical, max, >max |
> | Set size | Empty, 1 element, many |
> | Pointer/Reference | Null, valid, invalid |
> | File | Missing, empty, normal, huge |
>
> **Example - Password Validation:**
>
> | Partition | Values | Expected Result |
> |-----------|--------|-----------------|
> | Too short | length < 8 | "Password too short" |
> | Valid simple | 8-12, letters only | "Weak password" |
> | Valid complex | 8-20, mixed chars | "Strong password" |
> | Too long | length > 20 | "Password too long" |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 098 — Question 5: Weak vs Strong EP

> [!question] Question
> **Question 5: Weak vs Strong EP**
>
> A system has three input variables with the following equivalence classes:
> - Variable A: 4 classes
> - Variable B: 3 classes
> - Variable C: 5 classes
>
> How many tests are needed for weak EP? For strong EP?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.3 Weak vs Strong EP
>
> | Strategy | Description | Formula | Use Case |
> |----------|-------------|---------|----------|
> | **Weak EP** | One value from each partition | max(class counts) | Standard testing (one-fault assumption) |
> | **Strong EP** | All combinations of partition values | product of class counts | Higher criticality systems |
>
> **Example:**
> - Variable A: 3 classes
> - Variable B: 4 classes
> - Variable C: 2 classes
>
> | Strategy | Formula | Tests |
> |----------|---------|-------|
> | **Weak** | max(3,4,2) | **4** |
> | **Strong** | 3×4×2 | **24** |
>
> > **Practical Approach:** Start with weak, add strong for high-risk combinations.
>
> #### Weak Equivalence Partitioning
>
> **Formula:** `max(|partition counts|)` tests
>
> **Assumption:** Single-fault—only one input variable causes the fault at a time.
>
> **Example:**
> - Variable A: 3 partitions
> - Variable B: 4 partitions
> - Variable C: 2 partitions
>
> **Weak EP tests:** max(3, 4, 2) = **4 tests**
>
> ```
> Test 1: A₁, B₁, C₁
> Test 2: A₂, B₂, C₂
> Test 3: A₃, B₃, C₁  (wrap C)
> Test 4: A₁, B₄, C₂  (wrap A)
> ```

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 099 — Question 6: Finding Equivalence Classes

> [!question] Question
> **Question 6: Finding Equivalence Classes**
>
> For a function that validates email addresses, identify at least 5 equivalence classes.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.4 Finding Equivalence Classes: Heuristics
>
> | Source | Method | Example |
> |--------|--------|---------|
> | **Specification** | One class per stated case | "Discounts for orders > $100" |
> | **Code paths** | One class per branch | `if/else` → 2 classes |
> | **Error types** | One class per error | Invalid format, overflow |
> | **Ranges** | Valid + boundary violations | 1-100 → {<1, 1-100, >100} |
> | **Membership** | Inside + outside groups | Prime vs composite |
> | **Outputs** | Classes producing same output | All inputs → "Error 404" |
>
> > **Smell:** If you're writing many similar test cases, they probably belong to the same equivalence class!
>
> #### Finding Equivalence Classes: Heuristics
>
> | Source | Method | Example |
> |--------|--------|---------|
> | **Specification** | One class per stated case | "Discounts for orders > $100" → {≤$100, >$100} |
> | **Code paths** | One class per branch | `if/else` → 2 classes |
> | **Error types** | One class per error | Invalid format, overflow, null |
> | **Ranges** | Valid + boundary violations | 1-100 → {<1, 1-100, >100} |
> | **Membership** | Inside + outside groups | Prime vs composite numbers |
> | **Outputs** | Classes producing same output | All inputs → "Error 404" |
>
> > **Smell:** If you're writing many similar test cases, they probably belong to the same equivalence class!

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 100 — Question 7: Partition Heuristics

> [!question] Question
> **Question 7: Partition Heuristics**
>
> Match the heuristic to its example:
>
> | Heuristic | Example |
> |-----------|---------|
> | A. Range-based | 1. US regions (Northeast, South, Midwest, West) |
> | B. Enumeration | 2. Age groups (0-12, 13-19, 20-64, 65+) |
> | C. Error types | 3. Input that causes "File not found" error |

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.2 Partition Types
>
> ```mermaid
> flowchart LR
>     subgraph Input Domain
>         A[All Possible Inputs]
>     end
>     subgraph Partitions
>         B[Invalid Low]
>         C[Valid Range 1]
>         D[Valid Range 2]
>         E[Invalid High]
>     end
>     A --> B
>     A --> C
>     A --> D
>     A --> E
>
>     style B fill:#ffcdd2
>     style C fill:#c8e6c9
>     style D fill:#c8e6c9
>     style E fill:#ffcdd2
> ```
>
> | Type | Description | Example |
> |------|-------------|---------|
> | **Range-Based** | Numeric ranges defined by comprehension | Age: {<0, 0-12, 13-19, 20-64, 65+} |
> | **Enumeration-Based** | Discrete set of values | State: {CA, TX, NY, ...} |
> | **Invalid** | Values outside valid domain | String when number expected |
>
> **Common Partition Dimensions:**
>
> | Attribute | Partition Values |
> |-----------|------------------|
> | String length | 0, 1, typical, max, >max |
> | Set size | Empty, 1 element, many |
> | Pointer/Reference | Null, valid, invalid |
> | File | Missing, empty, normal, huge |
>
> **Example - Password Validation:**
>
> | Partition | Values | Expected Result |
> |-----------|--------|-----------------|
> | Too short | length < 8 | "Password too short" |
> | Valid simple | 8-12, letters only | "Weak password" |
> | Valid complex | 8-20, mixed chars | "Strong password" |
> | Too long | length > 20 | "Password too long" |
>
> #### Range-Based (Comprehension)
>
> Defined by numeric or ordered ranges:
>
> ```mermaid
> flowchart LR
>     subgraph "Age Input Domain"
>         INV["Invalid<br>age < 0"]
>         C["Child<br>0-12"]
>         T["Teen<br>13-19"]
>         A["Adult<br>20-64"]
>         S["Senior<br>65+"]
>     end
>
>     style INV fill:#ffcccc,stroke:#cc0000
>     style C fill:#ccffcc,stroke:#009900
>     style T fill:#ccffcc,stroke:#009900
>     style A fill:#ccffcc,stroke:#009900
>     style S fill:#ccffcc,stroke:#009900
> ```
>
> **Test values:** -1 (invalid), 5 (child), 15 (teen), 30 (adult), 70 (senior)

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 101 — Question 8: Boundary Fault Types

> [!question] Question
> **Question 8: Boundary Fault Types**
>
> Classify each bug by its boundary fault type:
>
> | Bug | Type |
> |-----|------|
> | A. `if (x < 10)` should be `if (x <= 10)` | ? |
> | B. `if (x < 10)` should be `if (x < 11)` | ? |
> | C. Upper bound check is missing | ? |

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.2 Boundary Fault Types
>
> | Fault Type | Description | Example |
> |------------|-------------|---------|
> | **Closure bug** | Wrong operator (< vs ≤) | `if (x < 10)` should be `if (x <= 10)` |
> | **Boundary shift** | Constant off by δ | `if (x < 10)` should be `if (x < 11)` |
> | **Boundary tilt** | Parameter coefficient wrong | ax + by = K vs ax + cy = K |
> | **Missing boundary** | Condition omitted | No upper bound check |
> | **Extra boundary** | Spurious condition | Unnecessary range check |
>
> #### Boundary Fault Types
>
> | Fault Type | Description | Example |
> |------------|-------------|---------|
> | **Closure** | Wrong operator (`<` vs `≤`) | `if (x < 10)` should be `if (x <= 10)` |
> | **Shift** | Boundary at wrong value | `if (x < 10)` should be `if (x < 11)` |
> | **Tilt** | Coefficient wrong (2D+) | `ax + by = K` vs `ax + cy = K` |
> | **Missing** | Boundary not implemented | No upper bound check |
> | **Extra** | Spurious boundary | Unnecessary constraint added |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 102 — Question 9: ON/OFF Points

> [!question] Question
> **Question 9: ON/OFF Points**
>
> For the condition `x >= 100`, identify:
> a) The ON point
> b) The OFF point
> c) Is the boundary open or closed?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Closed vs Open Boundary Summary
>
> | Boundary Type | Operator | ON Point | OFF Point Location |
> |---------------|----------|----------|-------------------|
> | **Closed** | ≤ | On boundary (valid) | Outside (invalid) |
> | **Closed** | ≥ | On boundary (valid) | Outside (invalid) |
> | **Open** | < | On boundary (invalid) | Inside (valid) |
> | **Open** | > | On boundary (invalid) | Inside (valid) |
>
> #### 3.3 ON/OFF Point Formalism
>
> Tian  formalized boundary testing with the ON/OFF point methodology:
>
> | Concept | Definition |
> |---------|------------|
> | **ON point** | Exactly on the boundary (satisfies f(x) = K) |
> | **OFF point** | Just off boundary, within ε distance |
> | **ε-neighborhood** | Small distance for distinguishing ON/OFF |
>
> **OFF point placement depends on boundary type:**
>
> | Boundary Type | OFF Point Location |
> |---------------|-------------------|
> | **Closed** (≤, ≥) | OFF point **outside** domain |
> | **Open** (<, >) | OFF point **inside** domain |
>
> **Concrete Example - Shipping Discount:**
> ```
> Rule: Free shipping for orders ≥ $50 (closed boundary)
>
> ON point:  $50.00  → should get free shipping
> OFF point: $49.99  → should NOT get free shipping (outside domain)
>
> Rule: Discount for orders > $100 (open boundary)
>
> ON point:  $100.00 → should NOT get discount (boundary excluded)
> OFF point: $100.01 → should get discount (inside domain)
> ```
>
> > **Warning — Open Boundaries Are Counterintuitive:** "ON" means *on the boundary* (Beizer's definition), **not** "the feature is on." For open boundaries like `> $100`, the ON point ($100.00) is *excluded* from the domain — it does NOT get the discount. The OFF point ($100.01) is the first value *inside* the domain that does. This reversal surprises many readers: the ON point is inactive, the OFF point is active. Keep the definition in mind: ON = at the boundary; OFF = just past it.
>
> > **Key Insight:** The OFF point must be in the **opposite** processing region from the ON point. This ensures you detect whether the boundary operator is correct.
>
> > **Exam Tip:** For closed boundaries (≤, ≥), the OFF point goes OUTSIDE the domain. For open boundaries (<, >), the OFF point goes INSIDE the domain. Think: "OFF point tests the OTHER side."

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 103 — Question 10: BVA Test Count

> [!question] Question
> **Question 10: BVA Test Count**
>
> A function takes 3 input variables. How many test cases does:
> a) Basic BVA require?
> b) Robust BVA require?
>
> *Hint: Basic BVA = 4k + 1, Robust BVA = 6k + 1*

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Test Count Examples
>
> | Variables (k) | Basic BVA (4k+1) | Robust BVA (6k+1) |
> |---------------|------------------|-------------------|
> | 1 | 5 | 7 |
> | 2 | 9 | 13 |
> | 3 | 13 | 19 |
> | 4 | 17 | 25 |
> | 5 | 21 | 31 |
>
> #### Basic BVA (4k + 1)
>
> For each of k input variables, test:
> - Minimum value
> - Just above minimum (min + ε)
> - Nominal (middle) value
> - Just below maximum (max - ε)
> - Maximum value
>
> Plus one test with all nominal values.
>
> **Formula:** `4k + 1` tests for k variables
>
> **Example:** k = 3 variables → **13 tests**

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 104 — Question 11: Closed vs Open Intervals

> [!question] Question
> **Question 11: Closed vs Open Intervals**
>
> For the valid range $1 < x < 100$, which test points should be used?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.5 Closed vs Open Boundaries
>
> The key difference between closed and open intervals determines where you place ON and OFF test points:
>
> …
>
> #### Closed vs Open Boundary Summary
>
> | Boundary Type | Operator | ON Point | OFF Point Location |
> |---------------|----------|----------|-------------------|
> | **Closed** | ≤ | On boundary (valid) | Outside (invalid) |
> | **Closed** | ≥ | On boundary (valid) | Outside (invalid) |
> | **Open** | < | On boundary (invalid) | Inside (valid) |
> | **Open** | > | On boundary (invalid) | Inside (valid) |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 105 — Question 12: BVA Limitations

> [!question] Question
> **Question 12: BVA Limitations**
>
> Name three limitations of boundary value analysis.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Boundary Value Analysis
>
> Boundary Value Analysis (BVA) focuses testing on the edges of equivalence partitions, where faults are most likely to occur. Off-by-one errors and incorrect boundary operators are among the most common programming mistakes.
>
> #### [Boundary Value Analysis](boundary.md)
>
> Test at partition boundaries where faults cluster:
> - **ON/OFF points**: Formal boundary testing strategy
> - **Fault types**: Closure, shift, tilt, missing, extra
> - **Formulas**: 4k+1 basic, 6k+1 robust

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 106 — Question 13: Decision Table Components

> [!question] Question
> **Question 13: Decision Table Components**
>
> What are the four main components of a decision table?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Decision Table Structure
>
> A decision table has four quadrants:
>
> ```
> ┌─────────────────┬──────────────────────────┐
> │   Condition     │   Condition Values       │
> │   Stubs         │   (per rule)             │
> ├─────────────────┼──────────────────────────┤
> │   Action        │   Action Entries         │
> │   Stubs         │   (per rule)             │
> └─────────────────┴──────────────────────────┘
> ```
>
> | Component | Description |
> |-----------|-------------|
> | **Conditions** | Input variables (rows) |
> | **Condition values** | Y/N, True/False, or enumerated values |
> | **Rules** | Columns—each unique combination |
> | **Actions** | Outputs or behaviors triggered |
> | **Don't care (-)** | Value doesn't affect this rule's outcome |
>
> #### 4.2 Decision Table Structure
>
> **Components:**
>
> | Section | Content |
> |---------|---------|
> | **Conditions** | Input variables (rows) |
> | **Condition values** | Y/N or enumerated values |
> | **Rules** | Columns - each combination |
> | **Actions** | Output behaviors |
> | **Don't care** | `-` or `*` - value doesn't affect outcome |
>
> **ATM Withdrawal Example:**
>
> **Problem Statement:**
> An ATM should dispense cash only if ALL of the following conditions are met:
> - The account has **sufficient balance** for the withdrawal
> - The requested amount is **divisible by 20** (ATM denominations)
> - The withdrawal is **within the daily limit**
>
> Otherwise, the ATM should display the appropriate error message:
> - "Insufficient funds" - if balance is too low
> - "Invalid amount" - if amount is not divisible by 20
> - "Daily limit exceeded" - if limit has been reached
>
> **Legend:** Y = Yes (condition true), N = No (condition false), * = Don't care
>
> | Conditions | R1 | R2 | R3 | R4 | R5 |
> |------------|:--:|:--:|:--:|:--:|:--:|
> | Sufficient Balance? | Y | Y | N | N | * |
> | Amount ÷ 20? | Y | N | Y | N | * |
> | Daily Limit OK? | Y | Y | Y | Y | N |
> | **Actions** | | | | | |
> | Dispense Cash | ✓ | | | | |
> | Show "Invalid Amount" | | ✓ | | ✓ | |
> | Show "Insufficient Funds" | | | ✓ | ✓ | |
> | Show "Limit Exceeded" | | | | | ✓ |
>
> **Reading the table:**
> - **R1:** All conditions met → Dispense cash
> - **R2:** Good balance but bad amount → "Invalid amount"
> - **R3:** Bad balance, good amount → "Insufficient funds"
> - **R4:** Bad balance, bad amount → Show both errors (or priority error)
> - **R5:** Daily limit exceeded → "Limit exceeded" (other conditions don't matter)

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 107 — Question 14: Rule Count

> [!question] Question
> **Question 14: Rule Count**
>
> A decision table has 3 binary conditions (Y/N). How many rules are needed before consolidation?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Decision Table Structure
>
> A decision table has four quadrants:
>
> ```
> ┌─────────────────┬──────────────────────────┐
> │   Condition     │   Condition Values       │
> │   Stubs         │   (per rule)             │
> ├─────────────────┼──────────────────────────┤
> │   Action        │   Action Entries         │
> │   Stubs         │   (per rule)             │
> └─────────────────┴──────────────────────────┘
> ```
>
> | Component | Description |
> |-----------|-------------|
> | **Conditions** | Input variables (rows) |
> | **Condition values** | Y/N, True/False, or enumerated values |
> | **Rules** | Columns—each unique combination |
> | **Actions** | Outputs or behaviors triggered |
> | **Don't care (-)** | Value doesn't affect this rule's outcome |
>
> #### Before Consolidation (8 rules):
>
> | | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
> |-|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
> | A | Y | Y | Y | Y | N | N | N | N |
> | B | Y | Y | N | N | Y | Y | N | N |
> | C | Y | N | Y | N | Y | N | Y | N |
> | **Action X** | ✓ | | | | | | | |
> | **Action Y** | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 108 — Question 15: Checksum Verification

> [!question] Question
> **Question 15: Checksum Verification**
>
> After consolidation, a decision table has 5 rules that cover {2, 3, 1, 4, 2} original rules. Was the consolidation correct if the original table had 12 rules?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.4 Consolidation and Verification
>
> **Why consolidate?** Rules that produce the *same actions* can be merged using don't-care (`*`) values, reducing the number of test cases.
>
> **Full ATM Table (8 rules):**
>
> | | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
> |-|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
> | Balance OK? | Y | Y | Y | Y | N | N | N | N |
> | ÷20? | Y | Y | N | N | Y | Y | N | N |
> | Limit OK? | Y | N | Y | N | Y | N | Y | N |
> | **Actions** ||||||||
> | Dispense Cash | ✓ | | | | | | | |
> | "Invalid Amount" | | | ✓ | | | | ✓ | |
> | "Insufficient Funds" | | | | | ✓ | | ✓ | |
> | **"Limit Exceeded"** | | **✓** | | **✓** | | **✓** | | **✓** |
>
> Notice that R2, R4, R6, R8 all produce the same action ("Limit Exceeded") — whenever `Limit OK? = N`, the other conditions don't matter. These 4 rules consolidate into a single rule with don't-cares.
>
> **After Consolidation (5 rules):**
>
> | | R1 | R2 | R3 | R4 | R5 |
> |-|:--:|:--:|:--:|:--:|:--:|
> | Balance OK? | Y | Y | N | N | * |
> | ÷20? | Y | N | Y | N | * |
> | Limit OK? | Y | Y | Y | Y | N |
> | **Actions** ||||||
> | Dispense Cash | ✓ | | | | |
> | "Invalid Amount" | | ✓ | | ✓ | |
> | "Insufficient Funds" | | | ✓ | ✓ | |
> | "Limit Exceeded" | | | | | ✓ |
> | **Covers** | 1 | 1 | 1 | 1 | 4 |
>
> **Checksum verification:** Sum of "covers" counts must equal original rule count.
>
> $$1 + 1 + 1 + 1 + 4 = 8 \checkmark$$
>
> #### 5. Skipping Decision Table Verification
>
> **Problem:** Consolidation errors lose test cases.
> **Solution:** Always verify checksum after consolidation.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 109 — Question 16: The 8-Step Method

> [!question] Question
> **Question 16: The 8-Step Method**
>
> Put the Beizer 8-step decision table method in correct order:
>
> A. Specify expected outputs per rule
> B. List conditions with values
> C. Verify checksum
> D. Fill columns with all combinations
> E. Develop test cases (one per rule)
> F. List equivalent responses (actions)
> G. Calculate number of rules
> H. Identify common actions → consolidate

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.3 The 8-Step Method (Beizer)
>
> Beizer  defined an 8-step systematic method for building decision tables:
>
> ```mermaid
> flowchart LR
>     subgraph "Build"
>         A[1. List Actions] --> B[2. List Conditions]
>         B --> C[3. Calculate Rules]
>         C --> D[4. Fill Combinations]
>     end
>     subgraph "Refine"
>         D --> E[5. Specify Outputs]
>         E --> F[6. Consolidate]
>         F --> G[7. Verify Checksum]
>     end
>     subgraph "Execute"
>         G --> H[8. Generate Tests]
>     end
> ```
>
> | Step | Purpose | Example |
> |------|---------|---------|
> | 1. List actions | Define output equivalence classes | "Dispense cash", "Show error" |
> | 2. List conditions | Define input variables/partitions | "Balance OK?", "Amount valid?" |
> | 3. Calculate rules | Product of condition values | 2×2×2 = 8 rules |
> | 4. Fill combinations | Systematic enumeration | YYY, YYN, YNY, ... |
> | 5. Specify outputs | Map rules to actions | Rule 1 → Dispense |
> | 6. Consolidate | Identify don't-care conditions | "If limit exceeded, don't care about balance" |
> | 7. Verify checksum | Ensure complete coverage | Sum of covers = original count |
> | 8. Generate tests | 1 per rule + don't-care verification | 5 tests from 8 rules |
>
> > **Key Insight:** Decision tables force completeness - they force explicit consideration of all combinations and can reveal don't-care conditions that reduce test count.
>
> #### Decision Table Structure
>
> A decision table has four quadrants:
>
> ```
> ┌─────────────────┬──────────────────────────┐
> │   Condition     │   Condition Values       │
> │   Stubs         │   (per rule)             │
> ├─────────────────┼──────────────────────────┤
> │   Action        │   Action Entries         │
> │   Stubs         │   (per rule)             │
> └─────────────────┴──────────────────────────┘
> ```
>
> | Component | Description |
> |-----------|-------------|
> | **Conditions** | Input variables (rows) |
> | **Condition values** | Y/N, True/False, or enumerated values |
> | **Rules** | Columns—each unique combination |
> | **Actions** | Outputs or behaviors triggered |
> | **Don't care (-)** | Value doesn't affect this rule's outcome |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 110 — Question 17: When to Use Decision Tables

> [!question] Question
> **Question 17: When to Use Decision Tables**
>
> Which scenarios are good fits for decision table testing?
>
> | Scenario | Good Fit? |
> |----------|-----------|
> | A. Tax calculation with multiple brackets and deductions | ? |
> | B. Performance testing under load | ? |
> | C. Access control based on role, department, and time | ? |
> | D. Continuous output (temperature prediction) | ? |

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Decision Table Testing
>
> Decision tables systematically enumerate all combinations of input conditions and their corresponding actions. They are particularly effective for testing complex business logic where multiple conditions interact to determine behavior.
>
> #### When to Use Decision Tables
>
> **Good fit:**
> - Multiple conditions combine to determine outcomes
> - Logical relationships (AND, OR, NOT)
> - Discrete, enumerable condition values
> - Clear mapping from conditions to actions
> - Order of evaluation doesn't matter
>
> **Best applications:**
> - Business rules engines
> - Permission and access control
> - Insurance/tax calculations
> - Configuration validation
> - State machine transitions
>
> **Not suitable when:**
> - Continuous outputs required
> - Evaluation order matters
> - Actions are probabilistic
> - Conditions are not enumerable

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 111 — Question 18: The 90% Finding

> [!question] Question
> **Question 18: The 90% Finding**
>
> According to NIST research, what percentage of software failures are triggered by 1-2 way parameter interactions?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.2 Key Research Finding
>
> From Kuhn et al. 2004  and Wallace & Kuhn 2001 :
>
> > **90% of software failures are triggered by 1-2 way interactions between parameters.**
>
> **NIST/FDA Research (15 years of medical device recall data):**
>
> …
>
> #### The 90% Finding
>
> Research by Kuhn et al.  and Wallace & Kuhn  revealed a crucial insight about software faults:
>
> > **90% or more of software failures are triggered by 1-2 way parameter interactions.**

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 112 — Question 19: Pairwise Test Reduction

> [!question] Question
> **Question 19: Pairwise Test Reduction**
>
> A configuration has 34 binary switches. Compare the test counts:
> a) All combinations
> b) Pairwise (2-way)

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Pairwise (2-Way) Testing
>
> **Concept:** Cover all pairs of parameter values without testing all combinations.
>
> …
>
> #### Step 4: Pairwise for Valid Combinations
>
> For the "happy path" (all inputs valid), use pairwise to cover parameter interactions:
>
> | Test | Amount | Card | Currency | Recurring |
> |------|--------|------|----------|-----------|
> | P1 | Small | Visa | USD | True |
> | P2 | Small | MasterCard | EUR | False |
> | P3 | Medium | Visa | EUR | False |
> | P4 | Medium | Amex | USD | True |
> | P5 | Large | MasterCard | GBP | True |
> | P6 | Large | Amex | EUR | False |
> | ... | ... | ... | ... | ... |
>
> **Result:** ~15 tests cover all pairwise interactions vs. 72 exhaustive combinations.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 113 — Question 20: Interaction Strength Selection

> [!question] Question
> **Question 20: Interaction Strength Selection**
>
> Match the testing context to the appropriate interaction strength:
>
> | Context | Strength |
> |---------|----------|
> | A. General UI testing | ? |
> | B. Medical device software | ? |
> | C. Business-critical financial system | ? |

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Selecting Interaction Strength
>
> | Context | Recommended Strength | Tests (10 params, 3 values) |
> |---------|---------------------|----------------------------|
> | Quick smoke test | 1-way (each value once) | ~30 |
> | General application | 2-way (pairwise) | ~15 |
> | Business-critical | 3-way | ~45 |
> | Safety-critical | 4-way or higher | ~100+ |
> | Maximum assurance | 6-way | ~300+ |
>
> #### 5.3 Pairwise (2-Way) Testing
>
> **Concept:** Cover all pairs of parameter values without testing all combinations.
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 114 — Question 21: Combinatorial Testing Limitations

> [!question] Question
> **Question 21: Combinatorial Testing Limitations**
>
> Name three limitations of combinatorial testing.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.5 Combinatorial Testing Limitations
>
> - Still need **proper partitioning** first (EP/BVA)
> - **Timing** issues not covered
> - **Masking** can hide faults
> - Tool-generated tests need **oracles**
>
> > **Best Practice:** Combine with equivalence partitioning and BVA - don't rely on combinatorial alone!
>
> #### 5.4 Combinatorial Testing Tools
>
> | Tool | Source |
> |------|--------|
> | **ACTS** | NIST (free) |
> | **Pairwise.org** | Online generators |
> | **Pict** | Microsoft |
> | **Jenny** | Open source |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 115 — Question 22: Technique Matching

> [!question] Question
> **Question 22: Technique Matching**
>
> Match each scenario to the best primary technique:
>
> | Scenario | Technique |
> |----------|-----------|
> | A. Testing a numeric range 1-100 | ? |
> | B. Testing a system with 20 configuration options | ? |
> | C. Testing ATM withdrawal with multiple conditions | ? |
> | D. Testing user types: admin, manager, user, guest | ? |

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Worked Example: Configuration Testing
>
> **System:** Web application with multiple configuration options
>
> | Parameter | Values |
> |-----------|--------|
> | Browser | Chrome, Firefox, Safari, Edge |
> | OS | Windows, macOS, Linux |
> | Screen | Desktop, Tablet, Mobile |
> | Theme | Light, Dark |
> | Language | EN, ES, FR, DE |
>
> **Exhaustive:** 4 × 3 × 3 × 2 × 4 = **288 tests**
>
> **Pairwise:** ~**15-20 tests** covering all pairs
>
> #### Technique Selection Guide
>
> | Situation | Primary Technique | Why |
> |-----------|-------------------|-----|
> | Discrete input categories | **Equivalence Partitioning** | Groups similar behaviors |
> | Numeric ranges with boundaries | **Boundary Value Analysis** | Faults cluster at edges |
> | Multiple conditions → actions | **Decision Tables** | Forces complete coverage |
> | Many parameters, interactions | **Combinatorial Testing** | Catches interaction faults |
> | Hierarchical parameters, many aspects | **Classification Tree Method** | Visual tree structure, constraint handling |
> | Complex business logic | **EP + DT combination** | Partitions + rule coverage |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 116 — Question 23: Integration Order

> [!question] Question
> **Question 23: Integration Order**
>
> What is the recommended order for combining input domain techniques?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Combining Input Domain Techniques
>
> No single input domain technique is sufficient for comprehensive testing. This page explains how to integrate Equivalence Partitioning, Boundary Value Analysis, Decision Tables, and Combinatorial Testing for maximum effectiveness.
>
> #### [Combining Techniques](integration.md)
>
> Integrate techniques for comprehensive coverage:
> - **90% finding**: Most faults from 1-2 way interactions
> - **Selection guide**: Match technique to problem type
> - **Integration pattern**: EP → BVA → DT → Combinatorial

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 117 — Question 24: EP and BVA Relationship (Practical)

> [!question] Question
> **Question 24: EP and BVA Relationship (Practical)**
>
> Explain why boundary value analysis complements equivalence partitioning rather than replacing it. Provide an example.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Boundary Value Analysis
>
> Boundary Value Analysis (BVA) focuses testing on the edges of equivalence partitions, where faults are most likely to occur. Off-by-one errors and incorrect boundary operators are among the most common programming mistakes.
>
> #### [Boundary Value Analysis](boundary.md)
>
> Test at partition boundaries where faults cluster:
> - **ON/OFF points**: Formal boundary testing strategy
> - **Fault types**: Closure, shift, tilt, missing, extra
> - **Formulas**: 4k+1 basic, 6k+1 robust

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 118 — Question 25: Decision Table Construction (Practical)

> [!question] Question
> **Question 25: Decision Table Construction (Practical)**
>
> A login system has the following conditions:
> - Username valid? (Y/N)
> - Password valid? (Y/N)
> - Account active? (Y/N)
>
> a) Create a complete decision table
> b) Consolidate using don't-care values
> c) Verify your consolidation with checksum

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Practical Example: Login System
>
> **Conditions:**
> - Username valid?
> - Password valid?
> - Account active?
>
> **Actions:**
> - Login success
> - Show "Invalid credentials"
> - Show "Account inactive"
>
> #### Consolidation with Don't-Care
>
> When multiple rules produce the same action, consolidate using `-` (don't care):

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

### Card 119 — Question 26: Critical Analysis (Practical)

> [!question] Question
> **Question 26: Critical Analysis (Practical)**
>
> A team decides to use only pairwise testing for a safety-critical medical device control system. Evaluate this decision.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Pairwise (2-Way) Testing
>
> **Concept:** Cover all pairs of parameter values without testing all combinations.
>
> …
>
> #### Decision Table Testing
>
> Decision tables systematically enumerate all combinations of input conditions and their corresponding actions. They are particularly effective for testing complex business logic where multiple conditions interact to determine behavior.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_L05_Domain.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_L05_Domain.md)

## Classification Tree Method (27)

### Card 120 — Q1

> [!question] Question
> Why was CTM developed? What specific problems with Category-Partition does it address?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.2 From Category-Partition to CTM
>
> The CTM  was developed as an improvement over the **Category-Partition (CP) method** :
>
> ```mermaid
> flowchart LR
>     subgraph "Category-Partition (1988)"
>         A1["Specification"] --> A2["TSL Text"]
>         A2 --> A3["Constraints"]
>         A3 --> A4["Generated<br>Test Frames"]
>     end
>
>     subgraph "Classification Tree Method (1993)"
>         B1["Specification"] --> B2["Tree Diagram"]
>         B2 --> B3["Combination<br>Table"]
>         B3 --> B4["Test Cases"]
>     end
>
>     style A1 fill:#fff3cd,stroke:#333
>     style A4 fill:#fff3cd,stroke:#333
>     style B1 fill:#c8e6c9,stroke:#333
>     style B4 fill:#c8e6c9,stroke:#333
> ```
>
> | Aspect | Category-Partition (1988) | Classification Tree Method (1993) |
> |--------|--------------------------|-----------------------------------|
> | **Notation** | Formalized text (TSL language) | Graphical tree + combination table |
> | **Structure** | Flat categories, all at same level | Hierarchical, multi-level |
> | **Test volume** | Start large, add restrictions | Start minimal, add until sufficient |
> | **Specification** | Implicit, lengthy generated lists | Direct, compact combination table |
>
> {: .exam-tip }
> > **Exam Tip:** The key improvement is **visual structure**. CP uses text; CTM uses a tree you can see, discuss with stakeholders, and reason about hierarchically.
>
> #### Why CTM?
>
> Before CTM, the **Category-Partition Method**  used a textual formalism (TSL — Test Specification Language) to define categories, choices, and constraints. While systematic, TSL was hard to learn, produced flat lists, and generated test cases implicitly through lengthy frame expansion.
>
> CTM addresses these limitations with three key improvements:
>
> ```mermaid
> flowchart LR
>     subgraph "Category-Partition (1988)"
>         A1["Specification"] --> A2["TSL Text"]
>         A2 --> A3["Constraints"]
>         A3 --> A4["Generated<br>Test Frames"]
>     end
>
>     subgraph "Classification Tree Method (1993)"
>         B1["Specification"] --> B2["Tree Diagram"]
>         B2 --> B3["Combination<br>Table"]
>         B3 --> B4["Test Cases"]
>     end
>
>     style A1 fill:#fff3cd,stroke:#333
>     style A4 fill:#fff3cd,stroke:#333
>     style B1 fill:#c8e6c9,stroke:#333
>     style B4 fill:#c8e6c9,stroke:#333
> ```
>
> | Aspect | Category-Partition | Classification Tree Method |
> |--------|:--:|:--:|
> | **Notation** | Textual (TSL syntax) | Graphical (tree + table) |
> | **Structure** | Flat list of categories | Hierarchical tree |
> | **Test case creation** | Start large, add restrictions | Start minimal, add until sufficient |
> | **Specification** | Implicit (lengthy generated lists) | Direct (compact combination table) |
> | **Hierarchy support** | Complex constraints needed | Built into tree structure |
>
> > "The crucial activity during testing is test case determination, since it determines the kind and scope of the examination and thus the quality of the test."

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 121 — Q2

> [!question] Question
> A colleague says "We don't need CTM — our testers are experienced and know what to test." How would you respond using evidence?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.4 Does CTM Work? Empirical Evidence
>
> Yu et al.  conducted the **only controlled empirical study** of CTM with 162 students (104 full-time + 58 part-time). After just 3 hours of training:
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "title": "Testing Method Preference: Before vs. After CTM Training",
>   "width": 400,
>   "height": 250,
>   "data": {
>     "values": [
>       {"Method": "White-box", "Phase": "Before Training", "Percentage": 53},
>       {"Method": "White-box", "Phase": "After Training", "Percentage": 18},
>       {"Method": "BVA", "Phase": "Before Training", "Percentage": 12},
>       {"Method": "BVA", "Phase": "After Training", "Percentage": 8},
>       {"Method": "EP", "Phase": "Before Training", "Percentage": 15},
>       {"Method": "EP", "Phase": "After Training", "Percentage": 5},
>       {"Method": "CTM", "Phase": "Before Training", "Percentage": 0},
>       {"Method": "CTM", "Phase": "After Training", "Percentage": 66},
>       {"Method": "Other", "Phase": "Before Training", "Percentage": 20},
>       {"Method": "Other", "Phase": "After Training", "Percentage": 3}
>     ]
>   },
>   "mark": "bar",
>   "encoding": {
>     "x": {"field": "Method", "type": "nominal", "axis": {"labelAngle": 0}},
>     "y": {"field": "Percentage", "type": "quantitative", "title": "% of students"},
>     "xOffset": {"field": "Phase", "type": "nominal"},
>     "color": {
>       "field": "Phase",
>       "type": "nominal",
>       "scale": {"range": ["#fff3cd", "#019546"]}
>     }
>   }
> }
> ```
>
> | Metric | Result |
> |--------|--------|
> | Preferred CTM over ad hoc | **66%** |
> | Perceived CTM as systematic | **63%** |
> | Valued graphical representation | **54%** |
> | Ad hoc fault detection | Only **55%** of faulty programs |
>
> …
>
> #### Controlled Study: CTM vs. Ad Hoc Testing
>
> The only controlled empirical evaluation of CTM  studied 162 students (two groups: 104 + 58) before and after a 3-hour CTM training session:
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "title": "Testing Method Preference: Before vs. After CTM Training",
>   "width": 400,
>   "height": 250,
>   "data": {
>     "values": [
>       {"Method": "White-box", "Phase": "Before Training", "Percentage": 53},
>       {"Method": "White-box", "Phase": "After Training", "Percentage": 18},
>       {"Method": "BVA", "Phase": "Before Training", "Percentage": 12},
>       {"Method": "BVA", "Phase": "After Training", "Percentage": 8},
>       {"Method": "EP", "Phase": "Before Training", "Percentage": 15},
>       {"Method": "EP", "Phase": "After Training", "Percentage": 5},
>       {"Method": "CTM", "Phase": "Before Training", "Percentage": 0},
>       {"Method": "CTM", "Phase": "After Training", "Percentage": 66},
>       {"Method": "Other", "Phase": "Before Training", "Percentage": 20},
>       {"Method": "Other", "Phase": "After Training", "Percentage": 3}
>     ]
>   },
>   "mark": "bar",
>   "encoding": {
>     "x": {"field": "Method", "type": "nominal", "axis": {"labelAngle": 0}},
>     "y": {"field": "Percentage", "type": "quantitative", "title": "% of students"},
>     "xOffset": {"field": "Phase", "type": "nominal"},
>     "color": {
>       "field": "Phase",
>       "type": "nominal",
>       "scale": {"range": ["#fff3cd", "#019546"]}
>     }
>   }
> }
> ```
>
> | Finding | Value |
> |---------|:--:|
> | Initially preferred white-box | 53% |
> | Preferred CTM after 3h training | **~66%** |
> | Perceived CTM as systematic | 63% |
> | Perceived CTM as complete | 56% |
> | Original suites' fault detection | 55% |
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 122 — Q3

> [!question] Question
> Evaluate the strength of empirical evidence for CTM. What are its limitations?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.4 Does CTM Work? Empirical Evidence
>
> Yu et al.  conducted the **only controlled empirical study** of CTM with 162 students (104 full-time + 58 part-time). After just 3 hours of training:
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "title": "Testing Method Preference: Before vs. After CTM Training",
>   "width": 400,
>   "height": 250,
>   "data": {
>     "values": [
>       {"Method": "White-box", "Phase": "Before Training", "Percentage": 53},
>       {"Method": "White-box", "Phase": "After Training", "Percentage": 18},
>       {"Method": "BVA", "Phase": "Before Training", "Percentage": 12},
>       {"Method": "BVA", "Phase": "After Training", "Percentage": 8},
>       {"Method": "EP", "Phase": "Before Training", "Percentage": 15},
>       {"Method": "EP", "Phase": "After Training", "Percentage": 5},
>       {"Method": "CTM", "Phase": "Before Training", "Percentage": 0},
>       {"Method": "CTM", "Phase": "After Training", "Percentage": 66},
>       {"Method": "Other", "Phase": "Before Training", "Percentage": 20},
>       {"Method": "Other", "Phase": "After Training", "Percentage": 3}
>     ]
>   },
>   "mark": "bar",
>   "encoding": {
>     "x": {"field": "Method", "type": "nominal", "axis": {"labelAngle": 0}},
>     "y": {"field": "Percentage", "type": "quantitative", "title": "% of students"},
>     "xOffset": {"field": "Phase", "type": "nominal"},
>     "color": {
>       "field": "Phase",
>       "type": "nominal",
>       "scale": {"range": ["#fff3cd", "#019546"]}
>     }
>   }
> }
> ```
>
> | Metric | Result |
> |--------|--------|
> | Preferred CTM over ad hoc | **66%** |
> | Perceived CTM as systematic | **63%** |
> | Valued graphical representation | **54%** |
> | Ad hoc fault detection | Only **55%** of faulty programs |
>
> …
>
> #### Why CTM?
>
> Before CTM, the **Category-Partition Method**  used a textual formalism (TSL — Test Specification Language) to define categories, choices, and constraints. While systematic, TSL was hard to learn, produced flat lists, and generated test cases implicitly through lengthy frame expansion.
>
> CTM addresses these limitations with three key improvements:
>
> ```mermaid
> flowchart LR
>     subgraph "Category-Partition (1988)"
>         A1["Specification"] --> A2["TSL Text"]
>         A2 --> A3["Constraints"]
>         A3 --> A4["Generated<br>Test Frames"]
>     end
>
>     subgraph "Classification Tree Method (1993)"
>         B1["Specification"] --> B2["Tree Diagram"]
>         B2 --> B3["Combination<br>Table"]
>         B3 --> B4["Test Cases"]
>     end
>
>     style A1 fill:#fff3cd,stroke:#333
>     style A4 fill:#fff3cd,stroke:#333
>     style B1 fill:#c8e6c9,stroke:#333
>     style B4 fill:#c8e6c9,stroke:#333
> ```
>
> | Aspect | Category-Partition | Classification Tree Method |
> |--------|:--:|:--:|
> | **Notation** | Textual (TSL syntax) | Graphical (tree + table) |
> | **Structure** | Flat list of categories | Hierarchical tree |
> | **Test case creation** | Start large, add restrictions | Start minimal, add until sufficient |
> | **Specification** | Implicit (lengthy generated lists) | Direct (compact combination table) |
> | **Hierarchy support** | Complex constraints needed | Built into tree structure |
>
> > "The crucial activity during testing is test case determination, since it determines the kind and scope of the examination and thus the quality of the test."

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 123 — Q4

> [!question] Question
> Why do the industrial results showing >90% test reduction not necessarily mean CTM is 90% more efficient?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.4 Does CTM Work? Empirical Evidence
>
> Yu et al.  conducted the **only controlled empirical study** of CTM with 162 students (104 full-time + 58 part-time). After just 3 hours of training:
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "title": "Testing Method Preference: Before vs. After CTM Training",
>   "width": 400,
>   "height": 250,
>   "data": {
>     "values": [
>       {"Method": "White-box", "Phase": "Before Training", "Percentage": 53},
>       {"Method": "White-box", "Phase": "After Training", "Percentage": 18},
>       {"Method": "BVA", "Phase": "Before Training", "Percentage": 12},
>       {"Method": "BVA", "Phase": "After Training", "Percentage": 8},
>       {"Method": "EP", "Phase": "Before Training", "Percentage": 15},
>       {"Method": "EP", "Phase": "After Training", "Percentage": 5},
>       {"Method": "CTM", "Phase": "Before Training", "Percentage": 0},
>       {"Method": "CTM", "Phase": "After Training", "Percentage": 66},
>       {"Method": "Other", "Phase": "Before Training", "Percentage": 20},
>       {"Method": "Other", "Phase": "After Training", "Percentage": 3}
>     ]
>   },
>   "mark": "bar",
>   "encoding": {
>     "x": {"field": "Method", "type": "nominal", "axis": {"labelAngle": 0}},
>     "y": {"field": "Percentage", "type": "quantitative", "title": "% of students"},
>     "xOffset": {"field": "Phase", "type": "nominal"},
>     "color": {
>       "field": "Phase",
>       "type": "nominal",
>       "scale": {"range": ["#fff3cd", "#019546"]}
>     }
>   }
> }
> ```
>
> | Metric | Result |
> |--------|--------|
> | Preferred CTM over ad hoc | **66%** |
> | Perceived CTM as systematic | **63%** |
> | Valued graphical representation | **54%** |
> | Ad hoc fault detection | Only **55%** of faulty programs |
>
> …
>
> #### Industrial Case Studies
>
> | Domain | Application | Finding | Source |
> |--------|------------|---------|--------|
> | Aerospace | Airfield lighting system | 263 test cases for 2,700 modules | Grochtmann 1993 |
> | Logistics | Letter sorting machine | Halved test cases, found new errors | Grochtmann 1993 |
> | Automotive | Adaptive cruise control | Embedded testing with Tessy | Buechner 2009 |
> | Aviation/Space | Multiple systems | >90% test reduction via dependency rules | Lehmann 2000 |
> | Automotive | Engine control, central locking | TPT for continuous behavior testing | Bringmann 2008 |
>
> {: .important }
> All documented industrial applications are from the Daimler/Berner & Mattner ecosystem. Independent replications outside this group are notably absent.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 124 — Q5

> [!question] Question
> How does CTM relate to the broader context of combinatorial testing?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Controlled Study: CTM vs. Ad Hoc Testing
>
> The only controlled empirical evaluation of CTM  studied 162 students (two groups: 104 + 58) before and after a 3-hour CTM training session:
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "title": "Testing Method Preference: Before vs. After CTM Training",
>   "width": 400,
>   "height": 250,
>   "data": {
>     "values": [
>       {"Method": "White-box", "Phase": "Before Training", "Percentage": 53},
>       {"Method": "White-box", "Phase": "After Training", "Percentage": 18},
>       {"Method": "BVA", "Phase": "Before Training", "Percentage": 12},
>       {"Method": "BVA", "Phase": "After Training", "Percentage": 8},
>       {"Method": "EP", "Phase": "Before Training", "Percentage": 15},
>       {"Method": "EP", "Phase": "After Training", "Percentage": 5},
>       {"Method": "CTM", "Phase": "Before Training", "Percentage": 0},
>       {"Method": "CTM", "Phase": "After Training", "Percentage": 66},
>       {"Method": "Other", "Phase": "Before Training", "Percentage": 20},
>       {"Method": "Other", "Phase": "After Training", "Percentage": 3}
>     ]
>   },
>   "mark": "bar",
>   "encoding": {
>     "x": {"field": "Method", "type": "nominal", "axis": {"labelAngle": 0}},
>     "y": {"field": "Percentage", "type": "quantitative", "title": "% of students"},
>     "xOffset": {"field": "Phase", "type": "nominal"},
>     "color": {
>       "field": "Phase",
>       "type": "nominal",
>       "scale": {"range": ["#fff3cd", "#019546"]}
>     }
>   }
> }
> ```
>
> | Finding | Value |
> |---------|:--:|
> | Initially preferred white-box | 53% |
> | Preferred CTM after 3h training | **~66%** |
> | Perceived CTM as systematic | 63% |
> | Perceived CTM as complete | 56% |
> | Original suites' fault detection | 55% |
>
> …
>
> #### 5.5 Combinatorial Testing Limitations
>
> - Still need **proper partitioning** first (EP/BVA)
> - **Timing** issues not covered
> - **Masking** can hide faults
> - Tool-generated tests need **oracles**
>
> > **Best Practice:** Combine with equivalence partitioning and BVA - don't rely on combinatorial alone!

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 125 — Q6

> [!question] Question
> A test object violates the "restful" property — it retains state between invocations. What problems does this cause for CTM?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.1 Test Objects
>
> A **test object** must be **invocable** (can be called), **observable** (output can be verified), and **restful** (returns to initial state). The choice of test object determines which aspects are relevant — testing the *full conveyor system* means lighting matters; testing just the *image processing module* means only figure properties matter.
>
> {: .exam-tip }
> > **Exam Tip:** If a test object violates the "restful" property, tests become order-dependent — results change based on execution sequence, making systematic coverage unreliable.
>
> #### 3.1 Step 1: Select Test Object
>
> The test object choice shapes the entire tree:
>
> | Level | Test Object | Relevant Aspects | Irrelevant |
> |-------|------------|-------------------|------------|
> | **End-to-end** | Full conveyor system | Shape, Color, Size, Lighting, Background | -- |
> | **Module** | Image processing library | Shape, Color, Size | Lighting, Background |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 126 — Q7

> [!question] Question
> Given this specification, identify the test-relevant aspects and their classes: "A shipping calculator charges based on package weight (up to 50kg), destination (domestic/international), and delivery speed (standard 5-day, express 2-day, overnight). Packages over 50kg are rejected."

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.2 Aspects and Equivalence Classes
>
> An **aspect** is any property that might influence the test object's behavior. Use **probing questions** to discover them: "What inputs? What environment? What values differ? What boundaries? What can go wrong?"
>
> An **equivalence class** partitions aspect values into groups that produce **equivalent behavior**:
> 1. **Mutually exclusive** — no value belongs to multiple classes
> 2. **Collectively exhaustive** — every possible value is covered
>
> {: .exam-tip }
> > **Exam Tip:** Aspect identification is NOT mechanical — it requires creativity and domain insight. Use probing questions systematically.
>
> #### 2.4 Finding Equivalence Classes: Heuristics
>
> | Source | Method | Example |
> |--------|--------|---------|
> | **Specification** | One class per stated case | "Discounts for orders > $100" |
> | **Code paths** | One class per branch | `if/else` → 2 classes |
> | **Error types** | One class per error | Invalid format, overflow |
> | **Ranges** | Valid + boundary violations | 1-100 → {<1, 1-100, >100} |
> | **Membership** | Inside + outside groups | Prime vs composite |
> | **Outputs** | Classes producing same output | All inputs → "Error 404" |
>
> > **Smell:** If you're writing many similar test cases, they probably belong to the same equivalence class!

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 127 — Q8

> [!question] Question
> Explain the difference between composition and classification using a real-world example not from the lectures.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.4 Composition vs Classification
>
> This is one of the most important distinctions in CTM :
>
> ```mermaid
> flowchart LR
>     subgraph "Composition (consists of)"
>         C1["Car"] --> W["Wheels"]
>         C1 --> M["Motor"]
>         C1 --> CH["Chassis"]
>     end
>
>     subgraph "Classification (is a kind of)"
>         C2["Vehicle"] --> BUS["Bus"]
>         C2 --> TRUCK["Truck"]
>         C2 --> SEDAN["Sedan"]
>     end
>
>     style C1 fill:#2D6E2A,stroke:#333,color:white,stroke-width:3px
>     style C2 fill:#4a90d9,stroke:#333,color:white
> ```
>
> - **Composition** = parts list (a car *has* wheels, motor, chassis — ALL exist simultaneously)
> - **Classification** = multiple-choice (a vehicle *is* a bus, truck, or sedan — exactly ONE applies)
>
> **In the machine vision example:** **Figure** is a *composition* (has Shape, Color, AND Size). **Shape** is a *classification* (Triangle, Circle, OR Square).
>
> #### Composition vs. Classification
>
> The distinction is critical. Consider modeling a **Car** :
>
> ```mermaid
> flowchart LR
>     subgraph "Composition (consists of)"
>         C1["Car"] --> W["Wheels"]
>         C1 --> M["Motor"]
>         C1 --> CH["Chassis"]
>     end
>
>     subgraph "Classification (is a kind of)"
>         C2["Vehicle"] --> BUS["Bus"]
>         C2 --> TRUCK["Truck"]
>         C2 --> SEDAN["Sedan"]
>     end
>
>     style C1 fill:#2D6E2A,stroke:#333,color:white,stroke-width:3px
>     style C2 fill:#4a90d9,stroke:#333,color:white
> ```
>
> - A car **consists of** wheels, motor, and chassis — all exist simultaneously (composition)
> - A vehicle **is a kind of** bus, truck, or sedan — exactly one applies (classification)

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 128 — Q9

> [!question] Question
> Why must invalid cases be in a separate branch? Show what goes wrong with a concrete example if you put them inside each classification.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Modeling Invalid Cases
>
> For robust (negative) testing, invalid inputs must be included in the classification tree. The key principle: **invalid cases form a separate branch, parallel to valid aspects** — they are not scattered as individual leaves within each valid classification.
>
> ```mermaid
> flowchart TD
>     ROOT(["Machine Vision System"])
>     ROOT --> FIG["Figure"]
>
>     FIG --> INV{{"Invalid"}}
>     FIG --> VAL{{"Valid"}}
>
>     INV --> EXMP["Exemplars"]
>     EXMP --> hex(["Small hexagon"])
>     EXMP --> irreg(["Large irregular<br>shape"])
>     EXMP --> wclr(["Wrong color"])
>
>     VAL --> ATTR["Attributes"]
>     ATTR --> SHAPE{{"Shape"}}
>     ATTR --> COLOR{{"Color"}}
>     ATTR --> SIZE{{"Size"}}
>
>     SHAPE --> tri(["Triangle"])
>     SHAPE --> circ(["Circle"])
>     SHAPE --> sq(["Square"])
>
>     COLOR --> r(["Red"])
>     COLOR --> g(["Green"])
>     COLOR --> b(["Blue"])
>
>     SIZE --> sm(["Small"])
>     SIZE --> lg(["Large"])
>
>     style ROOT fill:#019546,stroke:#333,color:white
>     style FIG fill:#2D6E2A,stroke:#333,color:white,stroke-width:3px
>     style INV fill:#d32f2f,stroke:#333,color:white
>     style VAL fill:#019546,stroke:#333,color:white
>     style EXMP fill:#ffcdd2,stroke:#d32f2f,color:#333,stroke-width:3px
>     style ATTR fill:#2D6E2A,stroke:#333,color:white,stroke-width:3px
>     style SHAPE fill:#4a90d9,stroke:#333,color:white
>     style COLOR fill:#4a90d9,stroke:#333,color:white
>     style SIZE fill:#4a90d9,stroke:#333,color:white
> ```
>
> **Why a separate branch?** If invalid values sit inside each valid classification, they enter the **combinatorial explosion** — the test generator combines them with every valid value from other aspects, producing meaningless test cases like "undefined shape + red + small + bright + white." A separate branch ensures invalids are tested individually.
>
> …
>
> #### 2.5 Modeling Invalid Cases
>
> Invalid cases form a **separate branch**, parallel to valid aspects — NOT scattered as individual leaves within each classification.
>
> {% raw %}
> ```mermaid
> flowchart TD
>     ROOT(["Machine Vision System"])
>     ROOT --> FIG["Figure"]
>
>     FIG --> INV{{"Invalid"}}
>     FIG --> VAL{{"Valid"}}
>
>     INV --> EXMP["Exemplars"]
>     EXMP --> hex(["Small hexagon"])
>     EXMP --> irreg(["Large irregular<br>shape"])
>     EXMP --> wclr(["Wrong color"])
>
>     VAL --> ATTR["Attributes"]
>     ATTR --> SHAPE{{"Shape"}}
>     ATTR --> COLOR{{"Color"}}
>     ATTR --> SIZE{{"Size"}}
>
>     SHAPE --> tri(["Triangle"])
>     SHAPE --> circ(["Circle"])
>     SHAPE --> sq(["Square"])
>
>     COLOR --> r(["Red"])
>     COLOR --> g(["Green"])
>     COLOR --> b(["Blue"])
>
>     SIZE --> sm(["Small"])
>     SIZE --> lg(["Large"])
>
>     style ROOT fill:#019546,stroke:#333,color:white
>     style FIG fill:#2D6E2A,stroke:#333,color:white,stroke-width:3px
>     style INV fill:#d32f2f,stroke:#333,color:white
>     style VAL fill:#019546,stroke:#333,color:white
>     style EXMP fill:#ffcdd2,stroke:#d32f2f,color:#333,stroke-width:3px
>     style ATTR fill:#2D6E2A,stroke:#333,color:white,stroke-width:3px
>     style SHAPE fill:#4a90d9,stroke:#333,color:white
>     style COLOR fill:#4a90d9,stroke:#333,color:white
>     style SIZE fill:#4a90d9,stroke:#333,color:white
> ```
> {% endraw %}
>
> **Why?** If invalids sit inside each valid classification, the generator combines them with every valid value from other aspects — producing meaningless test cases. A separate branch ensures invalids are tested **individually**.
>
> **Decision guide:** If the application tests invalids one at a time, use a separate branch. If it processes combinations of valid and invalid inputs together (e.g., multi-field form validation), consider mixing.
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 129 — Q10

> [!question] Question
> Why are only classes test-selectable, and not compositions or classifications?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.2 Aspects and Equivalence Classes
>
> An **aspect** is any property that might influence the test object's behavior. Use **probing questions** to discover them: "What inputs? What environment? What values differ? What boundaries? What can go wrong?"
>
> An **equivalence class** partitions aspect values into groups that produce **equivalent behavior**:
> 1. **Mutually exclusive** — no value belongs to multiple classes
> 2. **Collectively exhaustive** — every possible value is covered
>
> {: .exam-tip }
> > **Exam Tip:** Aspect identification is NOT mechanical — it requires creativity and domain insight. Use probing questions systematically.
>
> #### 2.4 Finding Equivalence Classes: Heuristics
>
> | Source | Method | Example |
> |--------|--------|---------|
> | **Specification** | One class per stated case | "Discounts for orders > $100" |
> | **Code paths** | One class per branch | `if/else` → 2 classes |
> | **Error types** | One class per error | Invalid format, overflow |
> | **Ranges** | Valid + boundary violations | 1-100 → {<1, 1-100, >100} |
> | **Membership** | Inside + outside groups | Prime vs composite |
> | **Outputs** | Classes producing same output | All inputs → "Error 404" |
>
> > **Smell:** If you're writing many similar test cases, they probably belong to the same equivalence class!

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 130 — Q11

> [!question] Question
> What is the relationship between equivalence partitioning (EP) and CTM classes?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Equivalence Partitioning
>
> Equivalence Partitioning (EP) divides the input domain into classes where all values are expected to produce similar behavior. Testing one representative from each class provides confidence for the entire class.
>
> #### 2.2 Aspects and Equivalence Classes
>
> An **aspect** is any property that might influence the test object's behavior. Use **probing questions** to discover them: "What inputs? What environment? What values differ? What boundaries? What can go wrong?"
>
> An **equivalence class** partitions aspect values into groups that produce **equivalent behavior**:
> 1. **Mutually exclusive** — no value belongs to multiple classes
> 2. **Collectively exhaustive** — every possible value is covered
>
> {: .exam-tip }
> > **Exam Tip:** Aspect identification is NOT mechanical — it requires creativity and domain insight. Use probing questions systematically.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 131 — Q12

> [!question] Question
> You're testing a mobile banking app. How does choosing "the transfer screen" vs "the entire app" as test object change your classification tree?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.1 Step 1: Select Test Object
>
> The test object choice shapes the entire tree:
>
> | Level | Test Object | Relevant Aspects | Irrelevant |
> |-------|------------|-------------------|------------|
> | **End-to-end** | Full conveyor system | Shape, Color, Size, Lighting, Background | -- |
> | **Module** | Image processing library | Shape, Color, Size | Lighting, Background |
>
> #### Classification Tree Method
>
> The **Classification Tree Method (CTM)** is a systematic, graphical technique for designing test cases by partitioning the input domain of a test object into a tree structure and combining selections in a table. Introduced by Grochtmann and Grimm in 1993 , it transforms test design from an ad hoc activity into a structured, visual, and documentable process.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 132 — Q13

> [!question] Question
> Apply probing questions to the function `search(database, query, filters, sortBy)` and build a classification tree.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Step 1–3: Build the classification tree
>
> ```mermaid
> flowchart TD
>     ROOT(["City Tax<br>Calculator"])
>     ROOT --> RES{{"Residency"}}
>
>     RES --> NR(["Non-Resident"])
>     RES --> R(["Resident"])
>
>     R --> MS{{"Marital Status"}}
>     R --> GP{{"Gross Pay"}}
>
>     MS --> S(["Single"])
>     MS --> F(["Family"])
>
>     GP --> LOW(["#le; $30,000"])
>     GP --> MID(["$30,001–<br>$50,000"])
>     GP --> HIGH(["#gt; $50,000"])
>
>     style ROOT fill:#019546,stroke:#333,color:white
>     style RES fill:#4a90d9,stroke:#333,color:white
>     style MS fill:#4a90d9,stroke:#333,color:white
>     style GP fill:#4a90d9,stroke:#333,color:white
> ```
>
> #### Classification Tree Method
>
> The **Classification Tree Method (CTM)** is a systematic, graphical technique for designing test cases by partitioning the input domain of a test object into a tree structure and combining selections in a table. Introduced by Grochtmann and Grimm in 1993 , it transforms test design from an ad hoc activity into a structured, visual, and documentable process.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 133 — Q14

> [!question] Question
> Why does Grindal et al. recommend "Avoid" as the best constraint strategy? When might you choose "Replace" instead?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.4 Step 4: Constrain (Dependency Rules)
>
> Grindal et al.  studied four strategies for handling conflicts across **3,854 test suites**:
>
> ```mermaid
> flowchart TD
>     CONFLICT["Conflict<br>Detected"] --> AVOID["Avoid<br>(prevent selection)"]
>     CONFLICT --> REPLACE["Replace<br>(substitute value)"]
>     CONFLICT --> ABSTRACT["Abstract<br>(merge parameters)"]
>     CONFLICT --> SUBMODEL["Sub-Model<br>(split tree)"]
>
>     style AVOID fill:#c8e6c9,stroke:#388e3c,stroke-width:3px
>     style REPLACE fill:#fff3cd,stroke:#ffc107
>     style ABSTRACT fill:#fff3cd,stroke:#ffc107
>     style SUBMODEL fill:#fff3cd,stroke:#ffc107
> ```
>
> | Strategy | How It Works | Suite Size |
> |----------|-------------|-----------|
> | **Avoid** | Modify the generator to skip conflicts | **Smallest** |
> | **Replace** | Generate all, then clone & fix conflicts | 2nd best |
> | **Abstract** | Merge conflicting parameters into one | Larger |
> | **Sub-models** | Split into conflict-free sub-models | Largest |
>
> {: .exam-tip }
> > **Exam Tip:** Remember: **Avoid > Replace > Abstract > Sub-models** in terms of suite size efficiency. "Avoid" is the recommended default strategy.
>
> #### Strategy Comparison
>
> | Strategy | Points per Boundary | Detects | Formula |
> |----------|---------------------|---------|---------|
> | **Weak 1×1** | 1 ON + 1 OFF | Closure, shift | 2 per condition |
> | **Weak N×1** | N ON + 1 OFF | + tilt detection | (n+1) × b + 1 |
> | **Basic BVA** | 4 per variable | Standard faults | 4k + 1 |
> | **Robust BVA** | 6 per variable | + beyond-boundary | 6k + 1 |
>
> > **Practical minimum:** Weak 1×1 (one ON + one OFF per boundary condition).

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 134 — Q15

> [!question] Question
> Compare minimality and pairwise (2-wise) generation. When would you choose each?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Pairwise (2-Way) Testing
>
> **Concept:** Cover all pairs of parameter values without testing all combinations.
>
> …
>
> #### Step 4: Pairwise for Valid Combinations
>
> For the "happy path" (all inputs valid), use pairwise to cover parameter interactions:
>
> | Test | Amount | Card | Currency | Recurring |
> |------|--------|------|----------|-----------|
> | P1 | Small | Visa | USD | True |
> | P2 | Small | MasterCard | EUR | False |
> | P3 | Medium | Visa | EUR | False |
> | P4 | Medium | Amex | USD | True |
> | P5 | Large | MasterCard | GBP | True |
> | P6 | Large | Amex | EUR | False |
> | ... | ... | ... | ... | ... |
>
> **Result:** ~15 tests cover all pairwise interactions vs. 72 exhaustive combinations.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 135 — Q16

> [!question] Question
> What does E[T] = 0.26 mean in practical terms? How would you improve it?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Practical Example: Login System
>
> **Conditions:**
> - Username valid?
> - Password valid?
> - Account active?
>
> **Actions:**
> - Login success
> - Show "Invalid credentials"
> - Show "Account inactive"
>
> #### 3.4 Step 4: Constrain (Dependency Rules)
>
> Grindal et al.  studied four strategies for handling conflicts across **3,854 test suites**:
>
> ```mermaid
> flowchart TD
>     CONFLICT["Conflict<br>Detected"] --> AVOID["Avoid<br>(prevent selection)"]
>     CONFLICT --> REPLACE["Replace<br>(substitute value)"]
>     CONFLICT --> ABSTRACT["Abstract<br>(merge parameters)"]
>     CONFLICT --> SUBMODEL["Sub-Model<br>(split tree)"]
>
>     style AVOID fill:#c8e6c9,stroke:#388e3c,stroke-width:3px
>     style REPLACE fill:#fff3cd,stroke:#ffc107
>     style ABSTRACT fill:#fff3cd,stroke:#ffc107
>     style SUBMODEL fill:#fff3cd,stroke:#ffc107
> ```
>
> | Strategy | How It Works | Suite Size |
> |----------|-------------|-----------|
> | **Avoid** | Modify the generator to skip conflicts | **Smallest** |
> | **Replace** | Generate all, then clone & fix conflicts | 2nd best |
> | **Abstract** | Merge conflicting parameters into one | Larger |
> | **Sub-models** | Split into conflict-free sub-models | Largest |
>
> {: .exam-tip }
> > **Exam Tip:** Remember: **Avoid > Replace > Abstract > Sub-models** in terms of suite size efficiency. "Avoid" is the recommended default strategy.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 136 — Q17

> [!question] Question
> Chen et al. proved two formal guarantees about tree restructuring. Why are these guarantees important?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.7 Tree Quality -- The E[T] Metric
>
> Chen et al.  proposed a metric to measure tree quality:
>
> **Formula:** `E[T] = legitimate test cases / potential test cases`
>
> | Tree Version | Potential | Legitimate | E[T] | Waste |
> |-------------|----------|------------|------|-------|
> | Ad hoc tree | 108 | 28 | **0.26** | 74% infeasible |
> | Restructured tree | 60 | 28 | **0.47** | 53% infeasible |
>
> **Restructuring nearly doubles effectiveness** while preserving all 28 legitimate test cases. Formal guarantees:
> - **Preservation:** No legitimate test case is lost during restructuring
> - **Convergence:** The potential count never increases
>
> {: .exam-tip }
> > **Exam Tip:** E[T] = 0.26 means **74% of generated tests are wasted** on infeasible combinations. Restructuring (moving aspects to different tree levels) can dramatically improve this without losing coverage.
>
> #### Tree Quality: Effectiveness Metric
>
> Chen et al.  defined a metric for tree quality:
>
> > **E[T] = legitimate test cases / potential test cases**
>
> - **Legitimate:** combinations that exist in the real input domain
> - **Potential:** all combinations the tree can generate (including infeasible ones)
>
> Ad hoc trees can have E[T] as low as **0.17** — meaning 83% of generated test cases are wasted on impossible combinations. Systematic restructuring can **double** effectiveness.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 137 — Q18

> [!question] Question
> Build a classification tree for an ATM withdrawal function. Include at least 4 aspects and model invalid cases.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Modeling Invalid Cases
>
> For robust (negative) testing, invalid inputs must be included in the classification tree. The key principle: **invalid cases form a separate branch, parallel to valid aspects** — they are not scattered as individual leaves within each valid classification.
>
> ```mermaid
> flowchart TD
>     ROOT(["Machine Vision System"])
>     ROOT --> FIG["Figure"]
>
>     FIG --> INV{{"Invalid"}}
>     FIG --> VAL{{"Valid"}}
>
>     INV --> EXMP["Exemplars"]
>     EXMP --> hex(["Small hexagon"])
>     EXMP --> irreg(["Large irregular<br>shape"])
>     EXMP --> wclr(["Wrong color"])
>
>     VAL --> ATTR["Attributes"]
>     ATTR --> SHAPE{{"Shape"}}
>     ATTR --> COLOR{{"Color"}}
>     ATTR --> SIZE{{"Size"}}
>
>     SHAPE --> tri(["Triangle"])
>     SHAPE --> circ(["Circle"])
>     SHAPE --> sq(["Square"])
>
>     COLOR --> r(["Red"])
>     COLOR --> g(["Green"])
>     COLOR --> b(["Blue"])
>
>     SIZE --> sm(["Small"])
>     SIZE --> lg(["Large"])
>
>     style ROOT fill:#019546,stroke:#333,color:white
>     style FIG fill:#2D6E2A,stroke:#333,color:white,stroke-width:3px
>     style INV fill:#d32f2f,stroke:#333,color:white
>     style VAL fill:#019546,stroke:#333,color:white
>     style EXMP fill:#ffcdd2,stroke:#d32f2f,color:#333,stroke-width:3px
>     style ATTR fill:#2D6E2A,stroke:#333,color:white,stroke-width:3px
>     style SHAPE fill:#4a90d9,stroke:#333,color:white
>     style COLOR fill:#4a90d9,stroke:#333,color:white
>     style SIZE fill:#4a90d9,stroke:#333,color:white
> ```
>
> **Why a separate branch?** If invalid values sit inside each valid classification, they enter the **combinatorial explosion** — the test generator combines them with every valid value from other aspects, producing meaningless test cases like "undefined shape + red + small + bright + white." A separate branch ensures invalids are tested individually.
>
> …
>
> #### 2.5 Modeling Invalid Cases
>
> Invalid cases form a **separate branch**, parallel to valid aspects — NOT scattered as individual leaves within each classification.
>
> {% raw %}
> ```mermaid
> flowchart TD
>     ROOT(["Machine Vision System"])
>     ROOT --> FIG["Figure"]
>
>     FIG --> INV{{"Invalid"}}
>     FIG --> VAL{{"Valid"}}
>
>     INV --> EXMP["Exemplars"]
>     EXMP --> hex(["Small hexagon"])
>     EXMP --> irreg(["Large irregular<br>shape"])
>     EXMP --> wclr(["Wrong color"])
>
>     VAL --> ATTR["Attributes"]
>     ATTR --> SHAPE{{"Shape"}}
>     ATTR --> COLOR{{"Color"}}
>     ATTR --> SIZE{{"Size"}}
>
>     SHAPE --> tri(["Triangle"])
>     SHAPE --> circ(["Circle"])
>     SHAPE --> sq(["Square"])
>
>     COLOR --> r(["Red"])
>     COLOR --> g(["Green"])
>     COLOR --> b(["Blue"])
>
>     SIZE --> sm(["Small"])
>     SIZE --> lg(["Large"])
>
>     style ROOT fill:#019546,stroke:#333,color:white
>     style FIG fill:#2D6E2A,stroke:#333,color:white,stroke-width:3px
>     style INV fill:#d32f2f,stroke:#333,color:white
>     style VAL fill:#019546,stroke:#333,color:white
>     style EXMP fill:#ffcdd2,stroke:#d32f2f,color:#333,stroke-width:3px
>     style ATTR fill:#2D6E2A,stroke:#333,color:white,stroke-width:3px
>     style SHAPE fill:#4a90d9,stroke:#333,color:white
>     style COLOR fill:#4a90d9,stroke:#333,color:white
>     style SIZE fill:#4a90d9,stroke:#333,color:white
> ```
> {% endraw %}
>
> **Why?** If invalids sit inside each valid classification, the generator combines them with every valid value from other aspects — producing meaningless test cases. A separate branch ensures invalids are tested **individually**.
>
> **Decision guide:** If the application tests invalids one at a time, use a separate branch. If it processes combinations of valid and invalid inputs together (e.g., multi-field form validation), consider mixing.
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 138 — Q19

> [!question] Question
> In the tax example, what would go wrong if you modeled Residency, Marital Status, and Gross Pay as a flat tree (all at root level) instead of nesting Status and Pay under the Resident class? How does hierarchy eliminate infeasible combinations?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.1 City Tax Example -- Full Walkthrough
>
> **Step 1 -- Specification:**
>
> | Residency | Status | Gross Pay | Tax Rate |
> |-----------|--------|-----------|----------|
> | Non-resident | Any | Any | 1% |
> | Resident | Single | <= $30,000 | 1% |
> | Resident | Single | $30,000-$50,000 | 5% |
> | Resident | Single | > $50,000 | 15% |
> | Resident | Family | <= $50,000 | 1% |
> | Resident | Family | > $50,000 | 5% |
>
> **Step 2-3 -- Classification Tree:**
>
> All three aspects are independent classification axes at the root level:
>
> {% raw %}
> ```mermaid
> flowchart TD
>     ROOT(["City Tax<br>Calculator"])
>
>     ROOT --> RES{{"Residency"}}
>     ROOT --> MS{{"Marital Status"}}
>     ROOT --> GP{{"Gross Pay"}}
>
>     RES --> NR(["Non-Resident"])
>     RES --> R(["Resident"])
>
>     MS --> S(["Single"])
>     MS --> F(["Family"])
>
>     GP --> LOW(["≤ $30,000"])
>     GP --> MID(["$30,001–<br>$50,000"])
>     GP --> HIGH(["&gt; $50,000"])
>
>     style ROOT fill:#019546,stroke:#333,color:white
>     style RES fill:#4a90d9,stroke:#333,color:white
>     style MS fill:#4a90d9,stroke:#333,color:white
>     style GP fill:#4a90d9,stroke:#333,color:white
> ```
> {% endraw %}
>
> {: .important }
> This flat tree generates 2 × 2 × 3 = **12 potential combinations**. Six are infeasible (Non-Resident paired with any Status or Pay bracket). **Dependency rules** (Avoid strategy) filter them out before test generation.
>
> **Step 5 -- Combination Table:**
>
> | TC | Resident? | Status | Gross Pay | Expected Tax |
> |----|-----------|--------|-----------|-------------|
> | 1 | No | -- | -- | 1% |
> | 2 | Yes | Single | <= $30k | 1% |
> | 3 | Yes | Single | $30k-$50k | 5% |
> | 4 | Yes | Single | > $50k | 15% |
> | 5 | Yes | Family | <= $50k | 1% |
> | 6 | Yes | Family | > $50k | 5% |
>
> **Step 6 -- Concrete Test Cases:**
>
> …
>
> #### Step 1–3: Build the classification tree
>
> ```mermaid
> flowchart TD
>     ROOT(["City Tax<br>Calculator"])
>     ROOT --> RES{{"Residency"}}
>
>     RES --> NR(["Non-Resident"])
>     RES --> R(["Resident"])
>
>     R --> MS{{"Marital Status"}}
>     R --> GP{{"Gross Pay"}}
>
>     MS --> S(["Single"])
>     MS --> F(["Family"])
>
>     GP --> LOW(["#le; $30,000"])
>     GP --> MID(["$30,001–<br>$50,000"])
>     GP --> HIGH(["#gt; $50,000"])
>
>     style ROOT fill:#019546,stroke:#333,color:white
>     style RES fill:#4a90d9,stroke:#333,color:white
>     style MS fill:#4a90d9,stroke:#333,color:white
>     style GP fill:#4a90d9,stroke:#333,color:white
> ```

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 139 — Q20

> [!question] Question
> You have this abstract test specification: "Array: size > 1, unsorted, multiple occurrences, alphanumeric content. CountWhat: multiple characters." Provide three different valid concrete test cases.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.4 Test Specification vs Test Case
>
> | Test Specification (What) | Test Case (How) |
> |--------------------------|----------------|
> | Array size > 1 | `["world", "father", "father", "country"]` |
> | Occurrences > 1 | `countWhat = "father"` |
> | Unsorted | (order is not sorted) |
> | Alphanumeric content | (strings contain letters) |
> | **Abstract -- many valid concrete values** | **Concrete -- one specific execution, expected: 2** |
>
> **Best practice:** Delay parameterization. One abstract spec can generate many valid concrete test cases .
>
> #### Step 6: Concrete test cases
>
> | TC | Residency | Status | Gross Pay | Expected Tax Amount |
> |:--:|-----------|--------|----------:|--------------------:|
> | 1 | Non-Resident | — | $45,000 | $450 |
> | 2 | Resident | Single | $25,000 | $250 |
> | 3 | Resident | Single | $40,000 | $2,000 |
> | 4 | Resident | Single | $75,000 | $11,250 |
> | 5 | Resident | Family | $48,000 | $480 |
> | 6 | Resident | Family | $60,000 | $3,000 |
>
> {: .note }
> Notice how the tree structure **naturally handles the constraint**: Non-Residents don't need marital status or pay brackets. By placing those classifications under the Resident class, impossible combinations are eliminated structurally rather than with explicit rules.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 140 — Q21

> [!question] Question
> In the password validation example, why can't you use standard CTM combination generation? What special handling is needed?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.3 Password Validation Example
>
> Password validation requires **all aspects satisfied simultaneously** (intersection, not union):
>
> | Aspect | Classes |
> |--------|---------|
> | Length | <8 (invalid), 8-16 (valid), >16 (invalid) |
> | Numeric chars | None (invalid), Some (valid), All (invalid) |
> | Uppercase chars | None (invalid), Some (valid), All (invalid) |
>
> **Valid password** = Length(8-16) AND Numeric(Some) AND Uppercase(Some)
>
> Example valid value: `Passw0rD` — satisfies all three aspects simultaneously.
>
> #### Why CTM?
>
> Before CTM, the **Category-Partition Method**  used a textual formalism (TSL — Test Specification Language) to define categories, choices, and constraints. While systematic, TSL was hard to learn, produced flat lists, and generated test cases implicitly through lengthy frame expansion.
>
> CTM addresses these limitations with three key improvements:
>
> ```mermaid
> flowchart LR
>     subgraph "Category-Partition (1988)"
>         A1["Specification"] --> A2["TSL Text"]
>         A2 --> A3["Constraints"]
>         A3 --> A4["Generated<br>Test Frames"]
>     end
>
>     subgraph "Classification Tree Method (1993)"
>         B1["Specification"] --> B2["Tree Diagram"]
>         B2 --> B3["Combination<br>Table"]
>         B3 --> B4["Test Cases"]
>     end
>
>     style A1 fill:#fff3cd,stroke:#333
>     style A4 fill:#fff3cd,stroke:#333
>     style B1 fill:#c8e6c9,stroke:#333
>     style B4 fill:#c8e6c9,stroke:#333
> ```
>
> | Aspect | Category-Partition | Classification Tree Method |
> |--------|:--:|:--:|
> | **Notation** | Textual (TSL syntax) | Graphical (tree + table) |
> | **Structure** | Flat list of categories | Hierarchical tree |
> | **Test case creation** | Start large, add restrictions | Start minimal, add until sufficient |
> | **Specification** | Implicit (lengthy generated lists) | Direct (compact combination table) |
> | **Hierarchy support** | Complex constraints needed | Built into tree structure |
>
> > "The crucial activity during testing is test case determination, since it determines the kind and scope of the examination and thus the quality of the test."

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 141 — Q22

> [!question] Question
> Identify the constraints (infeasible combinations) in the count() function tree. How would you handle them?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.3 Count Function Tree
>
> {% raw %}
> ```mermaid
> flowchart TD
>     ROOT(["count(array, what)"])
>
>     ROOT --> ARR["Array"]
>     ROOT --> CW["countWhat"]
>
>     ARR --> SZ{{"Size"}}
>     ARR --> OCC{{"Occurrences"}}
>     ARR --> ORD{{"Order"}}
>     ARR --> CNT{{"Content Type"}}
>
>     SZ --> sz0(["0<br>(empty)"])
>     SZ --> sz1(["1"])
>     SZ --> szN(["&gt; 1"])
>
>     OCC --> oNone(["None"])
>     OCC --> oOne(["One"])
>     OCC --> oMany(["&gt; One"])
>
>     ORD --> sorted(["Sorted"])
>     ORD --> unsorted(["Unsorted"])
>
>     CNT --> num(["Numeric"])
>     CNT --> alpha(["Alpha"])
>     CNT --> alnum(["Alphanumeric"])
>
>     CW --> LEN{{"Length"}}
>     LEN --> empty(["Empty"])
>     LEN --> one(["1 char"])
>     LEN --> multi(["&gt; 1 char"])
>
>     style ROOT fill:#019546,stroke:#333,color:white
>     style ARR fill:#2D6E2A,stroke:#333,color:white,stroke-width:3px
>     style CW fill:#2D6E2A,stroke:#333,color:white,stroke-width:3px
>     style SZ fill:#4a90d9,stroke:#333,color:white
>     style OCC fill:#4a90d9,stroke:#333,color:white
>     style ORD fill:#4a90d9,stroke:#333,color:white
>     style CNT fill:#4a90d9,stroke:#333,color:white
>     style LEN fill:#4a90d9,stroke:#333,color:white
> ```
> {% endraw %}
>
> **Combinatorial count:** 3 x 2 x 3 x 3 x 3 = **162 potential combinations** (valid only). Many are **infeasible** — e.g., "Array size = 0" AND "Occurrences = Many" is impossible. This is where constraints come in.
>
> **Constraints (impossible combinations):**
>
> | Constraint | Reason |
> |------------|--------|
> | Size = 0 -> Occurrences = None | Empty array cannot contain the value |
> | Size = 0 -> Order is irrelevant | Cannot sort an empty array |
> | Size = 1 -> Occurrences in {None, One} | Single element: either matches or doesn't |
> | Size = 1 -> Order is irrelevant | Single element is trivially sorted |
>
> #### Constraints (impossible combinations)
>
> This example shows why **dependency rules** are essential:
>
> | Constraint | Reason |
> |------------|--------|
> | Size = 0 → Occurrences = None | Empty array cannot contain the value |
> | Size = 0 → Order is irrelevant | Cannot sort an empty array |
> | Size = 1 → Occurrences ∈ {None, One} | Single element: either matches or doesn't |
> | Size = 1 → Order is irrelevant | Single element is trivially sorted |
>
> Without constraints, the tree produces **3 × 3 × 2 × 3 × 3 = 162** combinations. Many are impossible (e.g., empty array with multiple occurrences). Constraints reduce this to a manageable and meaningful test suite.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 142 — Q23

> [!question] Question
> You have a web form with 4 tabs, each with different fields. Should you create one big tree or four separate trees? What are the trade-offs?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.7 Tree Quality -- The E[T] Metric
>
> Chen et al.  proposed a metric to measure tree quality:
>
> **Formula:** `E[T] = legitimate test cases / potential test cases`
>
> | Tree Version | Potential | Legitimate | E[T] | Waste |
> |-------------|----------|------------|------|-------|
> | Ad hoc tree | 108 | 28 | **0.26** | 74% infeasible |
> | Restructured tree | 60 | 28 | **0.47** | 53% infeasible |
>
> **Restructuring nearly doubles effectiveness** while preserving all 28 legitimate test cases. Formal guarantees:
> - **Preservation:** No legitimate test case is lost during restructuring
> - **Convergence:** The potential count never increases
>
> {: .exam-tip }
> > **Exam Tip:** E[T] = 0.26 means **74% of generated tests are wasted** on infeasible combinations. Restructuring (moving aspects to different tree levels) can dramatically improve this without losing coverage.
>
> #### Tree Notation
>
> A classification tree uses four node types to model the input domain. Here is a complete example — a **machine vision system** that classifies figures on a conveyor belt (valid aspects only — see [Modeling Invalid Cases](#modeling-invalid-cases) below for the full tree with invalid exemplars):
>
> ```mermaid
> flowchart TD
>     ROOT(["Machine Vision System"])
>
>     ROOT --> FIG["Figure"]
>     ROOT --> ENV["Environment"]
>
>     FIG --> SHAPE{{"Shape"}}
>     FIG --> COLOR{{"Color"}}
>     FIG --> SIZE{{"Size"}}
>
>     SHAPE --> tri(["Triangle"])
>     SHAPE --> circ(["Circle"])
>     SHAPE --> sq(["Square"])
>
>     COLOR --> r(["Red"])
>     COLOR --> g(["Green"])
>     COLOR --> b(["Blue"])
>
>     SIZE --> sm(["Small<br>#le;300px"])
>     SIZE --> lg(["Large<br>#gt;300px"])
>
>     ENV --> LIGHT{{"Lighting"}}
>     ENV --> BG{{"Background"}}
>
>     LIGHT --> day(["Daylight"])
>     LIGHT --> art(["Artificial"])
>
>     BG --> white(["White"])
>     BG --> dark(["Dark"])
>
>     style ROOT fill:#019546,stroke:#333,color:white
>     style FIG fill:#2D6E2A,stroke:#333,color:white,stroke-width:3px
>     style ENV fill:#2D6E2A,stroke:#333,color:white,stroke-width:3px
>     style SHAPE fill:#4a90d9,stroke:#333,color:white
>     style COLOR fill:#4a90d9,stroke:#333,color:white
>     style SIZE fill:#4a90d9,stroke:#333,color:white
>     style LIGHT fill:#4a90d9,stroke:#333,color:white
>     style BG fill:#4a90d9,stroke:#333,color:white
> ```

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 143 — Q24

> [!question] Question
> Compare CTE XL and TESTONA. What capabilities does TESTONA add that make it more powerful for modern testing?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Pairwise (2-Way) Testing
>
> **Concept:** Cover all pairs of parameter values without testing all combinations.
>
> …
>
> #### Controlled Study: CTM vs. Ad Hoc Testing
>
> The only controlled empirical evaluation of CTM  studied 162 students (two groups: 104 + 58) before and after a 3-hour CTM training session:
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "title": "Testing Method Preference: Before vs. After CTM Training",
>   "width": 400,
>   "height": 250,
>   "data": {
>     "values": [
>       {"Method": "White-box", "Phase": "Before Training", "Percentage": 53},
>       {"Method": "White-box", "Phase": "After Training", "Percentage": 18},
>       {"Method": "BVA", "Phase": "Before Training", "Percentage": 12},
>       {"Method": "BVA", "Phase": "After Training", "Percentage": 8},
>       {"Method": "EP", "Phase": "Before Training", "Percentage": 15},
>       {"Method": "EP", "Phase": "After Training", "Percentage": 5},
>       {"Method": "CTM", "Phase": "Before Training", "Percentage": 0},
>       {"Method": "CTM", "Phase": "After Training", "Percentage": 66},
>       {"Method": "Other", "Phase": "Before Training", "Percentage": 20},
>       {"Method": "Other", "Phase": "After Training", "Percentage": 3}
>     ]
>   },
>   "mark": "bar",
>   "encoding": {
>     "x": {"field": "Method", "type": "nominal", "axis": {"labelAngle": 0}},
>     "y": {"field": "Percentage", "type": "quantitative", "title": "% of students"},
>     "xOffset": {"field": "Phase", "type": "nominal"},
>     "color": {
>       "field": "Phase",
>       "type": "nominal",
>       "scale": {"range": ["#fff3cd", "#019546"]}
>     }
>   }
> }
> ```
>
> | Finding | Value |
> |---------|:--:|
> | Initially preferred white-box | 53% |
> | Preferred CTM after 3h training | **~66%** |
> | Perceived CTM as systematic | 63% |
> | Perceived CTM as complete | 56% |
> | Original suites' fault detection | 55% |
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 144 — Q25

> [!question] Question
> A novice tester creates a flat tree with 5 classifications at the root level, each with 4 classes. What problems will they face? How would you coach them?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Tree Notation
>
> A classification tree uses four node types to model the input domain. Here is a complete example — a **machine vision system** that classifies figures on a conveyor belt (valid aspects only — see [Modeling Invalid Cases](#modeling-invalid-cases) below for the full tree with invalid exemplars):
>
> ```mermaid
> flowchart TD
>     ROOT(["Machine Vision System"])
>
>     ROOT --> FIG["Figure"]
>     ROOT --> ENV["Environment"]
>
>     FIG --> SHAPE{{"Shape"}}
>     FIG --> COLOR{{"Color"}}
>     FIG --> SIZE{{"Size"}}
>
>     SHAPE --> tri(["Triangle"])
>     SHAPE --> circ(["Circle"])
>     SHAPE --> sq(["Square"])
>
>     COLOR --> r(["Red"])
>     COLOR --> g(["Green"])
>     COLOR --> b(["Blue"])
>
>     SIZE --> sm(["Small<br>#le;300px"])
>     SIZE --> lg(["Large<br>#gt;300px"])
>
>     ENV --> LIGHT{{"Lighting"}}
>     ENV --> BG{{"Background"}}
>
>     LIGHT --> day(["Daylight"])
>     LIGHT --> art(["Artificial"])
>
>     BG --> white(["White"])
>     BG --> dark(["Dark"])
>
>     style ROOT fill:#019546,stroke:#333,color:white
>     style FIG fill:#2D6E2A,stroke:#333,color:white,stroke-width:3px
>     style ENV fill:#2D6E2A,stroke:#333,color:white,stroke-width:3px
>     style SHAPE fill:#4a90d9,stroke:#333,color:white
>     style COLOR fill:#4a90d9,stroke:#333,color:white
>     style SIZE fill:#4a90d9,stroke:#333,color:white
>     style LIGHT fill:#4a90d9,stroke:#333,color:white
>     style BG fill:#4a90d9,stroke:#333,color:white
> ```
>
> #### 2.2 Aspects and Equivalence Classes
>
> An **aspect** is any property that might influence the test object's behavior. Use **probing questions** to discover them: "What inputs? What environment? What values differ? What boundaries? What can go wrong?"
>
> An **equivalence class** partitions aspect values into groups that produce **equivalent behavior**:
> 1. **Mutually exclusive** — no value belongs to multiple classes
> 2. **Collectively exhaustive** — every possible value is covered
>
> {: .exam-tip }
> > **Exam Tip:** Aspect identification is NOT mechanical — it requires creativity and domain insight. Use probing questions systematically.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 145 — Q26

> [!question] Question
> Which of the five common pitfalls is most dangerous, and why?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Common Pitfalls
>
> :
>
> | # | Pitfall | Frequency | Mitigation |
> |---|---------|-----------|------------|
> | 1 | **Infeasible test cases** | 60% of novices | Use dependency rules / constraints |
> | 2 | **Classification identification** | Common | Use probing questions systematically |
> | 3 | **Subjectivity** | 25% | Use E[T] metric to evaluate tree quality |
> | 4 | **Flat trees** | Common | Use composition nodes for hierarchy |
> | 5 | **Skipping boundary values** | Common | Combine CTM with BVA |
>
> **Most dangerous:** Infeasible test cases (pitfall #1). When 60% of novices create impossible combinations, the majority of generated tests are wasted.
>
> #### Common Pitfalls
>
> Based on empirical observations  :
>
> 1. **Infeasible test cases** (60% of novices) — use dependency rules or tree restructuring to eliminate impossible combinations
> 2. **Flat trees with no hierarchy** — use composition nodes to group related aspects
> 3. **Too many classifications at root level** — abstract, then refine; large trees can use sub-tree refinements
> 4. **Confusing composition with classification** — ask: "consists of" (parts) vs. "is a kind of" (variants)?
> 5. **Skipping boundary values** — apply BVA at class borders (e.g., $30,000 and $30,001)
> 6. **Over-specifying** — keep test cases as abstract specifications; delay concrete value assignment

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

### Card 146 — Q27

> [!question] Question
> How does CTM integrate with equivalence partitioning, boundary value analysis, and combinatorial testing? Draw the connections.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Boundary Value Analysis
>
> Boundary Value Analysis (BVA) focuses testing on the edges of equivalence partitions, where faults are most likely to occur. Off-by-one errors and incorrect boundary operators are among the most common programming mistakes.
>
> #### [Boundary Value Analysis](boundary.md)
>
> Test at partition boundaries where faults cluster:
> - **ON/OFF points**: Formal boundary testing strategy
> - **Fault types**: Closure, shift, tilt, missing, extra
> - **Formulas**: 4k+1 basic, 6k+1 robust

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/domain/RQ_A08_ClassificationTree.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/domain/RQ_A08_ClassificationTree.md)

## Static Analysis (22)

### Card 147 — Question 1: Zero Analysis Trace

> [!question] Question
> **Question 1: Zero Analysis Trace**
>
> Given the following code, trace the zero analysis to fixed point. Identify where (if anywhere) a divide-by-zero warning is issued.
> ```c
> a = 5;
> b = 0;
> if (condition) {
>     b = a;
> }
> c = a / b;   // Is b safe here?
> ```
> *Hint: What is b's abstract value after the if-else merge?*

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.2 The Abstract Domain for Zero Analysis
>
> We abstract the infinite set of integers into just three values:
>
> | Concrete Values | Abstract Value | Meaning |
> |----------------|----------------|---------|
> | $0$ | $Z$ (Zero) | Definitely zero |
> | Any $n \neq 0$ | $NZ$ (Not Zero) | Definitely not zero |
> | Unknown / mixed | $MZ$ (Maybe Zero) | Could be zero or not |
>
> **The lattice:** When two paths merge (e.g., after an if-else), we compute the *join* (least upper bound):
>
> **Join rules:**
> - $Z \sqcup Z = Z$
> - $NZ \sqcup NZ = NZ$
> - $Z \sqcup NZ = MZ$ (we don't know which path was taken)
> - $MZ \sqcup \text{anything} = MZ$
>
> #### CFG with Abstract States
>
> ```mermaid
> flowchart TD
>     B1["B1: x=10, y=x, z=0
>     x:NZ, y:NZ, z:Z"] --> B2["B2: y > -1?"]
>     B2 -- "true" --> B3["B3: x=x/y, y=y-1, z=5
>     ⚠ y:MZ at division!"]
>     B3 --> B2
>     B2 -- "false" --> B4["B4: exit
>     x:NZ, y:MZ, z:MZ"]
> ```
>
> **How the analysis proceeds:**
>
> 1. **Block B1:** Sequential assignments. After execution: x:NZ, y:NZ, z:Z.
>
> 2. **Block B2 (first visit):** State arrives from B1: {x:NZ, y:NZ, z:Z}. Condition `y > -1` does not change abstract state (our simple domain does not model comparison refinement for zero analysis).
>
> 3. **Block B3 (first iteration):** Division `x = x / y` with y:NZ is safe. Then `y = y - 1`: since y:NZ, subtracting 1 might make it zero, so y:MZ. Then `z = 5`: z:NZ. State leaving B3: {x:NZ, y:MZ, z:NZ}.
>
> 4. **Block B2 (second visit):** Now state from B1 and state from B3 must be **joined**:
>    - x: NZ join NZ = NZ
>    - y: NZ join MZ = MZ
>    - z: Z join NZ = MZ
>
> 5. **Block B3 (second iteration):** Division `x = x / y` with **y:MZ** -- the divisor might be zero. **Report warning: potential divide-by-zero.**
>
> 6. **Fixed point:** The abstract state no longer changes between iterations. Analysis terminates.
>
> > **Detection:** At `x = x / y` in B3, the divisor `y` has abstract value MZ. The analysis reports a warning for potential divide-by-zero. This is a genuine bug: when `y` counts down to 0, the loop condition `y > -1` is still true, and the division executes with y = 0.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 148 — Question 2: Product Automaton

> [!question] Question
> **Question 2: Product Automaton**
>
> Given a simple function with two lock/unlock calls:
> ```c
> lock(m);
> if (error) {
>     return;     // Does this violate locking discipline?
> }
> unlock(m);
> ```
> Construct the product automaton with the locking FSM ($P_0$ = unlocked, $P_1$ = locked, $P_2$ = error). Identify the error state.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### FSM for Locking Discipline
>
> The locking discipline can be expressed as a three-state finite automaton:
>
> ```mermaid
> stateDiagram-v2
>     [*] --> P0
>     P0 --> P1 : lock
>     P1 --> P0 : unlock
>     P1 --> P2 : lock (ERROR)
>     P0 --> P2 : unlock (ERROR)
>     P2 --> P2 : any
>
>     state "P0: Unlocked" as P0
>     state "P1: Locked" as P1
>     state "P2: Error" as P2
> ```
>
> - **P0 (Unlocked)**: The resource is not held. Only `lock` is valid.
> - **P1 (Locked)**: The resource is held. Only `unlock` is valid.
> - **P2 (Error)**: An invalid operation occurred. This is an absorbing state.
>
> #### 5.2 Locking Discipline: Three Rules
>
> A thread interacting with a shared resource via lock/unlock must obey three rules:
>
> 1. **No double lock:** Do not lock a resource you already hold
> 2. **No double unlock:** Do not unlock a resource you do not hold
> 3. **No terminate-while-locked:** Do not exit while still holding a lock
>
> **Property FSM (Finite State Machine):**
>
> | Transition | From | To | Meaning |
> |------------|------|----|---------|
> | `lock` | $P_0$ | $P_1$ | Valid: acquire lock |
> | `unlock` | $P_1$ | $P_0$ | Valid: release lock |
> | `unlock` | $P_0$ | $P_2$ | ERROR: double unlock |
> | `lock` | $P_1$ | $P_2$ | ERROR: double lock |
> | `end` | $P_1$ | $P_2$ | ERROR: terminate while locked |
>
> This FSM encodes the locking discipline as a specification. Any path that reaches $P_2$ represents a violation.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 149 — Question 3: Soundness vs Completeness

> [!question] Question
> **Question 3: Soundness vs Completeness**
>
> A tool reports "No bugs found" for a program that actually contains a null pointer dereference.
> - Is this tool sound? Why or why not?
> - Is this tool complete? Why or why not?
> - Give an example of a tool that would catch this vs miss it.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.2 Soundness vs Completeness
>
> These two properties define what guarantees an analysis provides:
>
> **Soundness (over-approximation):**
> - If the analysis says "no bugs," there truly are no bugs (of the checked kind)
> - May report bugs that do not actually exist (false positives)
> - "No false negatives" -- never misses a real bug
> - Analogy: a smoke detector that goes off for steam is sound -- it never misses real fire, but sometimes triggers falsely
>
> **Completeness (under-approximation):**
> - If the analysis reports a bug, it is truly a bug (every report is real)
> - May miss bugs that do exist (false negatives)
> - "No false positives" -- every warning is actionable
> - Analogy: testing is complete -- every failing test indicates a real problem, but passing tests do not prove absence of bugs
>
> #### Null Pointer Analysis
>
> The same framework applies to null pointer detection with a different abstract domain: **{Null, NotNull, MaybeNull}**.
>
> ```java
> Integer x = new Integer(6);  // x:NotNull
> Integer y = bar();           // y:MaybeNull (unknown return)
> if (y != null) {
>     // Branch refinement: y:NotNull in this branch
>     z = x.intVal() + y.intVal();  // Safe: both NotNull
> } else {
>     z = x.intVal();               // Safe: x:NotNull
>     y = x;                        // y:NotNull (copy from x)
>     x = null;                     // x:Null
> }
> // After merge: x is Null ⊔ NotNull = MaybeNull
> return z + x.intVal();            // ERROR: x is MaybeNull!
> ```
>
> **Branch refinement** is a key feature of null analysis: when code checks `y != null`, the analysis can narrow `y` from MaybeNull to NotNull in the true branch and to Null in the false branch. This dramatically reduces false positives.
>
> Facebook's **Infer** tool uses a sophisticated variant of this analysis based on **separation logic** to detect null dereferences and resource leaks at scale, running automatically on every code diff before it is submitted .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 150 — Question 4: Model Checking vs Dataflow

> [!question] Question
> **Question 4: Model Checking vs Dataflow**
>
> A concurrent program has a potential deadlock (Thread A locks resource 1 then waits for resource 2; Thread B locks resource 2 then waits for resource 1). Would you use dataflow analysis or model checking to detect this? Explain your reasoning.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Model Checking vs Static Analysis
>
> | Aspect | Static Analysis | Model Checking |
> |--------|-----------------|----------------|
> | **Execution** | No execution; reasons about code structure | Systematic state exploration |
> | **Concurrency** | Limited support | Excellent (primary use case) |
> | **Scalability** | Millions of LOC | State explosion limits scale |
> | **Guarantees** | May miss bugs (unsound) or report false alarms | Exhaustive within the model |
> | **Output** | Warning list with locations | Counterexample trace |
> | **Effort** | Low (automated tools) | Medium (model construction required) |
> | **Best for** | Broad bug detection across large codebases | Verifying specific properties of concurrent systems |
>
> In practice, model checking and static analysis are complementary. Static analysis tools like Coverity or CodeQL handle large codebases with shallow-to-medium analysis depth, while model checkers like SPIN verify critical concurrency properties with deep guarantees on smaller models.
>
> #### 5.1 What is Model Checking?
>
> Model checking is a formal verification technique that exhaustively explores all reachable states of a system to verify whether a property holds . If the property is violated, the model checker produces a **counterexample** -- a concrete execution path demonstrating the violation.
>
> **Four-step process:**
> 1. **Build model** -- represent the program as a state machine
> 2. **Specify property** -- express the requirement in temporal logic
> 3. **Exhaustively explore** -- check every reachable state
> 4. **Counterexample** -- if property violated, provide a witness path
>
> **Temporal logic (brief):**
> - **Safety:** $G(\neg \textit{bad})$ -- "Globally, the bad state never occurs." Example: never divide by zero.
> - **Liveness:** $G(\textit{request} \rightarrow F\;\textit{response})$ -- "Globally, every request is eventually followed by a response." Example: every lock is eventually unlocked.
>
> **When to use model checking vs dataflow analysis:**
>
> | Criterion | Dataflow Analysis | Model Checking |
> |-----------|-------------------|----------------|
> | Best for | Value tracking (null, zero, taint) | Protocol/behavioral properties |
> | Concurrency | Limited | Excellent (all interleavings) |
> | Scalability | Good (handles large codebases) | Limited (state explosion) |
> | Output | Warnings at specific lines | Counterexample traces |
> | Cost | Moderate | Expensive |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 151 — Question 5: Tool Disagreement

> [!question] Question
> **Question 5: Tool Disagreement**
>
> Lenarduzzi et al. (2021) found <0.4% agreement among six SA tools. What does this mean for a team that relies on a single tool like SonarQube? What would you recommend?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 6.3 The Tool Agreement Problem
>
> Lenarduzzi et al.  compared six Java SA tools on 47 projects (13.5 million warning instances):
>
> | Metric | Value |
> |--------|-------|
> | Line-level agreement | **<0.4%** |
> | Highest pairwise overlap | FindBugs + PMD: 9.4% |
> | 3+ tool agreement | **Zero** at line level |
>
> **Implications:**
> - "Our SonarQube is clean" does NOT mean "our code is bug-free"
> - Each tool sees different things -- they are complementary, not redundant
> - The ensemble approach (multiple tools) catches more bugs than any single tool
> - High precision does not mean comprehensive (CheckStyle is precise but narrow)
>
> #### The Tool Agreement Problem
>
> A critical finding from comparing six Java static analysis tools :
>
> | Tool | Precision | Focus |
> |------|-----------|-------|
> | SonarQube | 18% | Broadest coverage |
> | Better Code Hub | 29% | Design quality |
> | Coverity Scan | 37% | Fewer but more precise findings |
> | CheckStyle | 86% | Style only (trivial issues) |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 152 — Question 6: CEGAR Explanation

> [!question] Question
> **Question 6: CEGAR Explanation**
>
> Explain the CEGAR loop in your own words. Why does it start with a coarse abstraction instead of analyzing the full program? What happens when a counterexample is spurious?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.7 CEGAR: Counter-Example Guided Abstraction Refinement
>
> Real programs have too many states to explore exhaustively. **CEGAR** makes model checking practical by iteratively refining abstractions :
>
> **The CEGAR loop:**
>
> 1. **Abstract:** Create a coarse model of the program (ignore some details)
> 2. **Verify:** Run model checker on the abstract model
> 3. **Check counterexample:** Is the reported violation real or spurious?
>    - If **real:** report the bug (done)
>    - If **spurious:** the abstraction was too coarse
> 4. **Refine:** Add more detail to the abstraction to eliminate the spurious counterexample
> 5. **Repeat** from step 2 with the refined model
>
> **Why CEGAR works:** It only adds detail where needed. Most of the program can remain abstract; only the parts relevant to the bug need precision.
>
> #### The CEGAR Loop
>
> ```mermaid
> flowchart LR
>     A["Abstract<br>model"] --> B["Model<br>check"]
>     B -->|"Counterexample"| C{"Spurious?"}
>     C -->|"Yes"| D["Refine<br>abstraction"]
>     D --> A
>     C -->|"No"| E["Real Bug!"]
>     B -->|"Verified"| F["Safe"]
> ```
>
> 1. **Abstract** the program using a small set of predicates (e.g., "is x positive?")
> 2. **Model check** the abstract model
> 3. If a counterexample is found, check if it is **spurious** (an artifact of the abstraction that cannot occur in the real program)
> 4. If spurious: **refine** the abstraction by adding new predicates that distinguish the spurious behavior from real behavior
> 5. If real: **report the bug** with a concrete execution trace
> 6. Repeat until the property is verified or a real bug is found

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 153 — Question 7: The 10% FP Rule

> [!question] Question
> **Question 7: The 10% FP Rule**
>
> What is the 10% false positive rule? Who enforces it and how? Why is this threshold important for industrial adoption of SA tools? What happens when a tool exceeds it at Google?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The 10% False Positive Rule
>
> The single most important metric for static analysis adoption is not accuracy -- it is **developer tolerance for false positives**. Two large-scale industrial studies converge on the same threshold.
>
> **Google** enforces a strict false positive policy for all Tricorder analyzers :
>
> | Threshold | Action |
> |-----------|--------|
> | **< 10%** effective false positive rate | Analyzer remains active |
> | **> 10%** | Analyzer placed on **probation** |
> | **> 25%** | Analyzer **disabled immediately** |
>
> Platform-wide, Tricorder achieves approximately 5% "not useful" rate. Critically, Google measures **developer perception** -- the rate at which developers click "not useful" on findings -- rather than theoretical accuracy metrics.
>
> **eBay** reached the same threshold through a different path :
>
> | Phase | False Positive Rate | Developer Response |
> |-------|--------------------|--------------------|
> | Initial deployment (default config) | **50%** | Declared tool "useless" |
> | After customization (75% of checks disabled) | **10%** | Acceptance and adoption |
>
> > **Key insight:** The threshold for developer tolerance is remarkably consistent across organizations -- around 10%. Above this, developers simply ignore all warnings.
>
> #### 6.2 Google Tricorder: The 10% Rule in Practice
>
> Sadowski et al.  described Google's Tricorder platform:
>
> | Metric | Value |
> |--------|-------|
> | Daily findings | ~93,000 across 31,000 changelists |
> | False positive threshold | **<10%** effective "not useful" rate |
> | Probation trigger | >10% "not useful" rate |
> | Immediate disable | >25% "not useful" rate |
> | Platform-wide "not useful" rate | ~5% (<4% excluding probationary tools) |
> | Daily "PLEASE FIX" clicks | 716 |
>
> **Key design principles:**
> 1. **Measure usefulness, not accuracy** -- developer action is the metric
> 2. **Workflow integration** -- findings appear during code review, not in a separate dashboard
> 3. **Empower domain experts** -- engineers write custom analyzers for their subsystems
> 4. **Project-level customization** -- not per-user (maintains team consistency)
> 5. **Provide fixes, not just warnings** -- suggested auto-fixes lower the barrier to action
>
> > "The bottom line is that developers will decide whether an analysis tool has high impact, and what a false positive is."

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 154 — Question 8: Cost-Effectiveness Comparison

> [!question] Question
> **Question 8: Cost-Effectiveness Comparison**
>
> Compare the cost-effectiveness of static analysis, manual code inspection, and testing based on the Nortel study (Zheng 2006). When would you invest in SA vs additional testing? What types of defects does each approach find best?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Why Static Analysis Matters
>
> Static analysis provides unique advantages over dynamic techniques:
>
> | Benefit | Detail |
> |---------|--------|
> | **Early defect detection** | Find issues before code runs; finding defects during development is 10x cheaper than finding them in testing  |
> | **Comprehensive coverage** | Analyze all code paths, not just executed ones |
> | **Fast feedback** | Runs in seconds or minutes, not hours |
> | **Consistent standards** | Enforce coding rules automatically across teams |
> | **Zero runtime overhead** | No performance impact on production |
>
> **Industrial evidence**: Automated static analysis (ASA) achieves a defect yield of 23-37%, comparable to manual inspection, at 60-72% of the cost . When combined with testing and inspection, static analysis catches fault types that the other techniques miss.
>
> #### Relationship to Static Analysis and Testing
>
> Symbolic execution occupies a unique position on the analysis continuum:
>
> | Dimension | Pure Static Analysis | Symbolic Execution | Dynamic Testing |
> |-----------|---------------------|-------------------|-----------------|
> | **Inputs** | All (abstract) | Symbolic (forked per path) | Concrete (specific values) |
> | **Paths explored** | All (approximated) | Some (systematically selected) | One per test case |
> | **Precision** | Lower (over-approximation) | High (per-path exact) | Exact (for that input) |
> | **Coverage guarantee** | All code analyzed | Paths within budget | Only executed paths |
> | **False positives** | Yes (conservative) | Rare (path conditions verified) | None (observed behavior) |
> | **Automation** | Fully automatic | Fully automatic | Requires test design |
>
> **Compared with fuzzing**, symbolic execution is guided by program structure rather than random mutation. A fuzzer might spend hours trying random inputs without discovering that `y` must equal `x + 1`, while symbolic execution solves this constraint directly. However, fuzzers are faster per execution and handle complex environments more naturally.
>
> **Hybrid fuzzing** combines both strengths: use fast fuzzing for broad coverage, switch to symbolic execution when the fuzzer gets stuck at complex branch conditions. This approach is the current state of the art for automated vulnerability detection .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 155 — Question 9: Program Model Construction (Practical)

> [!question] Question
> **Question 9: Program Model Construction (Practical)**
>
> Produce a program model for the code below. Be sure to identify and describe the states, actions, transitions, initial state, and end states.
>
> ```c
> int x = 0;
> int y = 3;
> while (x < 3) {
>     x++;
>     y--;
> }
> ```

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### What is Model Checking?
>
> Model checking verifies a system by transforming both the program and its correctness property into finite automata, then systematically searching for a computation that violates the property. The technique was invented by Edmund Clarke, Allen Emerson, and Joseph Sifakis, who received the 2008 Turing Award for this contribution.
>
> **Key characteristics:**
> - **Exhaustive**: Explores all reachable states, not just sampled executions
> - **Automated**: No manual proof construction required
> - **Counterexamples**: When a property is violated, produces a concrete trace showing how the violation occurs
> - **Concurrency-focused**: Primary use case is verifying concurrent and distributed systems
>
> > Model checking verifies a program by using software to analyze its state space, as opposed to the mathematical deductive methods proposed by the pioneers of verification like C.A.R. Hoare .
>
> #### Model Checking vs Static Analysis
>
> | Aspect | Static Analysis | Model Checking |
> |--------|-----------------|----------------|
> | **Execution** | No execution; reasons about code structure | Systematic state exploration |
> | **Concurrency** | Limited support | Excellent (primary use case) |
> | **Scalability** | Millions of LOC | State explosion limits scale |
> | **Guarantees** | May miss bugs (unsound) or report false alarms | Exhaustive within the model |
> | **Output** | Warning list with locations | Counterexample trace |
> | **Effort** | Low (automated tools) | Medium (model construction required) |
> | **Best for** | Broad bug detection across large codebases | Verifying specific properties of concurrent systems |
>
> In practice, model checking and static analysis are complementary. Static analysis tools like Coverity or CodeQL handle large codebases with shallow-to-medium analysis depth, while model checkers like SPIN verify critical concurrency properties with deep guarantees on smaller models.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 156 — Question 10: Counterexamples in Model Checking

> [!question] Question
> **Question 10: Counterexamples in Model Checking**
>
> In the context of model checking, what is a counterexample? Why is it valuable for debugging? What is the difference between a real and a spurious counterexample?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.1 What is Model Checking?
>
> Model checking is a formal verification technique that exhaustively explores all reachable states of a system to verify whether a property holds . If the property is violated, the model checker produces a **counterexample** -- a concrete execution path demonstrating the violation.
>
> **Four-step process:**
> 1. **Build model** -- represent the program as a state machine
> 2. **Specify property** -- express the requirement in temporal logic
> 3. **Exhaustively explore** -- check every reachable state
> 4. **Counterexample** -- if property violated, provide a witness path
>
> **Temporal logic (brief):**
> - **Safety:** $G(\neg \textit{bad})$ -- "Globally, the bad state never occurs." Example: never divide by zero.
> - **Liveness:** $G(\textit{request} \rightarrow F\;\textit{response})$ -- "Globally, every request is eventually followed by a response." Example: every lock is eventually unlocked.
>
> **When to use model checking vs dataflow analysis:**
>
> | Criterion | Dataflow Analysis | Model Checking |
> |-----------|-------------------|----------------|
> | Best for | Value tracking (null, zero, taint) | Protocol/behavioral properties |
> | Concurrency | Limited | Excellent (all interleavings) |
> | Scalability | Good (handles large codebases) | Limited (state explosion) |
> | Output | Warnings at specific lines | Counterexample traces |
> | Cost | Moderate | Expensive |
>
> #### Model Checking
>
> Model checking is an algorithmic approach to formal verification that exhaustively explores all reachable states of a system to verify whether a given property holds. Unlike theorem proving, which requires manual proof construction, model checking is fully automated and produces **counterexample traces** when a property is violated -- making it one of the most practical formal methods available .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 157 — Question 11: When Model Checking Fails

> [!question] Question
> **Question 11: When Model Checking Fails**
>
> Under what circumstances is model checking *not* a useful strategy? Give at least 3 situations where a different analysis technique would be more appropriate.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Model Checking vs Static Analysis
>
> | Aspect | Static Analysis | Model Checking |
> |--------|-----------------|----------------|
> | **Execution** | No execution; reasons about code structure | Systematic state exploration |
> | **Concurrency** | Limited support | Excellent (primary use case) |
> | **Scalability** | Millions of LOC | State explosion limits scale |
> | **Guarantees** | May miss bugs (unsound) or report false alarms | Exhaustive within the model |
> | **Output** | Warning list with locations | Counterexample trace |
> | **Effort** | Low (automated tools) | Medium (model construction required) |
> | **Best for** | Broad bug detection across large codebases | Verifying specific properties of concurrent systems |
>
> In practice, model checking and static analysis are complementary. Static analysis tools like Coverity or CodeQL handle large codebases with shallow-to-medium analysis depth, while model checkers like SPIN verify critical concurrency properties with deep guarantees on smaller models.
>
> #### 5.1 What is Model Checking?
>
> Model checking is a formal verification technique that exhaustively explores all reachable states of a system to verify whether a property holds . If the property is violated, the model checker produces a **counterexample** -- a concrete execution path demonstrating the violation.
>
> **Four-step process:**
> 1. **Build model** -- represent the program as a state machine
> 2. **Specify property** -- express the requirement in temporal logic
> 3. **Exhaustively explore** -- check every reachable state
> 4. **Counterexample** -- if property violated, provide a witness path
>
> **Temporal logic (brief):**
> - **Safety:** $G(\neg \textit{bad})$ -- "Globally, the bad state never occurs." Example: never divide by zero.
> - **Liveness:** $G(\textit{request} \rightarrow F\;\textit{response})$ -- "Globally, every request is eventually followed by a response." Example: every lock is eventually unlocked.
>
> **When to use model checking vs dataflow analysis:**
>
> | Criterion | Dataflow Analysis | Model Checking |
> |-----------|-------------------|----------------|
> | Best for | Value tracking (null, zero, taint) | Protocol/behavioral properties |
> | Concurrency | Limited | Excellent (all interleavings) |
> | Scalability | Good (handles large codebases) | Limited (state explosion) |
> | Output | Warnings at specific lines | Counterexample traces |
> | Cost | Moderate | Expensive |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 158 — Question 12: LTL Properties

> [!question] Question
> **Question 12: LTL Properties**
>
> Let $F$ be a formula. Represent in LTL the following properties:
> a) $F$ holds in **all** states of a path $s_0, s_1, \ldots$
> b) $F$ holds in **some** future state
> c) Whenever a lock is acquired, it is **eventually** released: $G(\textit{lock} \rightarrow F(\textit{unlock}))$
>
> Explain each operator ($G$, $F$, $U$) in plain English.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### LTL Operators
>
> | Operator | Name | Meaning |
> |----------|------|---------|
> | **G** | Globally / Always | Property holds in all future states |
> | **F** | Finally / Eventually | Property holds in some future state |
> | **X** | Next | Property holds in the next state |
> | **U** | Until | Property holds until another property becomes true |
>
> **Example in SPIN syntax:**
> ```
> ltl no_deadlock { [] !deadlock }
> ltl response   { [] (request -> <> granted) }
> ```
>
> #### 5.1 What is Model Checking?
>
> Model checking is a formal verification technique that exhaustively explores all reachable states of a system to verify whether a property holds . If the property is violated, the model checker produces a **counterexample** -- a concrete execution path demonstrating the violation.
>
> **Four-step process:**
> 1. **Build model** -- represent the program as a state machine
> 2. **Specify property** -- express the requirement in temporal logic
> 3. **Exhaustively explore** -- check every reachable state
> 4. **Counterexample** -- if property violated, provide a witness path
>
> **Temporal logic (brief):**
> - **Safety:** $G(\neg \textit{bad})$ -- "Globally, the bad state never occurs." Example: never divide by zero.
> - **Liveness:** $G(\textit{request} \rightarrow F\;\textit{response})$ -- "Globally, every request is eventually followed by a response." Example: every lock is eventually unlocked.
>
> **When to use model checking vs dataflow analysis:**
>
> | Criterion | Dataflow Analysis | Model Checking |
> |-----------|-------------------|----------------|
> | Best for | Value tracking (null, zero, taint) | Protocol/behavioral properties |
> | Concurrency | Limited | Excellent (all interleavings) |
> | Scalability | Good (handles large codebases) | Limited (state explosion) |
> | Output | Warnings at specific lines | Counterexample traces |
> | Cost | Moderate | Expensive |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 159 — Question 13: Static vs Dynamic Analysis Tradeoffs

> [!question] Question
> **Question 13: Static vs Dynamic Analysis Tradeoffs**
>
> Give an example of a circumstance under which you would prefer:
> a) Dynamic analysis over static analysis?
> b) Static analysis over dynamic analysis?
> c) Model checking over more lightweight static analysis?
>
> Explain your reasoning for each choice.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Model Checking vs Static Analysis
>
> | Aspect | Static Analysis | Model Checking |
> |--------|-----------------|----------------|
> | **Execution** | No execution; reasons about code structure | Systematic state exploration |
> | **Concurrency** | Limited support | Excellent (primary use case) |
> | **Scalability** | Millions of LOC | State explosion limits scale |
> | **Guarantees** | May miss bugs (unsound) or report false alarms | Exhaustive within the model |
> | **Output** | Warning list with locations | Counterexample trace |
> | **Effort** | Low (automated tools) | Medium (model construction required) |
> | **Best for** | Broad bug detection across large codebases | Verifying specific properties of concurrent systems |
>
> In practice, model checking and static analysis are complementary. Static analysis tools like Coverity or CodeQL handle large codebases with shallow-to-medium analysis depth, while model checkers like SPIN verify critical concurrency properties with deep guarantees on smaller models.
>
> #### 2.1 Static vs Dynamic Analysis
>
> | Dimension | Static Analysis | Dynamic Analysis (Testing) |
> |-----------|-----------------|---------------------------|
> | **Execution** | Does not run the program | Runs the program on inputs |
> | **Coverage** | All paths (via abstraction) | Only exercised paths |
> | **False positives** | Yes (warns about infeasible paths) | No (every failure is real) |
> | **False negatives** | Possible (unsound tools exist) | Yes (misses untested paths) |
> | **Timing** | Before deployment | During or after execution |
> | **Concurrency** | Can reason about all interleavings | Tests specific schedules |
> | **Input dependence** | Independent of specific inputs | Depends entirely on test inputs |
> | **Cost scaling** | Scales with code size | Scales with input space |
>
> **Key definition:** Static analysis systematically examines an *abstraction* of the program state space. The word "abstraction" is critical -- we do not track exact values, we track simplified representations that capture the properties we care about.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 160 — Question 14: Tool Adoption Strategies

> [!question] Question
> **Question 14: Tool Adoption Strategies**
>
> Describe two strategies for eliciting developer support and encouraging static analysis tool adoption in an organization. Reference the Google Tricorder experience and the eBay FindBugs deployment.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Industrial Deployment of Static Analysis
>
> Deploying static analysis tools is as much an organizational challenge as a technical one. Tools that work well in research settings frequently fail in practice due to high false positive rates, lack of workflow integration, or poor initial rollout. This page examines what makes deployment succeed, drawing on case studies from Microsoft, eBay, Google, and Nortel Networks.
>
> #### Case Study: eBay FindBugs
>
> **Context:** Large Java e-commerce platform with millions of lines of code. Goal: reduce production bugs cost-effectively.
>
> **Timeline** :
>
> | Phase | Action | Result |
> |-------|--------|--------|
> | **1. Initial evaluation** | Deployed FindBugs with default configuration | **50% false positives** -- developers dismissed tool as "useless" |
> | **2. Customization** | 2 FTE spent evaluating and tuning checks | Disabled 75% of default checks (irrelevant to eBay's codebase) |
> | **3. Severity classification** | Classified remaining checks by severity | High / Medium / Low categories |
> | **4. Enforcement policy** | Defined action requirements per severity | See below |
>
> **Enforcement policy:**
>
> | Severity | Policy |
> |----------|--------|
> | **High** | Must fix before release |
> | **Medium** | No new issues allowed (fix-forward) |
> | **Low** | Limited enforcement |
>
> **Result:** 10% false positive rate, developer acceptance, cost approximately $400K/year -- equivalent to about 2 manual testers.
>
> **Lesson:** Static analysis scales to millions of LOC; manual testers do not. But trust is fragile -- a bad first experience poisons adoption for years. **Customization before deployment is essential**, not optional.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 161 — Question 15: Rice's Theorem Implications

> [!question] Question
> **Question 15: Rice's Theorem Implications**
>
> Rice's Theorem (1953) proves that all non-trivial semantic properties of programs are undecidable.
> - Explain what this means for static analysis tools in practice.
> - How do practical tools work despite this theoretical limitation?
> - What tradeoffs (soundness/completeness/termination) must every tool make?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.4 Rice's Theorem
>
> Rice  proved a fundamental impossibility result:
>
> > "Any nontrivial property about the language recognized by a Turing machine is undecidable."
>
> **In plain language:** For any interesting question about what a program does (Does it divide by zero? Does it terminate? Does it access invalid memory?), there is no algorithm that can always give the correct yes/no answer for every possible program.
>
> **Consequence for static analysis:** No analysis tool can simultaneously be:
> 1. **Sound** -- reports all bugs (no false negatives)
> 2. **Complete** -- reports only real bugs (no false positives)
> 3. **Terminating** -- always finishes in finite time
>
> Every practical tool must sacrifice at least one of these properties:
>
> | Tool Strategy | Sound? | Complete? | Terminates? | Example |
> |---------------|--------|-----------|-------------|---------|
> | Over-approximate (conservative) | Yes | No | Yes | Dataflow analysis, abstract interpretation |
> | Under-approximate (optimistic) | No | Yes | Yes | Testing, bounded model checking |
> | Precise but may not halt | Yes | Yes | No | Unbounded theorem provers |
> | Heuristic (practical) | No | No | Yes | Most commercial tools (FindBugs, PMD) |
>
> > **Exam Tip:** Most commercial tools are *neither* sound nor complete. They use heuristics to find common bugs quickly. This is a practical engineering choice, not a theoretical deficiency.
>
> #### Modern Static Analysis Tools
>
> Static analysis tools range from simple linters that check coding style to sophisticated platforms that detect deep security vulnerabilities across millions of lines of code. This page surveys the modern tool landscape, the lessons learned from industrial deployments at Google and Facebook, and the emerging frontier of LLM-assisted analysis.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 162 — Question 16: Taint Analysis

> [!question] Question
> **Question 16: Taint Analysis**
>
> Explain how taint analysis detects SQL injection vulnerabilities. Define: source, sink, and sanitizer. Trace the taint through this code:
>
> ```java
> String input = request.getParameter("id");   // source
> String query = "SELECT * FROM users WHERE id=" + input;
> db.execute(query);                           // sink
> ```
>
> Where should a sanitizer be applied?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.3 Taint Analysis
>
> Taint analysis is a specialized form of dataflow analysis used primarily for security. It tracks the flow of untrusted (user-controlled) data through the program .
>
> **The four-element model:**
> 1. **Source** -- where untrusted data enters (HTTP parameters, form fields, file reads)
> 2. **Propagation** -- how tainted data flows through variables and function calls
> 3. **Sanitizer** -- functions that make data safe (escaping, validation, encoding)
> 4. **Sink** -- dangerous operations where tainted data causes harm (SQL query, HTML output)
>
> **If tainted data reaches a sink without passing through a sanitizer, report a vulnerability.**
>
> | Vulnerability | Source | Sink | Sanitizer |
> |---------------|--------|------|-----------|
> | **SQL Injection** | HTTP parameter | SQL query execution | Parameterized query / escaping |
> | **XSS** | User input field | HTML output | HTML encoding |
> | **Command Injection** | Form field | `exec()` / `system()` | Input validation / whitelist |
> | **Path Traversal** | URL parameter | File open | Path canonicalization |
>
> **Vulnerable code (SQL injection):**
> ```java
> String query = "SELECT * FROM users WHERE id = " + request.getParameter("id");
> Statement stmt = conn.createStatement();
> stmt.execute(query);  // SINK: tainted data in SQL query!
> ```
>
> **Safe code:**
> ```java
> PreparedStatement stmt = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
> stmt.setString(1, request.getParameter("id"));  // Sanitized via parameterized query
> stmt.execute();
> ```
>
> **Tools for taint analysis:** CodeQL (GitHub), Semgrep, Fortify (Micro Focus)
>
> > **Exam Tip:** Be able to trace a taint flow from source to sink and identify where sanitization is needed. Know the four vulnerability types and their source/sink/sanitizer patterns.
>
> #### Taint Analysis
>
> Taint analysis tracks the flow of untrusted data from **sources** (user input, network, files) to security-sensitive **sinks** (SQL queries, shell commands, HTML output) .
>
> **The core idea:**
> 1. **Sources** introduce tainted data (e.g., `request.getParameter("id")`)
> 2. **Propagation rules** define how taint flows through operations (e.g., string concatenation preserves taint)
> 3. **Sanitizers** remove taint (e.g., `escapeHtml()`, parameterized queries)
> 4. **Sinks** are dangerous if reached by tainted data (e.g., `executeQuery(sql)`)
>
> If tainted data reaches a sink without passing through an appropriate sanitizer, the tool reports a vulnerability.
>
> **Common vulnerability patterns:**
>
> | Vulnerability | Source | Sink | Sanitizer |
> |---------------|--------|------|-----------|
> | SQL Injection | HTTP parameter | SQL query | Parameterized query |
> | Cross-Site Scripting (XSS) | User input | HTML output | `escapeHtml()` |
> | Command Injection | User input | `exec()` / `system()` | Input validation |
> | Path Traversal | URL parameter | File open | Path canonicalization |
>
> **Example -- SQL injection:**
>
> ```java
> // VULNERABLE: tainted data flows directly to sink
> String id = request.getParameter("id");           // Source (tainted)
> String sql = "SELECT * FROM users WHERE id=" + id; // Propagation
> stmt.executeQuery(sql);                            // Sink - ALERT!
>
> // SAFE: sanitizer (parameterized query) removes taint
> String id = request.getParameter("id");           // Source (tainted)
> PreparedStatement ps = conn.prepareStatement(
>     "SELECT * FROM users WHERE id=?");
> ps.setString(1, id);                              // Sanitizer
> ps.executeQuery();                                // Sink - OK
> ```
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 163 — Question 17: Symbolic Execution

> [!question] Question
> **Question 17: Symbolic Execution**
>
> Explain how symbolic execution differs from concrete testing. Given:
>
> ```c
> int f(int x, int y) {
>     if (x > 0 && y > 0) {
>         if (x + y > 100)
>             return -1;  // error path
>     }
>     return 0;
> }
> ```
>
> What symbolic constraints does the engine collect to reach the error path? What is path explosion, and how does KLEE mitigate it?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Concolic Testing: Concrete + Symbolic
>
> Pure symbolic execution can struggle with operations that are hard to model symbolically, such as hash functions, system calls, or complex library functions. **Concolic testing** (concrete + symbolic) combines both approaches :
>
> 1. **Run the program concretely** with an initial input (e.g., `x = 0, y = 0`)
> 2. **Collect symbolic constraints** along the executed path
> 3. **Negate one branch condition** in the path constraint
> 4. **Solve** the modified constraint to get a new input that takes a different path
> 5. **Repeat** until all reachable paths are explored or a budget is exhausted
>
> #### What is Symbolic Execution?
>
> In conventional testing, you run a program with concrete inputs (e.g., `x = 5, y = 3`) and observe the output. **Symbolic execution** instead assigns symbolic values to inputs (e.g., `x = alpha, y = beta`) and executes the program symbolically:
>
> - **Symbolic state:** Variables hold symbolic expressions instead of concrete values (e.g., `z = alpha + beta`)
> - **Path condition:** A logical formula that accumulates the constraints from each branch decision (e.g., `alpha > 0 AND beta = alpha + 1`)
> - **Path forking:** At each conditional branch, execution forks into two paths -- one where the condition is true and one where it is false
> - **SMT solving:** An **SMT solver** (Satisfiability Modulo Theories) such as Z3 or STP checks whether a path condition is satisfiable. If so, it produces a concrete input that exercises that path
>
> The result: symbolic execution can automatically generate test inputs that reach specific code locations, trigger specific branches, or expose specific bugs.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 164 — Question 18: AST Pattern Matching

> [!question] Question
> **Question 18: AST Pattern Matching**
>
> PMD detects bugs by matching patterns in the Abstract Syntax Tree. Explain:
> - What is an AST and how is it constructed from source code?
> - How does a rule like "Empty While Statement" work at the AST level?
> - What are the limitations of AST pattern matching compared to dataflow analysis?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### AST Pattern Matching
>
> A step deeper than lexical analysis, AST (Abstract Syntax Tree) pattern matching parses source code into a tree representation and matches subtrees against known bug patterns .
>
> **What it detects:**
> - Known bug patterns (null comparisons after dereference, double-checked locking)
> - Misuse of APIs (incorrect argument order, missing null checks)
> - Common coding mistakes (equality vs. assignment, fall-through in switch)
> - Unused variables, unreachable code, empty catch blocks
>
> **How it works:**
> 1. Parse source code into an AST
> 2. Walk the tree looking for subtree patterns that match known bugs
> 3. Report matches with location and description
>
> **Example -- Double-checked locking (Java):**
> ```java
> // Broken double-checked locking pattern
> if (instance == null) {
>     synchronized (lock) {
>         if (instance == null) {
>             instance = new Singleton(); // May be reordered!
>         }
>     }
> }
> ```
>
> A tool like SpotBugs (formerly FindBugs) recognizes this AST pattern and flags it because the Java Memory Model allows instruction reordering that can expose a partially constructed object.
>
> **Tools:** PMD (Java, multi-language), SpotBugs (Java bytecode), Semgrep (multi-language, custom rules)
>
> #### 3.1 AST Pattern Matching
>
> **How it works:**
> 1. Parse source code into an Abstract Syntax Tree (AST)
> 2. Walk the tree looking for subtrees that match known bug patterns
> 3. Report matches as potential defects
>
> **Example tools:**
> - **PMD** -- Matches AST patterns via XPath-like rules for Java, JavaScript, Apex
> - **SpotBugs** (successor to FindBugs) -- Bytecode pattern analysis for Java
> - **Semgrep** -- Lightweight pattern matching across many languages
>
> **Strengths:** Fast, easy to write new rules, low false positive rate for well-defined patterns.
>
> **Limitations:** Cannot reason about data flow or execution order. If a bug depends on the *sequence* of operations (lock then unlock), AST matching cannot detect it.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 165 — Question 19: Abstraction in Static Analysis

> [!question] Question
> **Question 19: Abstraction in Static Analysis**
>
> Explain how abstraction reduces the state space in static analysis. Use the zero analysis example: how does abstracting integers to $\{Z, NZ, MZ\}$ reduce $2^{96}$ possible 32-bit values to just 3 abstract values? Why does this guarantee termination?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.6 Abstraction Reduces State Space Exponentially
>
> **Without abstraction:** Consider 3 integer variables, each 32 bits. The concrete state space is $2^{32 \times 3} = 2^{96}$ -- approximately $10^{29}$ states. No computer can enumerate them all.
>
> **With zero analysis abstraction:** Each variable can be in one of 3 abstract states: $Z$ (Zero), $NZ$ (Not-Zero), or $MZ$ (Maybe-Zero). With 3 variables, the abstract state space is $3^3 = 27$ states (at most $2^6 = 64$ if we consider the lattice structure). This is tractable.
>
> **The tradeoff:** Abstraction loses information. We can no longer distinguish x=5 from x=42 -- both are NZ. This means some paths that are infeasible in reality will appear feasible in the abstract model, producing false positives. But the analysis becomes tractable and *terminates*.
>
> > **Key Takeaway:** Abstraction is what makes static analysis possible despite Rice's Theorem. We accept imprecision (false positives) in exchange for tractability and termination.
>
> #### 4.2 The Abstract Domain for Zero Analysis
>
> We abstract the infinite set of integers into just three values:
>
> | Concrete Values | Abstract Value | Meaning |
> |----------------|----------------|---------|
> | $0$ | $Z$ (Zero) | Definitely zero |
> | Any $n \neq 0$ | $NZ$ (Not Zero) | Definitely not zero |
> | Unknown / mixed | $MZ$ (Maybe Zero) | Could be zero or not |
>
> **The lattice:** When two paths merge (e.g., after an if-else), we compute the *join* (least upper bound):
>
> **Join rules:**
> - $Z \sqcup Z = Z$
> - $NZ \sqcup NZ = NZ$
> - $Z \sqcup NZ = MZ$ (we don't know which path was taken)
> - $MZ \sqcup \text{anything} = MZ$

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 166 — Question 20: LLM-Augmented Static Analysis

> [!question] Question
> **Question 20: LLM-Augmented Static Analysis**
>
> IRIS (Li 2024) combines LLMs with CodeQL and achieves +103% detection improvement. Explain:
> - Why do traditional SA tools struggle with certain vulnerability types?
> - How does the neuro-symbolic approach work (LLM + static analysis)?
> - What are the risks of relying on LLMs for security analysis?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### IRIS: LLM + CodeQL
>
> The IRIS system  demonstrates a **neuro-symbolic** approach that combines LLMs with traditional static analysis:
>
> **How it works:**
> 1. CodeQL performs formal taint analysis on the whole repository
> 2. LLM (GPT-4) **infers missing taint specifications** for third-party library APIs that CodeQL lacks
> 3. LLM performs **contextual analysis** to filter false positives
> 4. Formal analysis verifies paths end-to-end, maintaining soundness guarantees
>
> **Results on CWE-Bench-Java (120 validated vulnerabilities):**
>
> | Approach | Vulnerabilities Detected |
> |----------|------------------------|
> | CodeQL alone | 27 |
> | IRIS (LLM + CodeQL) | 55 (**+103%**) |
>
> IRIS also identified 4 previously unknown vulnerabilities that no existing tool could find. The key insight is that LLMs excel at understanding API semantics (what is a source? what is a sanitizer?) while formal analysis excels at tracing data flow through code.
>
> #### Modern Static Analysis Tools
>
> Static analysis tools range from simple linters that check coding style to sophisticated platforms that detect deep security vulnerabilities across millions of lines of code. This page surveys the modern tool landscape, the lessons learned from industrial deployments at Google and Facebook, and the emerging frontier of LLM-assisted analysis.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 167 — Question 21: Zero Analysis Walkthrough (Practical)

> [!question] Question
> **Question 21: Zero Analysis Walkthrough (Practical)**
>
> Trace the zero analysis for the following code. Show the abstract state at each program point and identify all warnings.
>
> ```c
> int a = 10;      // B1
> int b = a - 10;  // B1
> int c = 1;       // B1
> while (b < 5) {  // B2 (loop header)
>     c = c * b;   // B3
>     b = b + 1;   // B3
> }
> int d = a / c;   // B4 — is c safe here?
> ```
>
> Draw the CFG. What is the abstract value of $c$ at block B4? Does the analysis report a false positive?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### CFG with Abstract States
>
> ```mermaid
> flowchart TD
>     B1["B1: x=10, y=x, z=0
>     x:NZ, y:NZ, z:Z"] --> B2["B2: y > -1?"]
>     B2 -- "true" --> B3["B3: x=x/y, y=y-1, z=5
>     ⚠ y:MZ at division!"]
>     B3 --> B2
>     B2 -- "false" --> B4["B4: exit
>     x:NZ, y:MZ, z:MZ"]
> ```
>
> **How the analysis proceeds:**
>
> 1. **Block B1:** Sequential assignments. After execution: x:NZ, y:NZ, z:Z.
>
> 2. **Block B2 (first visit):** State arrives from B1: {x:NZ, y:NZ, z:Z}. Condition `y > -1` does not change abstract state (our simple domain does not model comparison refinement for zero analysis).
>
> 3. **Block B3 (first iteration):** Division `x = x / y` with y:NZ is safe. Then `y = y - 1`: since y:NZ, subtracting 1 might make it zero, so y:MZ. Then `z = 5`: z:NZ. State leaving B3: {x:NZ, y:MZ, z:NZ}.
>
> 4. **Block B2 (second visit):** Now state from B1 and state from B3 must be **joined**:
>    - x: NZ join NZ = NZ
>    - y: NZ join MZ = MZ
>    - z: Z join NZ = MZ
>
> 5. **Block B3 (second iteration):** Division `x = x / y` with **y:MZ** -- the divisor might be zero. **Report warning: potential divide-by-zero.**
>
> 6. **Fixed point:** The abstract state no longer changes between iterations. Analysis terminates.
>
> > **Detection:** At `x = x / y` in B3, the divisor `y` has abstract value MZ. The analysis reports a warning for potential divide-by-zero. This is a genuine bug: when `y` counts down to 0, the loop condition `y > -1` is still true, and the division executes with y = 0.
>
> #### 4.2 The Abstract Domain for Zero Analysis
>
> We abstract the infinite set of integers into just three values:
>
> | Concrete Values | Abstract Value | Meaning |
> |----------------|----------------|---------|
> | $0$ | $Z$ (Zero) | Definitely zero |
> | Any $n \neq 0$ | $NZ$ (Not Zero) | Definitely not zero |
> | Unknown / mixed | $MZ$ (Maybe Zero) | Could be zero or not |
>
> **The lattice:** When two paths merge (e.g., after an if-else), we compute the *join* (least upper bound):
>
> **Join rules:**
> - $Z \sqcup Z = Z$
> - $NZ \sqcup NZ = NZ$
> - $Z \sqcup NZ = MZ$ (we don't know which path was taken)
> - $MZ \sqcup \text{anything} = MZ$

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

### Card 168 — Question 22: Model Checking Locking (Practical)

> [!question] Question
> **Question 22: Model Checking Locking (Practical)**
>
> Given the following code with a locking FSM ($P_0$=unlocked, $P_1$=locked, $P_2$=error):
>
> ```c
> void process(int flag) {
>     lock(m);           // S0
>     do_work();         // S1
>     if (flag) {
>         lock(m);       // S2 — is this safe?
>     }
>     unlock(m);         // S3
> }
> ```
>
> a) Draw the CFG for the code
> b) Draw the product automaton (code states $\times$ lock states)
> c) Identify all paths that reach an error state $P_2$
> d) Is the counterexample real or spurious?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.6 Bug 2: Double Unlock (if-condition TRUE, loop exits)
>
> **Counterexample trace:**
> 1. Start: unlocked (P0)
> 2. S0: `lock()` -- acquire lock, now P1
> 3. S1: condition is true (request exists)
> 4. S2: `unlock()` -- release lock, now P0
> 5. S3: `nPackets != nPacketsOld` is false (one packet processed, counts differ -- wait, actually `nPackets` was incremented, so they differ and loop continues)
>
> Actually, let us trace more carefully: After processing one request, `nPackets` is incremented but `nPacketsOld` was set to the old value. So `nPackets != nPacketsOld` is TRUE and the loop continues. The loop exits only when no request is processed in an iteration. But that means the if-condition was false, which is Bug 1's scenario.
>
> **Revised trace for Bug 2:** Consider the case where the if-condition is true on the first iteration (unlock at S2) and then the if-condition is false on the second iteration (no unlock). Now `nPackets == nPacketsOld`, so the loop exits at S3. At this point, the lock is held (from the second iteration's lock at S0 without unlock). Then S4 does `unlock()` -- this is actually correct for this path.
>
> The double unlock scenario occurs if: after processing the last request (unlock at S2), the loop condition evaluates to exit (nPackets == nPacketsOld somehow), and then S4 does `unlock()` again. The model checker identifies the precise condition under which this path is feasible.
>
> **Path:** $P_0 \xrightarrow{\text{lock}(S_0)} P_1 \xrightarrow{\text{unlock}(S_2)} P_0 \xrightarrow{\text{exit}(S_3)} P_0 \xrightarrow{\text{unlock}(S_4)} \textbf{ERROR}$
>
> **Key insight:** Both bugs are non-local -- the lock and unlock operations are spread across different code locations and control flow paths. The product automaton mechanically reveals all paths to the error state.
>
> …
>
> #### 5.4 Product Automaton Construction
>
> The product automaton combines the code's CFG with the lock property FSM. Each state is a pair: (code location, lock state).
>
> **Step-by-step construction:**
>
> **Start:** $(S_0, P_0)$ -- at the lock statement, lock is not held
>
> **Path A: if-condition is TRUE (request exists and has status)**
>
> $$P_0S_0 \xrightarrow{\text{lock}} P_1S_1 \xrightarrow{\text{if true}} P_1S_2 \xrightarrow{\text{unlock}} P_0S_3 \xrightarrow{\text{exit}} P_0S_4 \xrightarrow{\text{unlock}} \textbf{ERROR}$$
>
> Double unlock! Lock was released at $S_2$, then released again at $S_4$.
>
> **Path B: if-condition is FALSE (no request or bad status)**
>
> $$P_0S_0 \xrightarrow{\text{lock}} P_1S_1 \xrightarrow{\text{if false}} P_1S_3 \xrightarrow{\text{loop}} P_1S_0 \xrightarrow{\text{lock}} \textbf{ERROR}$$
>
> Double lock! Lock was never released (if-body skipped), then acquired again on next iteration.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/static/RQ_A06_Static.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/static/RQ_A06_Static.md)

## Combinatorial Testing (15)

### Card 169 — Question 1: Covering Array Construction

> [!question] Question
> **Question 1: Covering Array Construction**
>
> Given a system with 3 parameters (A, B, C), each with 2 values (0, 1):
>
> a) List all possible 2-way (pairwise) combinations that must be covered.
> b) Construct a covering array that covers all pairs. What is the minimum number of rows?
> c) How does this compare to exhaustive testing (2³ = 8)?
>
> *Hint: There are C(3,2) × 2² = 12 pairs to cover.*

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Example: scaling parameters (pairwise, 3 values each)
>
> | Parameters | Exhaustive | Pairwise | Reduction |
> |------------|-----------|----------|-----------|
> | 10 | 59,049 | 15 | 3,937× |
> | 20 | 3.5 × 10⁹ | 18 | ~10⁸× |
> | 40 | 1.2 × 10¹⁹ | 21 | ~10¹⁸× |
> | 100 | 5.2 × 10⁴⁷ | 25 | ~10⁴⁶× |
>
> The logarithmic growth is what makes CT practical for real systems with dozens or hundreds of parameters .
>
> #### Example: 10 parameters × 3 values each
>
> | Strength | Exhaustive | Covering Array | Reduction |
> |----------|-----------|----------------|-----------|
> | 1-way | 30 | 3 | 10× |
> | 2-way | 810 | 15 | 54× |
> | 3-way | 19,683 | 33 | 596× |
> | 4-way | 531,441 | 54 | 9,841× |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/combinatorial/RQ_A07_Combinatorial.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/combinatorial/RQ_A07_Combinatorial.md)

### Card 170 — Question 2: Logarithmic Growth Explanation

> [!question] Question
> **Question 2: Logarithmic Growth Explanation**
>
> A system has 20 parameters, each with 3 values.
>
> a) How many exhaustive test cases exist?
> b) Approximately how many pairwise tests are needed? (Use the AETG result: ~18 tests for this configuration.)
> c) If we double to 40 parameters, the pairwise count increases to ~21. Explain why doubling parameters barely changes the test count.
> d) If we increase from 2-way to 3-way for the original 20 parameters, how does the test count change? Explain why strength increases are expensive.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.3 Logarithmic Growth — The Key Property
>
> The test count formula :
>
> > N ∝ v^t × log(k)
> >
> > v = values per parameter, t = strength, k = number of parameters
>
> **Implications:**
> - **Adding parameters is cheap:** Doubling parameters from 20 to 40 adds ~3 tests (pairwise)
> - **Raising strength is expensive:** The v^t factor means 2-way → 3-way multiplies by ~v
>
> **Example (10 parameters × 3 values each):**
>
> | Strength | Exhaustive | Covering Array | Reduction |
> |----------|-----------|----------------|-----------|
> | 1-way | 30 | 3 | 10× |
> | 2-way | 810 | 15 | 54× |
> | 3-way | 19,683 | 33 | 596× |
> | 4-way | 531,441 | 54 | 9,841× |
>
> **Example (scaling parameters, pairwise, 3 values each):**
>
> | Parameters | Exhaustive | Pairwise |
> |------------|-----------|----------|
> | 10 | 59,049 | 15 |
> | 20 | 3.5 × 10⁹ | 18 |
> | 40 | 1.2 × 10¹⁹ | **21** |
> | 100 | 5.2 × 10⁴⁷ | **25** |
>
> {: .highlight }
> > **Exam Tip:** The formula N ∝ v^t × log(k) explains two facts: (1) why CT scales to huge parameter spaces, and (2) why raising strength is so expensive. Be ready to explain both.
>
> #### Logarithmic Growth
>
> The most important practical property of covering arrays: test count grows **logarithmically** in the number of parameters.
>
> The approximate test count formula :
>
> > N ∝ v^t × log(k)
>
> Where v = values per parameter, t = interaction strength, k = number of parameters.
>
> **Good news:** Adding parameters is cheap. Doubling from 20 to 40 parameters adds only ~3 tests for pairwise coverage.
>
> **Bad news:** Raising interaction strength is expensive. The v^t factor means going from 2-way to 3-way roughly multiplies test count by v.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/combinatorial/RQ_A07_Combinatorial.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/combinatorial/RQ_A07_Combinatorial.md)

### Card 171 — Question 3: NIST Fault Interaction Data

> [!question] Question
> **Question 3: NIST Fault Interaction Data**
>
> Kuhn et al. (2004) found these cumulative fault detection rates:
>
> | Domain | 2-way | 3-way | 4-way |
> |--------|-------|-------|-------|
> | NASA | 93% | 98% | 100% |
> | Medical | 97% | 99% | 100% |
> | Mozilla | 76% | 95% | — |
>
> a) What does "93% at 2-way" mean practically?
> b) A safety-critical medical device team uses pairwise testing. Is this sufficient? What would you recommend?
> c) Why does Mozilla have a lower 2-way detection rate than medical devices?
> d) What is the maximum interaction strength needed across ALL studied projects? What does this imply for testing strategy?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.2 The NIST Fault Interaction Study
>
> Kuhn, Wallace, and Gallo  analyzed 329 error reports from NASA, medical devices, Mozilla, and Apache. Their findings form the empirical foundation of CT:
>
> | Domain | 1-way | 2-way | 3-way | 4-way | 6-way |
> |--------|-------|-------|-------|-------|-------|
> | NASA GSFC | 68% | **93%** | 98% | 100% | — |
> | Medical Devices | 66% | **97%** | 99% | 100% | — |
> | Mozilla | 29% | 76% | 95% | — | 100% |
> | Apache | 42% | 70% | — | — | 100% |
>
> **Key insight:** No failure in any studied project required more than 6-way interactions. If you test all 6-tuples, you achieve effectively exhaustive coverage .
>
> #### The ≤6-Way Interaction Insight
>
> NIST analyzed 329 error reports across multiple domains and found a remarkable pattern :
>
> | Domain | 2-way | 3-way | 4-way | 6-way |
> |--------|-------|-------|-------|-------|
> | NASA GSFC | 93% | 98% | 100% | — |
> | Medical Devices | 97% | 99% | 100% | — |
> | Mozilla | 76% | 95% | — | 100% |
> | Apache | 70% | — | — | 100% |
>
> **No failure in any studied project required more than 6-way interactions.** This means testing all 6-tuples is effectively exhaustive for practical purposes.
>
> Why are almost all faults triggered by few-way interactions? Code structure naturally limits complexity. A NASA study of 7,685 conditions found that 80% of `if`/`while` statements have 1-2 boolean operands . Developers simply don't write deeply nested conditions.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/combinatorial/RQ_A07_Combinatorial.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/combinatorial/RQ_A07_Combinatorial.md)

### Card 172 — Question 4: IPOG Algorithm Trace

> [!question] Question
> **Question 4: IPOG Algorithm Trace**
>
> Trace the IPOG algorithm for 3 parameters (P1, P2, P3), each with values {0, 1, 2}, at strength t=2.
>
> a) **Phase 1:** What is the initial test set for P1 and P2?
> b) **Phase 2 (Horizontal Growth):** Extend each row with a value for P3 that covers the most uncovered (P1,P3) and (P2,P3) pairs.
> c) **Phase 3 (Vertical Growth):** Which pairs (if any) remain uncovered? Add rows with don't-care values to cover them.
> d) How many rows does your final array have?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.2 IPOG — Parameter-Order Growth (2007)
>
> Lei et al.  introduced the one-**parameter**-at-a-time approach:
>
> **Three phases:**
> 1. Build t-way covering set for first t parameters
> 2. **Horizontal growth:** Extend existing rows with new parameter (greedy assignment)
> 3. **Vertical growth:** Add new rows for uncovered t-tuples (use don't-care `*` values)
>
> **Advantages:** Lower complexity than AETG, deterministic, generalizes to any t. Foundation of ACTS.
>
> #### Three Phases
>
> **Phase 1:** Build a complete t-way covering set for the first t parameters.
>
> **Phase 2 — Horizontal Growth:** For each remaining parameter, extend every existing test case by adding a value that covers the most uncovered t-tuples.
>
> | P1 | P2 | → | P1 | P2 | P3 |
> |----|----|----|----|----|-----|
> | 0 | 0 | | 0 | 0 | **0** |
> | 0 | 1 | | 0 | 1 | **1** |
> | 1 | 0 | | 1 | 0 | **2** |
> | 1 | 1 | | 1 | 1 | **0** |
>
> **Phase 3 — Vertical Growth:** Add new rows for any t-tuples not yet covered. Use "don't-care" values (marked `*`) in positions that don't affect coverage.
>
> | P1 | P2 | P3 |
> |----|----|----|
> | 0 | 0 | 0 |
> | 0 | 1 | 1 |
> | 1 | 0 | 2 |
> | 1 | 1 | 0 |
> | **0** | **\*** | **2** |
> | **1** | **\*** | **1** |
>
> **Advantages over AETG:**
> - Lower computational complexity
> - Deterministic (no random candidates)
> - Naturally generalizes to any strength t
> - Foundation of the NIST ACTS tool

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/combinatorial/RQ_A07_Combinatorial.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/combinatorial/RQ_A07_Combinatorial.md)

### Card 173 — Question 5: AETG vs IPOG

> [!question] Question
> **Question 5: AETG vs IPOG**
>
> Compare the AETG (1997) and IPOG (2007) algorithms:
>
> a) What is the fundamental difference in their approach? (Hint: "one-X-at-a-time")
> b) Which has lower computational complexity and why?
> c) Which serves as the basis for the ACTS tool?
> d) In what scenario might AETG produce smaller test suites than IPOG?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.2 IPOG — Parameter-Order Growth (2007)
>
> Lei et al.  introduced the one-**parameter**-at-a-time approach:
>
> **Three phases:**
> 1. Build t-way covering set for first t parameters
> 2. **Horizontal growth:** Extend existing rows with new parameter (greedy assignment)
> 3. **Vertical growth:** Add new rows for uncovered t-tuples (use don't-care `*` values)
>
> **Advantages:** Lower complexity than AETG, deterministic, generalizes to any t. Foundation of ACTS.
>
> #### AETG: The First Greedy Algorithm (1997)
>
> AETG (Automatic Efficient Test Generator) was the first practical tool for generating covering arrays for software testing .
>
> **Approach:** One-**test**-at-a-time
>
> 1. Identify parameter and value appearing in most uncovered pairs
> 2. Order remaining parameters by number of uncovered pairs
> 3. For each remaining parameter, greedily select value covering most uncovered pairs
> 4. Generate M=50 random candidates this way, keep the best one
> 5. Repeat until all t-tuples are covered
>
> **Key contribution:** Proved that test suite size grows **logarithmically** in the number of parameters. This meant CT could scale to systems with 80+ parameters.
>
> **Performance examples:**
> - 40 parameters × 3 values: **21 tests** (vs. 1.2 × 10¹⁹ exhaustive)
> - 800-service telecom project: 336 scenarios → **30 pairwise tests**
> - Achieved >90% block coverage on Unix commands
>
> **Limitation:** Random candidate generation (M=50 per test) makes AETG slow for large models.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/combinatorial/RQ_A07_Combinatorial.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/combinatorial/RQ_A07_Combinatorial.md)

### Card 174 — Question 6: Constraint Handling

> [!question] Question
> **Question 6: Constraint Handling**
>
> A date testing model has parameters: Day (1-31), Month (Jan-Dec), Year (leap/non-leap).
>
> a) Give two examples of invalid combinations.
> b) Explain the "Avoid" strategy for handling these constraints.
> c) Why can't you simply remove invalid rows from the covering array after generation?
> d) How does CASA handle constraints differently from ACTS?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.1 Constraint Handling
>
> Four strategies for invalid combinations:
>
> | Strategy | Description | When to Use |
> |----------|-------------|-------------|
> | Abstract | Combine conflicting params | Few conflicts |
> | Partition | Split into sub-models | Independent groups |
> | Avoid | Generator excludes invalid | ACTS, PICT support |
> | Replace | Post-process conflicting rows | Legacy models |
>
> #### CASA: When Constraints Dominate
>
> CASA (Covering Arrays by Simulated Annealing) integrates a SAT solver for systems with complex constraints .
>
> **When to use CASA:**
> - Systems with many interdependent constraints
> - When test suite size matters more than generation time
> - Test execution takes >21 seconds per test (CASA's generation cost is amortized)
>
> **Performance:**
> - **25% smaller** suites than greedy approaches on constrained problems
> - **90× faster** than base SA through optimizations
> - SAT solver (MiniSAT) handles constraint satisfaction during search
>
> **Trade-off:** Generation is slower than ACTS/PICT, but smaller suites save execution time. The break-even point is approximately 21 seconds per test execution .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/combinatorial/RQ_A07_Combinatorial.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/combinatorial/RQ_A07_Combinatorial.md)

### Card 175 — Question 7: Industrial Evidence Analysis

> [!question] Question
> **Question 7: Industrial Evidence Analysis**
>
> Hu et al. (2020) found that CT detected 93.3% of multi-factor faults while in-house teams detected only 6.7%.
>
> a) Why is the gap so dramatic for multi-factor faults?
> b) For single-factor faults, the gap narrows (89.3% vs 71.4%). Why does CT still outperform?
> c) Name three barriers to CT adoption that Hu identified.
> d) How would you address the barrier that "ACTS can't generate executable test scripts"?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Barriers to Adoption
>
> Despite strong evidence, industrial adoption faces challenges :
>
> | Barrier | Description |
> |---------|-------------|
> | **Manual execution limit** | Industry prefers <120-200 test cases for manual execution |
> | **Tool gap** | ACTS generates abstract tests, not executable scripts |
> | **Documentation dependency** | Parameter model quality depends on specification quality |
> | **Masking effect** | Early faults terminate execution before later faults are reached |
> | **Skills gap** | CT requires understanding covering array theory |
> | **Organizational inertia** | Teams resist changing established testing processes |
>
> #### Barriers to Adoption
>
> | Barrier | Mitigation |
> |---------|-----------|
> | Manual execution limits (<200 tests) | Automate execution |
> | Tools don't generate scripts | Add mapping layer |
> | Depends on specification quality | Invest in parameter model |
> | Masking effect | Separate positive/negative tests |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/combinatorial/RQ_A07_Combinatorial.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/combinatorial/RQ_A07_Combinatorial.md)

### Card 176 — Question 8: Choosing Interaction Strength

> [!question] Question
> **Question 8: Choosing Interaction Strength**
>
> You are testing a web application with the following parameters:
> - Authentication: username, password, MFA method (3 params — security-critical)
> - UI: theme, language, font size (3 params — low risk)
> - Payment: card type, amount, currency (3 params — medium risk)
>
> a) What interaction strength would you recommend for each group?
> b) How could mixed-strength arrays help reduce the total test count?
> c) If pairwise testing reveals no faults, does that prove the system is correct? Why or why not?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.3 Choosing Interaction Strength
>
> | Risk Level | Strength | Approx. Detection | Domain Examples |
> |------------|----------|-------------------|-----------------|
> | Low | 2-way | ~90% | Web forms, UI config |
> | Medium | 3-way | ~98% | Business logic, APIs |
> | High | 4-way | ~100% | Medical devices, aerospace |
> | Very High | 5-6-way | 100% | FAA, nuclear, automotive safety |
>
> Evidence: Bures & Ahmed  showed 3-way detected faults that 2-way missed entirely in **30%** of tested systems. Start with 2-way; increase for critical subsystems.
>
> #### Choosing Interaction Strength
>
> The choice of t (interaction strength) depends on risk level and available budget.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/combinatorial/RQ_A07_Combinatorial.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/combinatorial/RQ_A07_Combinatorial.md)

### Card 177 — Question 9: Autonomous Driving CT (Tao 2019)

> [!question] Question
> **Question 9: Autonomous Driving CT (Tao 2019)**
>
> Tao et al. applied CT to Autonomous Emergency Braking at AVL List GmbH.
>
> a) Why is exhaustive physical testing infeasible for autonomous driving?
> b) Describe the end-to-end pipeline: from domain ontology to test results.
> c) The model had 37 parameters and 39 constraints. Why is constraint handling critical in this domain?
> d) Only 2-way (pairwise) coverage was used. What would be the implications of increasing to 3-way?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### AVL List GmbH Case (Tao 2019)
>
> **Domain:** Autonomous Emergency Braking (AEB) function for Euro NCAP compliance.
>
> **Pipeline:**
>
> 1. **Domain Ontology** — UML model of AEB domain from Euro NCAP protocols
> 2. **CT Model** — 37 parameters, 39 constraints (via CT_ONT2 algorithm)
> 3. **Test Generation** — IPOG generates 319 pairwise test cases
> 4. **Scenario Format** — Automatic conversion to OpenScenario XML
> 5. **Simulation** — Execution in VTD (Virtual Test Drive) platform
> 6. **Results** — All 319 scenarios verified in simulation
>
> **Parameters include:**
> - Ego vehicle speed (0-130 km/h)
> - 8 vehicle types (sedan, SUV, motorcycle, bicycle, etc.)
> - Lateral offset, direction, deceleration profiles
> - Pedestrian type (adult, child)
> - Lighting (day, night), road surface (dry, wet)
>
> **Key insight:** Ontology-based CT bridges the gap between domain knowledge and systematic test generation. The ontology captures relationships and constraints that raw parameter models cannot express.
>
> #### Case Study: Autonomous Driving (Tao 2019)
>
> Tao et al.  applied CT to Autonomous Emergency Braking (AEB) function validation at AVL List GmbH.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/combinatorial/RQ_A07_Combinatorial.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/combinatorial/RQ_A07_Combinatorial.md)

### Card 178 — Question 10: Seed Reuse Strategy

> [!question] Question
> **Question 10: Seed Reuse Strategy**
>
> A team has a pairwise (2-way) test suite of 500 tests and needs to increase to 3-way coverage.
>
> a) According to Bombarda (2025), should they use the existing tests as seeds? Which tool should they use?
> b) What happens if they try to use partial test cases (rows with missing values) as seeds?
> c) A different team wants to reuse tests to complete an incomplete 2-way suite (60% complete). Is seeding beneficial here?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.6 Seed Reuse (Bombarda 2025)
>
> Bombarda & Gargantini  studied when to reuse existing tests:
>
> | Scenario | Use Seeds? | Best Tool |
> |----------|-----------|-----------|
> | Strength increase (2→3) | **Yes** | ACTS (smallest suites) |
> | Suite completion (>70%) | Maybe | PICT |
> | Partial test cases | **No** | Overhead negates benefit |
>
> {: .highlight }
> > **Exam Tip:** Know AETG vs IPOG: AETG = one-test-at-a-time (greedy candidates), IPOG = one-parameter-at-a-time (horizontal + vertical growth). IPOG is lower complexity and the basis of ACTS.
>
> #### Key Findings
>
> **Strength increase:** Seeds are clearly beneficial. ACTS produced the smallest 3-way suites when seeded with existing 2-way tests (mean 864 tests vs. PICT's 935 and pMEDICI+'s 1,130) .
>
> **Test suite completion:** Results are mixed. ACTS actually produced *larger* suites when given seeds for completion. PICT benefited from seeds only when the existing suite was >70% complete.
>
> **Partial test cases:** Not recommended. The preprocessing overhead to handle incomplete test cases negated any benefits from reuse.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/combinatorial/RQ_A07_Combinatorial.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/combinatorial/RQ_A07_Combinatorial.md)

### Card 179 — Question 11: CT for ML Dataset Quality

> [!question] Question
> **Question 11: CT for ML Dataset Quality**
>
> Lanus et al. (2021) found that a smaller dataset had higher 2-way combinatorial coverage (0.93) than a larger dataset (0.83).
>
> a) What does "2-way combinatorial coverage of a dataset" mean?
> b) Why doesn't dataset size guarantee representativeness?
> c) How could the SDCCM metric predict transfer learning performance drops?
> d) Give one practical application of CCM metrics for an ML engineering team.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.4 CT for ML Dataset Quality
>
> Lanus et al.  bridged CT and ML quality:
> - **CCM_t:** Measures t-way coverage of a dataset
> - **SDCCM_t:** Coverage difference between datasets
> - **Finding:** Smaller dataset had HIGHER 2-way coverage (0.93 vs 0.83)
> - **Lesson:** Dataset size ≠ representativeness
>
> #### Practical Applications
>
> - **Source model selection:** Choose pre-trained models from a model zoo based on training dataset coverage similarity
> - **Directing data collection:** Identify missing t-way combinations and collect targeted data
> - **Transfer learning prediction:** Coverage asymmetry (SDCCM) predicts performance drops when transferring between datasets
> - **Stress test design:** Use uncovered t-tuples to design adversarial test cases

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/combinatorial/RQ_A07_Combinatorial.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/combinatorial/RQ_A07_Combinatorial.md)

### Card 180 — Question 12: Tool Selection

> [!question] Question
> **Question 12: Tool Selection**
>
> For each scenario, recommend a tool (ACTS, PICT, or CASA) and explain your reasoning:
>
> a) A medical device with 15 parameters, strict constraints, and safety-critical testing requirements.
> b) A web application CI pipeline that needs to regenerate tests on every commit.
> c) An embedded system with 50 parameters and complex interdependent constraints.
> d) A team that needs to increase from 2-way to 3-way and has an existing 2-way suite.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### CASA: When Constraints Dominate
>
> CASA (Covering Arrays by Simulated Annealing) integrates a SAT solver for systems with complex constraints .
>
> **When to use CASA:**
> - Systems with many interdependent constraints
> - When test suite size matters more than generation time
> - Test execution takes >21 seconds per test (CASA's generation cost is amortized)
>
> **Performance:**
> - **25% smaller** suites than greedy approaches on constrained problems
> - **90× faster** than base SA through optimizations
> - SAT solver (MiniSAT) handles constraint satisfaction during search
>
> **Trade-off:** Generation is slower than ACTS/PICT, but smaller suites save execution time. The break-even point is approximately 21 seconds per test execution .
>
> #### Tool Recommendations by Use Case
>
> | Use Case | Recommended | Why |
> |----------|-------------|-----|
> | General industrial testing | **ACTS** | Best all-around: speed, size, constraints, seeds |
> | CI/CD pipeline integration | **PICT** | Text input, CLI, fast generation |
> | Heavily constrained systems | **CASA** | SAT solver handles complex constraint networks |
> | Enterprise collaboration | **Hexawise** | Web-based, team features, reporting |
> | Academic research | **CAgen** | Multiple algorithms, benchmarking support |
> | Strength increase with seeds | **ACTS** | Smallest suites when reusing existing tests |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/combinatorial/RQ_A07_Combinatorial.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/combinatorial/RQ_A07_Combinatorial.md)

### Card 181 — Question 13: Calculation Problem

> [!question] Question
> **Question 13: Calculation Problem**
>
> A mobile app has the following test parameters:
> - OS: {iOS, Android} (2 values)
> - Browser: {Chrome, Safari, Firefox} (3 values)
> - Screen: {Small, Medium, Large} (3 values)
> - Network: {WiFi, 4G, 3G} (3 values)
> - Language: {EN, FR, DE} (3 values)
>
> a) Calculate the exhaustive test count.
> b) Using the AETG logarithmic growth principle, estimate the pairwise test count. (Hint: for 5 params with max 3 values, expect ~15-18 tests.)
> c) If testing takes 10 minutes per test case, compare the total testing time for exhaustive vs pairwise.
> d) A constraint says "Safari only works on iOS." How does this affect the covering array?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.3 Logarithmic Growth — The Key Property
>
> The test count formula :
>
> > N ∝ v^t × log(k)
> >
> > v = values per parameter, t = strength, k = number of parameters
>
> **Implications:**
> - **Adding parameters is cheap:** Doubling parameters from 20 to 40 adds ~3 tests (pairwise)
> - **Raising strength is expensive:** The v^t factor means 2-way → 3-way multiplies by ~v
>
> **Example (10 parameters × 3 values each):**
>
> | Strength | Exhaustive | Covering Array | Reduction |
> |----------|-----------|----------------|-----------|
> | 1-way | 30 | 3 | 10× |
> | 2-way | 810 | 15 | 54× |
> | 3-way | 19,683 | 33 | 596× |
> | 4-way | 531,441 | 54 | 9,841× |
>
> **Example (scaling parameters, pairwise, 3 values each):**
>
> | Parameters | Exhaustive | Pairwise |
> |------------|-----------|----------|
> | 10 | 59,049 | 15 |
> | 20 | 3.5 × 10⁹ | 18 |
> | 40 | 1.2 × 10¹⁹ | **21** |
> | 100 | 5.2 × 10⁴⁷ | **25** |
>
> {: .highlight }
> > **Exam Tip:** The formula N ∝ v^t × log(k) explains two facts: (1) why CT scales to huge parameter spaces, and (2) why raising strength is so expensive. Be ready to explain both.
>
> #### Example: scaling parameters (pairwise, 3 values each)
>
> | Parameters | Exhaustive | Pairwise | Reduction |
> |------------|-----------|----------|-----------|
> | 10 | 59,049 | 15 | 3,937× |
> | 20 | 3.5 × 10⁹ | 18 | ~10⁸× |
> | 40 | 1.2 × 10¹⁹ | 21 | ~10¹⁸× |
> | 100 | 5.2 × 10⁴⁷ | 25 | ~10⁴⁶× |
>
> The logarithmic growth is what makes CT practical for real systems with dozens or hundreds of parameters .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/combinatorial/RQ_A07_Combinatorial.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/combinatorial/RQ_A07_Combinatorial.md)

### Card 182 — Question 14: Algorithm Taxonomy

> [!question] Question
> **Question 14: Algorithm Taxonomy**
>
> Zeb et al. (2025) classified CT algorithms into five categories.
>
> a) Name the five categories and give one example algorithm for each.
> b) Which category has been the most successful historically?
> c) What is a "hyper-heuristic" and why is it considered the emerging frontier?
> d) Why might a mix strategy outperform a standard (single) metaheuristic?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Algorithm Evolution Timeline
>
> The field has progressed through increasingly sophisticated strategies:
>
> ```
> 1997: AETG (Greedy) → 2007: IPOG (Parameter-order) → 2011: CASA (SA+SAT) → 2020s: Hyper-heuristics
> ```
>
> Zeb et al.  analyzed 91 studies (2003-2025) and identified five algorithm categories:
>
> | Category | Description | Examples | Key Trait |
> |----------|-------------|----------|-----------|
> | **Standard** | Single metaheuristic | SA, GA, PSO, ACO | Simple, proven |
> | **Mix** | Two algorithms combined | Greedy + SA (2SSA) | Better than either alone |
> | **Adaptive** | Self-tuning parameters | Fuzzy TLBO | Adjusts during search |
> | **Hybrid** | Search + greedy/algebraic | REH | Speed + quality |
> | **Hyper-heuristic** | Meta-level selector | HHSA, HHH | Selects best strategy per instance |
>
> **Key finding:** Simulated Annealing is the most successful algorithm across all categories . Hyper-heuristics represent the emerging frontier — they select which low-level algorithm to use for each specific problem instance.
>
> #### 4.4 Algorithm Evolution
>
> Zeb et al.  classified 91 studies into 5 categories:
>
> | Category | Approach | Example | Key Trait |
> |----------|----------|---------|-----------|
> | Standard | Single metaheuristic | SA, GA, PSO | Simple, proven |
> | Mix | Two algorithms | Greedy+SA | Better than either |
> | Adaptive | Self-tuning | Fuzzy TLBO | Adjusts during search |
> | Hybrid | Search + greedy | REH | Speed + quality |
> | Hyper-heuristic | Meta-selector | HHSA | Selects best per instance |
>
> **SA is the most successful** algorithm across all categories. Hyper-heuristics are the emerging frontier.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/combinatorial/RQ_A07_Combinatorial.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/combinatorial/RQ_A07_Combinatorial.md)

### Card 183 — Question 15: Comprehensive Comparison

> [!question] Question
> **Question 15: Comprehensive Comparison**
>
> Compare the following three testing approaches for a system with 10 parameters, 3 values each:
>
> | Approach | Tests | What It Guarantees |
> |----------|-------|-------------------|
> | 1-way | ? | ? |
> | 2-way (pairwise) | ? | ? |
> | Exhaustive | ? | ? |
>
> a) Fill in the table with approximate test counts and what each guarantees.
> b) Which approach would you use for: (i) a prototype, (ii) a production web app, (iii) a medical device controller?
> c) What additional technique would you combine with CT for maximum effectiveness?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Example: scaling parameters (pairwise, 3 values each)
>
> | Parameters | Exhaustive | Pairwise | Reduction |
> |------------|-----------|----------|-----------|
> | 10 | 59,049 | 15 | 3,937× |
> | 20 | 3.5 × 10⁹ | 18 | ~10⁸× |
> | 40 | 1.2 × 10¹⁹ | 21 | ~10¹⁸× |
> | 100 | 5.2 × 10⁴⁷ | 25 | ~10⁴⁶× |
>
> The logarithmic growth is what makes CT practical for real systems with dozens or hundreds of parameters .
>
> #### Example: 10 parameters × 3 values each
>
> | Strength | Exhaustive | Covering Array | Reduction |
> |----------|-----------|----------------|-----------|
> | 1-way | 30 | 3 | 10× |
> | 2-way | 810 | 15 | 54× |
> | 3-way | 19,683 | 33 | 596× |
> | 4-way | 531,441 | 54 | 9,841× |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/combinatorial/RQ_A07_Combinatorial.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/combinatorial/RQ_A07_Combinatorial.md)

## Random Testing (34)

### Card 184 — Question 1: What Makes Random Testing "Random"

> [!question] Question
> **Question 1: What Makes Random Testing "Random"**
>
> What makes random testing "random" in the technical sense? What three conditions must be satisfied (Hamlet 1984)?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### What Makes Testing "Random"?
>
> Hamlet distinguishes "random" in the technical sense — statistically independent test selection from a defined distribution — from the slang usage meaning haphazard, unplanned testing . True random testing requires:
>
> 1. **A defined input distribution** (operational profile or uniform)
> 2. **Statistical independence** between test selections
> 3. **An oracle** to determine pass/fail for each execution
>
> When these conditions hold, random testing uniquely enables quantitative reliability prediction. When they do not, "not only is random testing counterindicated, but testing of any kind cannot provide a plausible prediction of software quality" .
>
> #### 2.3 Random vs. Partition Testing
>
> The debate has been running since 1984 :
>
> | Year | Authors | Finding |
> |------|---------|---------|
> | 1984 | Duran & Ntafos | Random often more cost-effective |
> | 2001 | Ntafos | ~20% more random tests erase partition advantage |
> | 2006 | Hamlet | Only random will do for unstructured spaces and state-dependent systems |
>
> **Resolution (Ntafos 2001):** The gap shrinks to <0.05% at scale. Roughly 20% more random tests eliminate any partition testing advantage .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 185 — Question 2: Random vs Partition Testing

> [!question] Question
> **Question 2: Random vs Partition Testing**
>
> When would random testing be a poor choice compared to partition testing?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.3 Random vs. Partition Testing
>
> The debate has been running since 1984 :
>
> | Year | Authors | Finding |
> |------|---------|---------|
> | 1984 | Duran & Ntafos | Random often more cost-effective |
> | 2001 | Ntafos | ~20% more random tests erase partition advantage |
> | 2006 | Hamlet | Only random will do for unstructured spaces and state-dependent systems |
>
> **Resolution (Ntafos 2001):** The gap shrinks to <0.05% at scale. Roughly 20% more random tests eliminate any partition testing advantage .
>
> #### Random vs. Partition Testing
>
> A persistent question in testing theory: does systematic partition testing outperform random testing?
>
> The debate has a nuanced resolution :
>
> - **Random wins** when no meaningful partition exists, cost matters, operational profile testing is needed, or stateful systems require sequence testing
> - **Partition wins** when subdomains are genuinely homogeneous and cost-weighted failure rates vary significantly across subdomains
> - **The gap is small**: roughly 20% more random tests erase any partition advantage , and just 1-2 additional random tests can tilt the balance at scale
>
> The practical answer: combine both — random testing first for broad coverage and reliability estimation, followed by targeted systematic testing for edge cases .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 186 — Question 3: Statistical Confidence Limits

> [!question] Question
> **Question 3: Statistical Confidence Limits**
>
> A colleague says "we ran 10,000 random tests with no failures, so the software is bug-free." What is wrong with this claim? Use the formula $C = 1-(1-F)^N$.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Why Random Testing?
>
> Systematic testing strategies require human judgement to select inputs. That judgement introduces bias: testers exercise the cases they anticipate, missing the unexpected interactions that cause real failures. Random testing bypasses this bias entirely.
>
> The empirical evidence is compelling:
>
> - **Miller's 16-year fuzz series** found that 25-33% of UNIX utilities crashed on random input , and the same error classes persisted for over a decade
> - **Randoop** found 30 errors in a .NET component already tested by 40 engineers for 5 years — more than a tester typically finds in a year
> - **QuickCheck** discovered bugs in production Haskell libraries with a 300-line tool, finding errors equally distributed across generators, specifications, and implementations
>
> Random testing also uniquely supports **statistical reliability prediction**: after N successful random tests drawn from an operational profile, one can bound the probability of undetected failure .
>
> #### 1.2 Why Use Random Testing?
>
> | Benefit | Explanation |
> |---------|-------------|
> | **Cheap** | Once the oracle is solved, generating inputs is trivial |
> | **Probabilistic guarantees** | Can calculate reliability bounds  |
> | **Complements partition** | Finds different faults than systematic testing |
> | **Scales well** | Can generate millions of tests automatically |
>
> Random testing is particularly useful when domain knowledge is lacking, the state space is large, or reliability calculations are required .
>
> {: .highlight }
> > **Exam Tip:** Random testing is NOT haphazard testing. It requires a defined distribution, statistical independence, and an oracle. Memorize these three requirements.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 187 — Question 4: Reliability Calculation

> [!question] Question
> **Question 4: Reliability Calculation**
>
> Calculate how many random tests are needed for 95% confidence that the failure rate is below 1 in 10,000.
>
> *Hint: Use $N = \frac{\ln(1-C)}{\ln(1-F)}$*

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Reliability Prediction
>
> The fundamental formula for random testing confidence:
>
> $$
> C = 1 - (1-F)^N
> $$
>
> Where:
> - **C** = confidence that at least one failure would have been observed
> - **F** = true failure rate in the operational profile
> - **N** = number of successful random tests
>
> **Example**: If the true failure rate is F = 0.001 (1 in 1,000 inputs triggers a bug), how many random tests do we need for 95% confidence we would have seen a failure?
>
> $$
> 0.95 = 1 - (1 - 0.001)^N \implies N = \frac{\ln(0.05)}{\ln(0.999)} \approx 2{,}996
> $$
>
> So ~3,000 successful tests give 95% confidence the failure rate is below 0.1% .
>
> …
>
> #### 2.1 Probabilistic Guarantees
>
> The fundamental formula for random testing confidence :
>
> $$C = 1 - (1-F)^N$$
>
> Where:
> - **C** = confidence that at least one failure would have been observed
> - **F** = true failure rate in the operational profile
> - **N** = number of successful random tests
>
> | Confidence | Target F | Tests Needed |
> |------------|----------|--------------|
> | 90% | 10⁻³ | 2,302 |
> | 90% | 10⁻⁴ | 23,025 |
> | 99% | 10⁻⁴ | 46,050 |
> | 99% | 10⁻⁵ | 460,517 |
>
> **Key insight:** 23,000 successful random tests give 90% confidence the failure rate is below 1 in 10,000 .
>
> {: .highlight }
> > **Exam Tip:** Know the formula C = 1-(1-F)^N and the planning table. Be able to compute N given C and F: N = ln(1-C) / ln(1-F).

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 188 — Question 5: Randoop Plateau Effect

> [!question] Question
> **Question 5: Randoop Plateau Effect**
>
> What is the "plateau effect" in Randoop and what causes it?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.4 Randoop: Feedback-Directed Random Testing
>
> Randoop builds test sequences incrementally :
>
> | Metric | Value |
> |--------|-------|
> | Errors found | **30** in 15 human hours (on code tested by 40 engineers for 5 years) |
> | Productivity | **100x** faster than manual testing |
> | Tests generated | 4,000,000 sequences |
>
> The **"plateau effect"** — error-finding rate drops from 5/hour to zero after ~12 hours .
>
> {: .highlight }
> > **Exam Tip:** Know the "20% rule" — 20% more random tests erase partition advantage (Ntafos 2001). Know the two scenarios where only random testing will do (Hamlet 2006).
>
> #### Randoop
>
> Randoop builds test sequences incrementally :
>
> 1. Start with simple sequences (constructors, constants)
> 2. Randomly select a method to call
> 3. Choose arguments from previously constructed sequences
> 4. Execute immediately and classify:
>    - **Error-revealing** → report as bug, do not extend
>    - **Illegal** (e.g., `ArgumentException` on null) → discard
>    - **New** (creates novel object states) → add to pool for extension
>
> Key results on a .NET component tested by 40 engineers for 5 years:
>
> | Metric | Value |
> |--------|-------|
> | Errors found | 30 (in 15 human hours, 150 CPU hours) |
> | Productivity | 100x faster than manual testing |
> | Tests generated | 4,000,000 sequences |
> | Coverage finding | Found errors in code with 100% block and arc coverage |
>
> The "plateau effect" — error-finding rate dropping from 5/hour to zero after ~12 hours — reveals the limitation of uniform random method selection: classes with simple constructors are explored disproportionately .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 189 — Question 6: Hamlet's Argument for Random Testing

> [!question] Question
> **Question 6: Hamlet's Argument for Random Testing**
>
> Why did Hamlet (2006) argue that "only random testing will do" in certain scenarios? Name two such scenarios.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.3.1 Hamlet's Two Scenarios (2006)
>
> Hamlet  argues random testing is not merely an alternative but the **only valid choice** in two specific scenarios:
>
> **Scenario 1 — Large, unstructured input domains:**
> When no rational basis exists to partition the input space, systematic subdomain testing relies on subjective judgement. Without meaningful partitions, it is "no more than subjective comfort." Random sampling of the operational profile is the only principled approach.
>
> **Scenario 2 — Persistent-state systems:**
> Valid tests of stateful programs must be *input sequences from reset*, not individually sampled states. Feasible states are "very sparse in all possible bit patterns" — directly setting a program to an arbitrary state may exercise configurations no real input sequence can reach. Random sequence generation correctly restricts testing to reachable states; state-sampled systematic testing does not.
>
> > "Valid tests of programs with state are sequences of inputs, and it is here that random testing comes into its own." — Hamlet 2006
>
> #### 2.4 Randoop: Feedback-Directed Random Testing
>
> Randoop builds test sequences incrementally :
>
> | Metric | Value |
> |--------|-------|
> | Errors found | **30** in 15 human hours (on code tested by 40 engineers for 5 years) |
> | Productivity | **100x** faster than manual testing |
> | Tests generated | 4,000,000 sequences |
>
> The **"plateau effect"** — error-finding rate drops from 5/hour to zero after ~12 hours .
>
> {: .highlight }
> > **Exam Tip:** Know the "20% rule" — 20% more random tests erase partition advantage (Ntafos 2001). Know the two scenarios where only random testing will do (Hamlet 2006).

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 190 — Question 7: Oracle and Effectiveness

> [!question] Question
> **Question 7: Oracle and Effectiveness**
>
> Explain the relationship between the oracle and the effectiveness of random testing. Compare crash detection, sanitizers, properties, and differential oracles.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The Oracle Problem
>
> Generating millions of inputs is easy. Knowing whether each output is *correct* is the hard part. The oracle mechanism determines what class of bugs random testing can find:
>
> | Oracle Type | Mechanism | Catches | Misses |
> |-------------|-----------|---------|--------|
> | **Crash detection** | Program crashes or hangs | Reliability failures, memory corruption | Semantic bugs |
> | **Sanitizers** | ASan, UBSan, TSan | Buffer overflows, undefined behavior, data races | Logic errors |
> | **Contracts** | Preconditions, postconditions, invariants | Specification violations | Unspecified behavior |
> | **Properties** | User-defined invariants for all inputs | Logical errors, corner cases | Requires developer specification effort |
> | **Coverage feedback** | New code paths = interesting input | Guides exploration toward new behavior | Does not verify correctness |
> | **Differential** | Compare against reference implementation | Any divergence from reference | Shared bugs in both implementations |
>
> ```mermaid
> flowchart LR
>     A["Crash Detection"] --> B["Sanitizers"]
>     B --> C["Coverage Feedback"]
>     C --> D["Contracts"]
>     D --> E["Properties"]
>     E --> F["Differential"]
>
>     style A fill:#c8e6c9,stroke:#388e3c
>     style B fill:#c8e6c9,stroke:#388e3c
>     style C fill:#fff3cd,stroke:#ffc107
>     style D fill:#fff3cd,stroke:#ffc107
>     style E fill:#ffccbc,stroke:#e64a19
>     style F fill:#ffccbc,stroke:#e64a19
> ```
>
> *Left to right: more automated but less precise → more precise but requires more effort.*
>
> The evolution from crash oracles  to sanitizer-augmented coverage  to specification-based properties  represents a trade-off between **automation and precision** .
>
> #### 1.1 What is Random Testing?
>
> Random testing selects test inputs independently at random from the program's input domain . It is not haphazard — it requires:
>
> 1. A **defined input distribution** (operational profile or uniform)
> 2. **Statistical independence** between test selections
> 3. An **oracle** to determine pass/fail
>
> | "Random" in Testing | "Random" Elsewhere |
> |--------------------|--------------------|
> | Systematic exploration | Arbitrary selection |
> | Statistical guarantees | No guarantees |
> | Automated generation | Manual "pick some" |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 191 — Question 8: Fuzz vs Random Testing

> [!question] Question
> **Question 8: Fuzz vs Random Testing**
>
> How does fuzz testing differ from random testing, and when would you choose fuzzing over general random testing?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### [Fuzz Testing](fuzzing)
>
> From Miller's 1990 UNIX study through whitebox fuzzing (SAGE) to modern coverage-guided greybox fuzzers (AFL, AFLGo).
>
> #### Why Random Testing?
>
> Systematic testing strategies require human judgement to select inputs. That judgement introduces bias: testers exercise the cases they anticipate, missing the unexpected interactions that cause real failures. Random testing bypasses this bias entirely.
>
> The empirical evidence is compelling:
>
> - **Miller's 16-year fuzz series** found that 25-33% of UNIX utilities crashed on random input , and the same error classes persisted for over a decade
> - **Randoop** found 30 errors in a .NET component already tested by 40 engineers for 5 years — more than a tester typically finds in a year
> - **QuickCheck** discovered bugs in production Haskell libraries with a 300-line tool, finding errors equally distributed across generators, specifications, and implementations
>
> Random testing also uniquely supports **statistical reliability prediction**: after N successful random tests drawn from an operational profile, one can bound the probability of undetected failure .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 192 — Question 9: Three Generations of Fuzzing

> [!question] Question
> **Question 9: Three Generations of Fuzzing**
>
> Explain the three generations of fuzzing (blackbox, whitebox, greybox) and why greybox fuzzing "won."

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.2 Three Generations of Fuzzing
>
> | Generation | Era | Approach | Example |
> |------------|-----|----------|---------|
> | **1. Blackbox** | 1990-2000 | Random bytes, no program knowledge | Miller's `cat /dev/urandom \| prog` |
> | **2. Whitebox** | 2000-2013 | Symbolic execution + constraint solving | SAGE (Microsoft) |
> | **3. Greybox** | 2013-present | Lightweight coverage feedback + evolution | AFL, AFLGo, libFuzzer |
>
> **Greybox won:** Best throughput-to-insight ratio with ~5-20% overhead .
>
> #### Three Generations of Fuzzing
>
> ```mermaid
> timeline
>     title Fuzzing Evolution
>     section Generation 1 — Blackbox
>         1990 : Miller — UNIX fuzz
>         2000 : Forrester — Windows NT
>         2006 : Miller — macOS
>     section Generation 2 — Whitebox
>         2008 : SAGE — symbolic + fuzz
>         2012 : KLEE — open-source SE
>     section Generation 3 — Greybox
>         2013 : AFL — coverage-guided
>         2017 : AFLGo — directed greybox
>         2019 : JQF — PBT + coverage
> ```

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 193 — Question 10: Miller's Persistent Bug Classes

> [!question] Question
> **Question 10: Miller's Persistent Bug Classes**
>
> Miller's fuzz studies found the same bug classes persisting for 16 years (1990-2006). What does this tell us about the software industry?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.3 Miller's Fuzz Studies (16-Year Longitudinal)
>
> | Year | Target | Crash Rate |
> |------|--------|------------|
> | 1990 | UNIX utilities | **25-33%**  |
> | 2000 | Windows NT apps | **21%** (+24% hang)  |
> | 2006 | macOS CLI | 7% (improved)  |
> | 2006 | macOS GUI | **73%** (worst ever)  |
>
> #### If the program crashes or hangs → bug found
>
> ```
>
> 25-33% of utilities on seven UNIX variants crashed or hung. The failures exposed fundamental programming errors: pointer and array bounds violations, unchecked return values, race conditions, and signed character handling bugs.
>
> **Windows NT (2000)**: Extended to GUI applications — 21% of tested applications crashed and 24% hung on random valid Win32 messages; 100% failed on random raw messages . The study exposed a systematic Win32 API flaw: applications could not distinguish window messages from the OS versus those from other programs, creating an inherent vulnerability.
>
> **macOS X (2006)**: Command-line reliability improved to 7% crash rate (down from 33%), but GUI failure rate reached 73% — the worst ever recorded .
>
> **The longitudinal finding**: The same error classes — buffer overflows, null pointer dereferences, unchecked return values — persisted for 16 years across operating systems. Simple random testing continues to find bugs that sophisticated techniques miss .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 194 — Question 11: Directed Greybox Fuzzing

> [!question] Question
> **Question 11: Directed Greybox Fuzzing**
>
> What is directed greybox fuzzing and why was AFLGo able to find Heartbleed in 20 minutes when symbolic execution failed in 24 hours?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Generation 3: Coverage-Guided Greybox Fuzzing (2013-present)
>
> Modern greybox fuzzers use lightweight instrumentation to measure code coverage, then evolve inputs that reach new program states.
>
> **The AFL model**: American Fuzzy Lop (AFL, 2013) introduced edge-based coverage measurement combined with an evolutionary algorithm :
>
> ```mermaid
> flowchart LR
>     A["Seed Queue"] --> B["Select & Mutate"]
>     B --> C["Execute PUT"]
>     C --> D{"New coverage?"}
>     D -- "Yes" --> E["Save to queue"]
>     E --> A
>     D -- "No" --> F["Discard"]
>     F --> A
>
>     style E fill:#c8e6c9,stroke:#388e3c
>     style F fill:#ffcdd2,stroke:#c62828
> ```
>
> A 1% increase in coverage correlates with 0.92% more bugs found .
>
> **What mutation looks like** — AFL takes a seed input and applies small changes:
>
> ```
> Original seed: "GET /index.html HTTP/1.1\r\n"
> Bit flip:      "GET /index.htm\xec HTTP/1.1\r\n"   ← flipped one bit
> Arithmetic:    "GET /index.html HTTP/2.1\r\n"       ← incremented '1' → '2'
> Block delete:  "GET HTTP/1.1\r\n"                   ← removed a chunk
> ```
>
> If any mutated input triggers a new code edge, it joins the queue for further mutation.
>
> **Directed greybox fuzzing (AFLGo)**: Böhme et al. extended greybox fuzzing with distance-based guidance via simulated annealing, directing the fuzzer toward specific program locations . AFLGo exposed Heartbleed in under 20 minutes where Katch (symbolic execution) failed in 24 hours, and found 26 bugs in OSS-Fuzz targets including 17 CVEs.
>
> #### Three Generations of Fuzzing
>
> ```mermaid
> timeline
>     title Fuzzing Evolution
>     section Generation 1 — Blackbox
>         1990 : Miller — UNIX fuzz
>         2000 : Forrester — Windows NT
>         2006 : Miller — macOS
>     section Generation 2 — Whitebox
>         2008 : SAGE — symbolic + fuzz
>         2012 : KLEE — open-source SE
>     section Generation 3 — Greybox
>         2013 : AFL — coverage-guided
>         2017 : AFLGo — directed greybox
>         2019 : JQF — PBT + coverage
> ```

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 195 — Question 12: Crash Count vs Bug Count

> [!question] Question
> **Question 12: Crash Count vs Bug Count**
>
> Why is the finding that "57,142 unique crashes = only 9 actual bugs" (Klees 2018) important for fuzzing practice?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### If the program crashes or hangs → bug found
>
> ```
>
> 25-33% of utilities on seven UNIX variants crashed or hung. The failures exposed fundamental programming errors: pointer and array bounds violations, unchecked return values, race conditions, and signed character handling bugs.
>
> **Windows NT (2000)**: Extended to GUI applications — 21% of tested applications crashed and 24% hung on random valid Win32 messages; 100% failed on random raw messages . The study exposed a systematic Win32 API flaw: applications could not distinguish window messages from the OS versus those from other programs, creating an inherent vulnerability.
>
> **macOS X (2006)**: Command-line reliability improved to 7% crash rate (down from 33%), but GUI failure rate reached 73% — the worst ever recorded .
>
> **The longitudinal finding**: The same error classes — buffer overflows, null pointer dereferences, unchecked return values — persisted for 16 years across operating systems. Simple random testing continues to find bugs that sophisticated techniques miss .
>
> #### Bug Oracles for Fuzzing
>
> The oracle determines what bugs a fuzzer can find :
>
> | Oracle | Detects | Overhead |
> |--------|---------|----------|
> | **Crash signal** | Segfaults, abort | None |
> | **AddressSanitizer (ASan)** | Buffer overflow, use-after-free, double-free | ~73% |
> | **UndefinedBehaviorSan (UBSan)** | Integer overflow, null deref, alignment | ~20% |
> | **ThreadSanitizer (TSan)** | Data races, deadlocks | ~5-15x |
> | **MemorySanitizer (MSan)** | Uninitialized memory reads | ~3x |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 196 — Question 13: Multiple Fuzzers

> [!question] Question
> **Question 13: Multiple Fuzzers**
>
> Why does running multiple different fuzzers on the same target find 50% more bugs than any single tool?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Generation-Based vs Mutation-Based Fuzzing
>
> Orthogonal to the three generations, fuzzers differ in how they create inputs :
>
> | Approach | How it works | Strengths | Weaknesses |
> |----------|-------------|-----------|------------|
> | **Mutation-based** | Takes valid samples and applies anomalies (bit-flip, byte-flip, block deletion) | Easy to set up, no model required | Seed quality is critical; shallow coverage |
> | **Generation-based** | Creates inputs from scratch using a grammar or protocol model | Deeper coverage (25.5% vs 10.5-14.9% on libpng); finds ~15% more bugs | Requires building a model of the input format |
>
> An independent evaluation found that running multiple different fuzzers on the same target typically finds **50% more bugs** than any single tool in isolation . This validates the practice of combining mutation-based and generation-based fuzzers in production fuzzing campaigns.
>
> #### Evaluating Fuzzers
>
> Klees et al. established critical benchmarking standards after finding widespread methodological problems in fuzzing research :
>
> | Problem | Evidence | Recommendation |
> |---------|----------|----------------|
> | Single-run evaluations | 56% of papers used one run | **30+ independent trials** |
> | Crash ≠ bug | 57,142 AFL "unique crashes" → 9 actual bugs | **Ground truth measurement** |
> | Short campaigns | Performance rankings reverse over time | **24-hour minimum timeout** |
> | No statistical tests | Results may be due to randomness | **Mann-Whitney U test** |
> | Seed sensitivity | Different seeds → different results | **Report seed selection methodology** |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 197 — Question 14: QuickCheck Bug Distribution

> [!question] Question
> **Question 14: QuickCheck Bug Distribution**
>
> QuickCheck found bugs equally in implementations, specifications, and generators. Why is this surprising?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### If the program crashes or hangs → bug found
>
> ```
>
> 25-33% of utilities on seven UNIX variants crashed or hung. The failures exposed fundamental programming errors: pointer and array bounds violations, unchecked return values, race conditions, and signed character handling bugs.
>
> **Windows NT (2000)**: Extended to GUI applications — 21% of tested applications crashed and 24% hung on random valid Win32 messages; 100% failed on random raw messages . The study exposed a systematic Win32 API flaw: applications could not distinguish window messages from the OS versus those from other programs, creating an inherent vulnerability.
>
> **macOS X (2006)**: Command-line reliability improved to 7% crash rate (down from 33%), but GUI failure rate reached 73% — the worst ever recorded .
>
> **The longitudinal finding**: The same error classes — buffer overflows, null pointer dereferences, unchecked return values — persisted for 16 years across operating systems. Simple random testing continues to find bugs that sophisticated techniques miss .
>
> #### Key Insight: Where Bugs Hide
>
> QuickCheck's case studies revealed that errors are found roughly equally in three places :
>
> | Location | Proportion | Implication |
> |----------|------------|-------------|
> | **Implementation** | ~1/3 | The bugs you expect to find |
> | **Specification** | ~1/3 | Properties themselves are wrong — forces specification clarity |
> | **Generators** | ~1/3 | Test data generation is biased or incomplete |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 198 — Question 15: Hypothesis Byte-Stream Representation

> [!question] Question
> **Question 15: Hypothesis Byte-Stream Representation**
>
> What problem does Hypothesis's "universal byte-stream representation" solve?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Key Innovation: Universal Test Representation
>
> Instead of requiring separate generators, shrinkers, and validity filters for each type, Hypothesis uses a single underlying byte-stream representation. All test cases are sequences of choices from this stream, and shrinking operates uniformly by reducing the byte stream :
>
> - **No custom shrinker code** needed per type
> - **Automatic validity preservation** during shrinking
> - **Transparent targeted PBT** — can optimize toward specific goals without generator changes
>
> #### 4.2 Hypothesis: Modern PBT for Python
>
> MacIver and Hatfield-Dodds developed Hypothesis :
>
> **Key innovation:** Universal byte-stream representation — no custom shrinker needed per type.
>
> **Impact:** 100,000+ weekly downloads, ~4% of Python developers, found bugs in NumPy and Astropy.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 199 — Question 16: JQF Improvement

> [!question] Question
> **Question 16: JQF Improvement**
>
> How does JQF achieve a 1,000x improvement over random PBT?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.3 JQF: Where PBT Meets Fuzzing
>
> JQF bridges PBT and coverage-guided fuzzing :
>
> | Benchmark | Random PBT | Zest (Coverage-Guided) |
> |-----------|-----------|----------------------|
> | Trie bug | Not found in **7M+** executions | Found in **~5K** executions |
>
> **1,000x improvement** with coverage guidance. Found **42 bugs** in OpenJDK, Apache Commons, Google Closure, Mozilla Rhino .
>
> #### JQF: Where PBT Meets Fuzzing
>
> Padhye et al. bridged the gap between QuickCheck-style PBT and AFL-style coverage-guided fuzzing with JQF .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 200 — Question 17: PBT Property Challenge

> [!question] Question
> **Question 17: PBT Property Challenge**
>
> Why do 16 out of 30 PBT practitioners say "not knowing what properties to test" is the biggest challenge (Goldstein 2024)?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.4 PBT in Industry Practice
>
> Goldstein et al. conducted 30 interviews at Jane Street :
>
> | High-Leverage Pattern | Usage |
> |-----------------------|-------|
> | **Differential testing** | 17/30 |
> | **Round-trip** (encode-decode = identity) | 11/30 |
> | **Catastrophic failure** detection | 7/30 |
>
> **Primary challenge:** "Not knowing what properties to test" — 16/30 practitioners .
>
> {: .highlight }
> > **Exam Tip:** Know the PBT evolution: QuickCheck (2000, properties) → Hypothesis (2019, universal byte-stream) → JQF (2019, coverage-guided). The key number is 1,000x improvement from coverage guidance.
>
> #### Practical Constraints
>
> - **Time budgets are strict**: 50ms to 30s per property (vs. fuzzing campaigns of hours or days)
> - **Generator design is tedious**: 6/30 practitioners cited generator complexity as a major challenge
> - **The primary failure mode**: "not knowing what properties to test" — 16/30 found writing properties challenging
> - **Value beyond bugs**: PBT serves as executable documentation that "never falls out of date"

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 201 — Question 18: PBT vs Fuzzing Time Budgets

> [!question] Question
> **Question 18: PBT vs Fuzzing Time Budgets**
>
> Compare the time budgets of PBT (50ms-30s) versus fuzzing campaigns (hours/days). What does this reveal about their integration patterns?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.3 JQF: Where PBT Meets Fuzzing
>
> JQF bridges PBT and coverage-guided fuzzing :
>
> | Benchmark | Random PBT | Zest (Coverage-Guided) |
> |-----------|-----------|----------------------|
> | Trie bug | Not found in **7M+** executions | Found in **~5K** executions |
>
> **1,000x improvement** with coverage guidance. Found **42 bugs** in OpenJDK, Apache Commons, Google Closure, Mozilla Rhino .
>
> #### JQF: Where PBT Meets Fuzzing
>
> Padhye et al. bridged the gap between QuickCheck-style PBT and AFL-style coverage-guided fuzzing with JQF .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 202 — Question 19: Coupling Effect

> [!question] Question
> **Question 19: Coupling Effect**
>
> Explain the coupling effect and why it justifies testing with simple mutations only.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Coupling Effect
>
> > "Test data that distinguishes all programs differing from a correct one by only simple errors is so sensitive that it also implicitly distinguishes more complex errors."
>
> Empirical validation: test sets that killed all first-order mutants also killed over 99% of second- and third-order mutants . For Hoare's FIND algorithm, only 19 out of 22,000+ randomly generated complex-error mutants survived adequate test data — and all 19 were proven equivalent to the original .
>
> #### 2.4 Randoop: Feedback-Directed Random Testing
>
> Randoop builds test sequences incrementally :
>
> | Metric | Value |
> |--------|-------|
> | Errors found | **30** in 15 human hours (on code tested by 40 engineers for 5 years) |
> | Productivity | **100x** faster than manual testing |
> | Tests generated | 4,000,000 sequences |
>
> The **"plateau effect"** — error-finding rate drops from 5/hour to zero after ~12 hours .
>
> {: .highlight }
> > **Exam Tip:** Know the "20% rule" — 20% more random tests erase partition advantage (Ntafos 2001). Know the two scenarios where only random testing will do (Hamlet 2006).

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 203 — Question 20: Equivalent Mutant Problem

> [!question] Question
> **Question 20: Equivalent Mutant Problem**
>
> Why is the equivalent mutant problem considered the most persistent challenge in mutation testing?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The Equivalent Mutant Problem
>
> Some mutants produce identical behavior to the original program for all possible inputs. These **equivalent mutants** cannot be killed by any test and must be identified and excluded from the mutation score calculation.
>
> #### 5.4 The Equivalent Mutant Problem
>
> 10-40% of mutants are equivalent — undecidable to detect .
>
> **LLM-Assisted Detection:** Fine-tuned UniXCoder (110M params) achieves **86.58% F1-score** vs GPT-4 at 55.90% .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 204 — Question 21: Small vs Large LLMs for Mutant Detection

> [!question] Question
> **Question 21: Small vs Large LLMs for Mutant Detection**
>
> Why does a smaller code-specific model (UniXCoder, 110M parameters) outperform GPT-4 on equivalent mutant detection (Tian 2024)?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### LLM-Assisted Detection
>
> Tian et al. conducted the first large-scale study of LLMs for equivalent mutant detection on 3,302 Java mutant pairs :
>
> | Approach | Best Model | F1-Score |
> |----------|-----------|----------|
> | **Fine-tuned code embeddings** | UniXCoder (110M params) | **86.58%** |
> | **Pre-trained code embeddings** | UniXCoder | 82.18% |
> | **Few-shot prompting** | GPT-4 | 55.90% |
> | **Best baseline (non-LLM)** | ASTNN | 70.00% |
>
> Key findings:
> - LLMs achieve 35.69% average F1-score improvement over existing techniques
> - **Smaller code-specific models outperform larger general models** — UniXCoder (110M parameters) beats GPT-4 and text-embedding models
> - Prompting alone is insufficient; fine-tuning on code embeddings is necessary
> - Inference time is acceptable: 0.0431 seconds per mutant pair
>
> #### 5.4 The Equivalent Mutant Problem
>
> 10-40% of mutants are equivalent — undecidable to detect .
>
> **LLM-Assisted Detection:** Fine-tuned UniXCoder (110M params) achieves **86.58% F1-score** vs GPT-4 at 55.90% .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 205 — Question 22: Crossfire Phenomenon

> [!question] Question
> **Question 22: Crossfire Phenomenon**
>
> What is the "crossfire" phenomenon in mutation testing?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.1 What is Mutation Testing?
>
> Mutation testing introduces small deliberate changes (mutants) into the program and checks whether existing tests catch them .
>
> $$\text{Mutation Score} = \frac{\text{Killed}}{\text{Total} - \text{Equivalent}} \times 100\%$$
>
> #### 5.5 Mutation Testing in Practice
>
> Smith and Williams : 2-9% coverage gain in 60 minutes, ~1 new test every 6 minutes. **"Crossfire"** — one test kills multiple mutants.
>
> {: .highlight }
> > **Exam Tip:** Know the mutation score formula. Know the 5 essential operators (ABS, UOI, LCR, AOR, ROR) and that they achieve 99.5% effectiveness. Know that 10-40% of mutants are equivalent and detection is undecidable.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 206 — Question 23: Mutation Score Target

> [!question] Question
> **Question 23: Mutation Score Target**
>
> A team achieves 85% mutation score. Should they aim for 100%? Why or why not?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.1 What is Mutation Testing?
>
> Mutation testing introduces small deliberate changes (mutants) into the program and checks whether existing tests catch them .
>
> $$\text{Mutation Score} = \frac{\text{Killed}}{\text{Total} - \text{Equivalent}} \times 100\%$$
>
> #### 5.5 Mutation Testing in Practice
>
> Smith and Williams : 2-9% coverage gain in 60 minutes, ~1 new test every 6 minutes. **"Crossfire"** — one test kills multiple mutants.
>
> {: .highlight }
> > **Exam Tip:** Know the mutation score formula. Know the 5 essential operators (ABS, UOI, LCR, AOR, ROR) and that they achieve 99.5% effectiveness. Know that 10-40% of mutants are equivalent and detection is undecidable.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 207 — Question 24: Mutation vs PBT Comparison

> [!question] Question
> **Question 24: Mutation vs PBT Comparison**
>
> Compare how mutation testing and property-based testing approach test quality. How are they complementary?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The Convergence with Property-Based Testing
>
> Pure fuzzing mutates bytes without understanding input structure. Property-based testing generates structured inputs without coverage feedback. **JQF** bridges both paradigms : coverage-guided mutation of structured inputs.
>
> Where pure random testing failed to find a Trie bug in 7 million+ executions, Zest (coverage-guided) found it in approximately 5,000 executions — a **1,000x improvement** .
>
> See [Property-Based Testing](property-based) for the full PBT story.
>
> #### Property-Based Testing
>
> Property-based testing (PBT) combines random input generation with executable specifications. Instead of writing individual test cases with expected outputs, developers write **properties** — statements that should hold for all inputs — and the tool generates hundreds or thousands of random inputs to find counterexamples.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 208 — Question 25: Branch Coverage and Mutation

> [!question] Question
> **Question 25: Branch Coverage and Mutation**
>
> What is the relation between branch coverage and mutation testing? Does one subsume the other?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Mutation Testing
>
> Mutation testing measures the fault-detection effectiveness of a test suite by introducing small, deliberate changes (mutants) into the program and checking whether existing tests catch them. It answers a fundamental question: **if a bug were present, would your tests find it?**
>
> For an introduction to mutation operators and mutation score, see [Mutation Coverage](../coverage/mutation).
>
> ```mermaid
> flowchart LR
>     A["Original<br>Program"] --> B["Apply Mutation<br>Operators"]
>     B --> C["Mutants"]
>     C --> D["Run Test Suite"]
>     D --> E{"Test fails?"}
>     E -- "Yes" --> F["Killed"]
>     E -- "No" --> G{"Equivalent?"}
>     G -- "Yes" --> H["Exclude"]
>     G -- "No" --> I["Survives — weak test"]
>
>     style F fill:#c8e6c9,stroke:#388e3c
>     style I fill:#ffcdd2,stroke:#c62828
>     style H fill:#e0e0e0,stroke:#757575
> ```
>
> #### 5.1 What is Mutation Testing?
>
> Mutation testing introduces small deliberate changes (mutants) into the program and checks whether existing tests catch them .
>
> $$\text{Mutation Score} = \frac{\text{Killed}}{\text{Total} - \text{Equivalent}} \times 100\%$$

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 209 — Question 26: Random vs Partition — Short Answer

> [!question] Question
> **Question 26: Random vs Partition — Short Answer**
>
> Is random testing better than partition testing? Under what conditions does each approach excel?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Random vs. Partition Testing
>
> A persistent question in testing theory: does systematic partition testing outperform random testing?
>
> The debate has a nuanced resolution :
>
> - **Random wins** when no meaningful partition exists, cost matters, operational profile testing is needed, or stateful systems require sequence testing
> - **Partition wins** when subdomains are genuinely homogeneous and cost-weighted failure rates vary significantly across subdomains
> - **The gap is small**: roughly 20% more random tests erase any partition advantage , and just 1-2 additional random tests can tilt the balance at scale
>
> The practical answer: combine both — random testing first for broad coverage and reliability estimation, followed by targeted systematic testing for edge cases .
>
> #### 2.3 Random vs. Partition Testing
>
> The debate has been running since 1984 :
>
> | Year | Authors | Finding |
> |------|---------|---------|
> | 1984 | Duran & Ntafos | Random often more cost-effective |
> | 2001 | Ntafos | ~20% more random tests erase partition advantage |
> | 2006 | Hamlet | Only random will do for unstructured spaces and state-dependent systems |
>
> **Resolution (Ntafos 2001):** The gap shrinks to <0.05% at scale. Roughly 20% more random tests eliminate any partition testing advantage .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 210 — Question 27: Fuzz Testing Definition

> [!question] Question
> **Question 27: Fuzz Testing Definition**
>
> What is fuzz testing? How is it different from random testing? Compare inputs, focus, and oracle.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.2 Why Use Random Testing?
>
> | Benefit | Explanation |
> |---------|-------------|
> | **Cheap** | Once the oracle is solved, generating inputs is trivial |
> | **Probabilistic guarantees** | Can calculate reliability bounds  |
> | **Complements partition** | Finds different faults than systematic testing |
> | **Scales well** | Can generate millions of tests automatically |
>
> Random testing is particularly useful when domain knowledge is lacking, the state space is large, or reliability calculations are required .
>
> {: .highlight }
> > **Exam Tip:** Random testing is NOT haphazard testing. It requires a defined distribution, statistical independence, and an oracle. Memorize these three requirements.
>
> #### 1.1 What is Random Testing?
>
> Random testing selects test inputs independently at random from the program's input domain . It is not haphazard — it requires:
>
> 1. A **defined input distribution** (operational profile or uniform)
> 2. **Statistical independence** between test selections
> 3. An **oracle** to determine pass/fail
>
> | "Random" in Testing | "Random" Elsewhere |
> |--------------------|--------------------|
> | Systematic exploration | Arbitrary selection |
> | Statistical guarantees | No guarantees |
> | Automated generation | Manual "pick some" |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 211 — Question 28: Oracle Problem

> [!question] Question
> **Question 28: Oracle Problem**
>
> What is the oracle problem? Why is it the bottleneck of random testing?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.2 The Oracle Problem
>
> The oracle determines what class of bugs random testing can find :
>
> | Oracle Type | Description | Overhead |
> |-------------|-------------|----------|
> | **Gold standard** | Reference implementation | High |
> | **Crash detection** | Detect crashes/hangs | None |
> | **Sanitizers** | ASan (~73%), UBSan (~20%), TSan (~5-15x) | Variable |
> | **Assertions** | Pre/postconditions | Low |
> | **Properties** | Invariants for all inputs | Medium |
>
> **Key insight:** The oracle is the bottleneck. Random testing is only practical with automated evaluation .
>
> #### 1.1 What is Random Testing?
>
> Random testing selects test inputs independently at random from the program's input domain . It is not haphazard — it requires:
>
> 1. A **defined input distribution** (operational profile or uniform)
> 2. **Statistical independence** between test selections
> 3. An **oracle** to determine pass/fail
>
> | "Random" in Testing | "Random" Elsewhere |
> |--------------------|--------------------|
> | Systematic exploration | Arbitrary selection |
> | Statistical guarantees | No guarantees |
> | Automated generation | Manual "pick some" |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 212 — Question 29: Oracle Evolution

> [!question] Question
> **Question 29: Oracle Evolution**
>
> Trace the evolution of oracles across the four techniques: random testing, fuzz testing, property-based testing, and mutation testing.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The Convergence with Property-Based Testing
>
> Pure fuzzing mutates bytes without understanding input structure. Property-based testing generates structured inputs without coverage feedback. **JQF** bridges both paradigms : coverage-guided mutation of structured inputs.
>
> Where pure random testing failed to find a Trie bug in 7 million+ executions, Zest (coverage-guided) found it in approximately 5,000 executions — a **1,000x improvement** .
>
> See [Property-Based Testing](property-based) for the full PBT story.
>
> #### Why Random Testing?
>
> Systematic testing strategies require human judgement to select inputs. That judgement introduces bias: testers exercise the cases they anticipate, missing the unexpected interactions that cause real failures. Random testing bypasses this bias entirely.
>
> The empirical evidence is compelling:
>
> - **Miller's 16-year fuzz series** found that 25-33% of UNIX utilities crashed on random input , and the same error classes persisted for over a decade
> - **Randoop** found 30 errors in a .NET component already tested by 40 engineers for 5 years — more than a tester typically finds in a year
> - **QuickCheck** discovered bugs in production Haskell libraries with a 300-line tool, finding errors equally distributed across generators, specifications, and implementations
>
> Random testing also uniquely supports **statistical reliability prediction**: after N successful random tests drawn from an operational profile, one can bound the probability of undetected failure .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 213 — Question 30: Single Technique Selection

> [!question] Question
> **Question 30: Single Technique Selection**
>
> If you could only apply one technique from this lecture to a new project, which would you choose and why? Consider different project types.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Part 6: Summary — Choosing the Right Technique
>
> | Technique | Purpose | Oracle | Key Result |
> |-----------|---------|--------|------------|
> | **Random** | Find faults | Required | 90% confidence @ 23K tests |
> | **Fuzz** | Security bugs | Crash / sanitizers | 25-33% of apps crash |
> | **PBT** | Specification bugs | Properties | 1,000x with coverage guidance |
> | **Mutation** | Test quality | Existing tests | 5 operators cover 99.5% |
>
> **The oracle determines the ceiling** — from crash detection to properties to differential testing.
>
> #### Randoop
>
> Randoop builds test sequences incrementally :
>
> 1. Start with simple sequences (constructors, constants)
> 2. Randomly select a method to call
> 3. Choose arguments from previously constructed sequences
> 4. Execute immediately and classify:
>    - **Error-revealing** → report as bug, do not extend
>    - **Illegal** (e.g., `ArgumentException` on null) → discard
>    - **New** (creates novel object states) → add to pool for extension
>
> Key results on a .NET component tested by 40 engineers for 5 years:
>
> | Metric | Value |
> |--------|-------|
> | Errors found | 30 (in 15 human hours, 150 CPU hours) |
> | Productivity | 100x faster than manual testing |
> | Tests generated | 4,000,000 sequences |
> | Coverage finding | Found errors in code with 100% block and arc coverage |
>
> The "plateau effect" — error-finding rate dropping from 5/hour to zero after ~12 hours — reveals the limitation of uniform random method selection: classes with simple constructors are explored disproportionately .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 214 — Question 31: Bug Classes vs Tool Progress

> [!question] Question
> **Question 31: Bug Classes vs Tool Progress**
>
> The same bug classes persisted for 16 years (Miller studies). Meanwhile, LLMs detect 86% of equivalent mutants. What does this contrast tell us?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Mutant 3 (equivalent!): swapping b==c and a==c   ← same behavior for all inputs
>
> ```
>
> A test suite that kills Mutants 1 and 2 but cannot kill Mutant 3 (because it is **equivalent**) achieves a mutation score of 2/2 = 100%.
>
> #### 3.3 Miller's Fuzz Studies (16-Year Longitudinal)
>
> | Year | Target | Crash Rate |
> |------|--------|------------|
> | 1990 | UNIX utilities | **25-33%**  |
> | 2000 | Windows NT apps | **21%** (+24% hang)  |
> | 2006 | macOS CLI | 7% (improved)  |
> | 2006 | macOS GUI | **73%** (worst ever)  |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 215 — Question 32: Testing Strategy Design (Practical)

> [!question] Question
> **Question 32: Testing Strategy Design (Practical)**
>
> Design a testing strategy for a JSON parser that combines techniques from all four topics (random testing, fuzzing, PBT, mutation testing).

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.3 JQF: Where PBT Meets Fuzzing
>
> JQF bridges PBT and coverage-guided fuzzing :
>
> | Benchmark | Random PBT | Zest (Coverage-Guided) |
> |-----------|-----------|----------------------|
> | Trie bug | Not found in **7M+** executions | Found in **~5K** executions |
>
> **1,000x improvement** with coverage guidance. Found **42 bugs** in OpenJDK, Apache Commons, Google Closure, Mozilla Rhino .
>
> #### Random Testing Fundamentals
>
> Random testing selects test inputs by sampling from input distributions rather than deriving them from code structure or specifications. This section covers the theory, reliability arguments, sampling strategies, and feedback-directed tools that make random testing practical.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 216 — Question 33: JQF's Significance (Practical)

> [!question] Question
> **Question 33: JQF's Significance (Practical)**
>
> Why might JQF's convergence of PBT and fuzzing be the most significant development across all four topics? Explain how it resolves limitations of both approaches.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.3 JQF: Where PBT Meets Fuzzing
>
> JQF bridges PBT and coverage-guided fuzzing :
>
> | Benchmark | Random PBT | Zest (Coverage-Guided) |
> |-----------|-----------|----------------------|
> | Trie bug | Not found in **7M+** executions | Found in **~5K** executions |
>
> **1,000x improvement** with coverage guidance. Found **42 bugs** in OpenJDK, Apache Commons, Google Closure, Mozilla Rhino .
>
> #### JQF: Where PBT Meets Fuzzing
>
> Padhye et al. bridged the gap between QuickCheck-style PBT and AFL-style coverage-guided fuzzing with JQF .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

### Card 217 — Question 34: Pesticide Paradox (Practical)

> [!question] Question
> **Question 34: Pesticide Paradox (Practical)**
>
> Explain how the "pesticide paradox" applies across all four testing techniques covered in this lecture. What is the universal mitigation?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Random vs. Partition Testing
>
> A persistent question in testing theory: does systematic partition testing outperform random testing?
>
> The debate has a nuanced resolution :
>
> - **Random wins** when no meaningful partition exists, cost matters, operational profile testing is needed, or stateful systems require sequence testing
> - **Partition wins** when subdomains are genuinely homogeneous and cost-weighted failure rates vary significantly across subdomains
> - **The gap is small**: roughly 20% more random tests erase any partition advantage , and just 1-2 additional random tests can tilt the balance at scale
>
> The practical answer: combine both — random testing first for broad coverage and reliability estimation, followed by targeted systematic testing for edge cases .
>
> #### Random Testing Fundamentals
>
> Random testing selects test inputs by sampling from input distributions rather than deriving them from code structure or specifications. This section covers the theory, reliability arguments, sampling strategies, and feedback-directed tools that make random testing practical.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/random/RQ_L06_Random.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/random/RQ_L06_Random.md)

## Exploratory Testing & Operational Profile (30)

### Card 218 — Question 1: ET vs OP Fundamental Difference

> [!question] Question
> **Question 1: ET vs OP Fundamental Difference**
>
> What is the fundamental difference between exploratory testing and operational profile-based testing?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Why Exploratory Testing?
>
> The empirical evidence across five controlled experiments consistently shows :
>
> | Finding | Evidence |
> |---------|----------|
> | **Matches scripted testing** in defect detection | No significant difference in 4 of 5 experiments |
> | **4-6x more efficient** when total effort counted | ET: 4.58h vs. TCT: 19.47h for equivalent results  |
> | **Fewer false positives** | TCT produces 2x more false defect reports  |
> | **88% industry adoption** | Mainstream practice, not academic theory  |
>
> However, ET consistently achieves **lower systematic coverage** than scripted testing , creating a fundamental trade-off between efficiency and coverage assurance.
>
> #### 2.1 What is Exploratory Testing?
>
> Exploratory testing is **simultaneous learning, test design, and test execution** . The tester observes the system, forms hypotheses, and tests them immediately.
>
> Key characteristics:
> - **Not ad-hoc:** ET uses charters, heuristics, and sessions for structure
> - **Cognitive engagement:** The tester's thinking drives test design in real time
> - **Feedback-driven:** Each test result informs the next test
>
> > "The result of each test leads you to design the next" — Elisabeth Hendrickson

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 219 — Question 2: Scripted + Exploratory = Coverage

> [!question] Question
> **Question 2: Scripted + Exploratory = Coverage**
>
> Why does the lecture say "scripted + exploratory = coverage"? What types of defects does each approach find?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### ET Complements Scripted Testing
>
> The evidence consistently shows ET and scripted testing are **complementary**, not competing approaches:
>
> ```mermaid
> flowchart LR
>     subgraph et["Exploratory Testing"]
>         direction TB
>         E1["Usability defects"]
>         E2["GUI defects"]
>         E3["Edge cases"]
>         E4["Unknown unknowns"]
>     end
>
>     subgraph st["Scripted Testing"]
>         direction TB
>         S1["Specification conformance"]
>         S2["Regression detection"]
>         S3["Systematic coverage"]
>         S4["Traceability to requirements"]
>     end
>
>     subgraph overlap["Both Find"]
>         direction TB
>         O1["Functional defects"]
>         O2["Logic errors"]
>     end
>
>     et --- overlap --- st
>
>     style et fill:#c8e6c9,stroke:#388e3c
>     style st fill:#bbdefb,stroke:#1976d2
>     style overlap fill:#fff9c4,stroke:#f9a825
> ```
>
> | Dimension | ET Strength | Scripted Strength |
> |-----------|-------------|-------------------|
> | Defect types | Usability, GUI, edge cases  | Conformance, specification-based |
> | Efficiency | Higher (no design overhead) | — |
> | Coverage | — | Higher systematic coverage  |
> | Traceability | — | Full traceability to requirements |
> | Adaptability | High (responds to discoveries) | Low (follows script) |
>
> > "ET is not a replacement for existing test-case based approaches, but a complementary testing approach suitable for certain situations"
>
> #### 2.8 The Coverage Paradox
>
> ET consistently achieves **lower structural coverage** than scripted testing (Shah 2014 ), yet matches or exceeds it in defect counts. This apparent contradiction has three explanations:
>
> 1. **Coverage measures traversal, not fault-revealing power.** Code coverage records which statements or branches were executed — not whether those executions stressed the system. Scripted tests systematically execute all branches, but many of those executions use "expected" inputs on "expected" paths. The code runs without finding a bug not because the bug isn't there, but because the input didn't trigger it.
>
> 2. **Defects cluster.** Most bugs are concentrated in a small fraction of the codebase — the complex, edge-case-heavy modules. ET testers, guided by heuristics and active reasoning, naturally gravitate toward complexity and anomalies. They reach high-defect areas without covering the full structural map.
>
> 3. **ET exercises paths with higher fault-revealing inputs.** Even when an ET tester and a scripted tester both execute the same branch, the ET tester is more likely to do so with adversarial, boundary-probing, or semantically interesting inputs. Coverage counts the path once; it doesn't distinguish between a routine traversal and a targeted probe.
>
> {: .highlight }
> > **Exam Tip:** Coverage is a **necessary but not sufficient** condition for fault detection. Executing code does not guarantee finding bugs in it — it depends on *how* the code is executed. ET achieves comparable fault detection with lower coverage because it optimises the *quality* of each execution, not the breadth.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 220 — Question 3: ET vs Ad-Hoc Testing

> [!question] Question
> **Question 3: ET vs Ad-Hoc Testing**
>
> How does exploratory testing differ from ad-hoc testing?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.1 What is Exploratory Testing?
>
> Exploratory testing is **simultaneous learning, test design, and test execution** . The tester observes the system, forms hypotheses, and tests them immediately.
>
> Key characteristics:
> - **Not ad-hoc:** ET uses charters, heuristics, and sessions for structure
> - **Cognitive engagement:** The tester's thinking drives test design in real time
> - **Feedback-driven:** Each test result informs the next test
>
> > "The result of each test leads you to design the next" — Elisabeth Hendrickson
>
> #### Exploratory Testing
>
> **Exploratory testing (ET)** is simultaneous learning, test design, and test execution . Unlike ad-hoc testing, ET operates within predefined testing parameters — it uses structured heuristics, charters, and sessions to guide the tester's investigation .
>
> ET is not the absence of structure but a different relationship between test design and execution: the tester's cognitive engagement during testing replaces upfront test case documentation.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 221 — Question 4: Coupon System Example

> [!question] Question
> **Question 4: Coupon System Example**
>
> Explain the coupon system example. Why couldn't scripted testing find those bugs?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### ET Complements Scripted Testing
>
> The evidence consistently shows ET and scripted testing are **complementary**, not competing approaches:
>
> ```mermaid
> flowchart LR
>     subgraph et["Exploratory Testing"]
>         direction TB
>         E1["Usability defects"]
>         E2["GUI defects"]
>         E3["Edge cases"]
>         E4["Unknown unknowns"]
>     end
>
>     subgraph st["Scripted Testing"]
>         direction TB
>         S1["Specification conformance"]
>         S2["Regression detection"]
>         S3["Systematic coverage"]
>         S4["Traceability to requirements"]
>     end
>
>     subgraph overlap["Both Find"]
>         direction TB
>         O1["Functional defects"]
>         O2["Logic errors"]
>     end
>
>     et --- overlap --- st
>
>     style et fill:#c8e6c9,stroke:#388e3c
>     style st fill:#bbdefb,stroke:#1976d2
>     style overlap fill:#fff9c4,stroke:#f9a825
> ```
>
> | Dimension | ET Strength | Scripted Strength |
> |-----------|-------------|-------------------|
> | Defect types | Usability, GUI, edge cases  | Conformance, specification-based |
> | Efficiency | Higher (no design overhead) | — |
> | Coverage | — | Higher systematic coverage  |
> | Traceability | — | Full traceability to requirements |
> | Adaptability | High (responds to discoveries) | Low (follows script) |
>
> > "ET is not a replacement for existing test-case based approaches, but a complementary testing approach suitable for certain situations"
>
> #### 2.2 ET in Practice — The Coupon Example
>
> An exploratory tester with the charter *"Explore the coupon system using unusual input combinations to discover pricing errors"* discovers in a 90-minute session:
>
> | # | Action | Bug Found |
> |---|--------|-----------|
> | 1 | Apply coupon twice | Discount doubles |
> | 2 | Coupon on sale item | Price goes negative |
> | 3 | Apply coupon, then remove items | Discount stays, subtotal < 0 |
> | 4 | Two browser tabs, different coupons | Both coupons apply |
>
> None of these bugs were in any test plan.
>
> {: .highlight }
> > **Exam Tip:** Be able to explain the coupon example. It illustrates how ET finds bugs that no script anticipated — through real-time reasoning.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 222 — Question 5: Charter Definition

> [!question] Question
> **Question 5: Charter Definition**
>
> What is a charter and why is it important for exploratory testing? Give the template format.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.1 What is Exploratory Testing?
>
> Exploratory testing is **simultaneous learning, test design, and test execution** . The tester observes the system, forms hypotheses, and tests them immediately.
>
> Key characteristics:
> - **Not ad-hoc:** ET uses charters, heuristics, and sessions for structure
> - **Cognitive engagement:** The tester's thinking drives test design in real time
> - **Feedback-driven:** Each test result informs the next test
>
> > "The result of each test leads you to design the next" — Elisabeth Hendrickson
>
> #### Empirical Evidence for Exploratory Testing
>
> The effectiveness of exploratory testing has been studied through multiple controlled experiments and industrial case studies. The evidence converges on three robust findings: ET matches scripted testing in defect detection, is dramatically more efficient, and produces fewer false positives.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 223 — Question 6: Hendrickson's Heuristics

> [!question] Question
> **Question 6: Hendrickson's Heuristics**
>
> Describe three of Hendrickson's heuristics and give an example for each.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Hendrickson's Heuristics
>
> Elisabeth Hendrickson provides a complementary set of lightweight heuristics for test idea generation :
>
> #### 2.3 Hendrickson's Heuristics
>
> **Charter template:** Every session begins with a charter:
>
> > **Explore** [target] **using** [resources] **to discover** [information]
>
> **Core heuristics:**
>
> | Heuristic | What to Try | Example |
> |-----------|-------------|---------|
> | **None, Some, All** | Empty, partial, full sets | Permissions: none → admin access bug? |
> | **Too Big, Too Small, Just Right** | Size extremes (Goldilocks) | Image upload: 3 MB, empty, 50 KB |
> | **Beginning, Middle, End** | Position variations | Edit at start/middle/end of line |
> | **Zero, One, Many** | Count variations | Invoices with 0, 1, 100 items |
> | **CRUD** | All data operations | Create, Read, Update, Delete each entity |
> | **Command Injection** | Malicious input | Single quote in search → SQL error? |
> | **Data Type Attacks** | Type boundaries | Feb 30, 13:75, 2^32+1 |
>
> **The Nightmare Headline Game:** Ask *"What would be the worst headline if this software fails?"*

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 224 — Question 7: Session-Based Test Management

> [!question] Question
> **Question 7: Session-Based Test Management**
>
> Explain Session-Based Test Management (SBTM). Why was it created? What are its four pillars?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.4 Session-Based Test Management (SBTM)
>
> **The four pillars** :
>
> | Pillar | Details |
> |--------|---------|
> | **Charter** | What to explore, how, and what problems to seek |
> | **Time Box** | 60-120 minutes |
> | **Reviewable Result** | Bug reports, coverage notes, issues |
> | **Debriefing** | Post-session review with manager/team |
>
> **Debriefing questions:** How did you spend your time? What did you find? Did you need special knowledge? Is there more to do?
>
> {: .highlight }
> > **Exam Tip:** Know the four SBTM pillars (Charter, Time Box, Reviewable Result, Debriefing) and the debriefing questions.
>
> #### Session-Based Test Management
>
> A key obstacle to ET adoption is accountability: how do managers track testing progress without test cases? **Session-Based Test Management (SBTM)**, introduced by Jonathan Bach, provides a management framework that brings structure and metrics to exploratory testing without constraining the tester's freedom .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 225 — Question 8: Whittaker's Five Districts

> [!question] Question
> **Question 8: Whittaker's Five Districts**
>
> What are Whittaker's five districts and what does each focus on?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.5 Whittaker's Tourist Metaphor — Five Districts
>
> James Whittaker organizes exploration using a tourist metaphor :
>
> | District | Focus | Key Tours |
> |----------|-------|-----------|
> | **Business** | Features users rely on daily | Guidebook Tour, Money Tour |
> | **Historical** | Legacy code and old features | Bad Neighborhood Tour, Museum Tour |
> | **Entertainment** | Fun, unusual inputs | Obsessive-Compulsive Tour, Antisocial Tour |
> | **Tourist** | First-time user experience | Collector's Tour, Supermodel Tour |
> | **Hotel** | Background processes | All-Nighter Tour, TOGOF |
>
> #### The Five Districts
>
> ```mermaid
> mindmap
>   root((Software<br>Under Test))
>     Business District
>       Guidebook Tour
>       Money Tour
>       Landmark Tour
>     Historical District
>       Bad Neighborhood Tour
>       Museum Tour
>     Entertainment District
>       Obsessive-Compulsive Tour
>       Couch Potato Tour
>     Tourist District
>       Collector's Tour
>       Supermodel Tour
>     Hotel District
>       All-Nighter Tour
>       TOGOF Tour<br>(Good Old Features)
> ```
>
> | District | Focus | Example Tours |
> |----------|-------|--------------|
> | **Business District** | Features users rely on daily | Guidebook Tour, Money Tour, Landmark Tour |
> | **Historical District** | Legacy code and old features | Bad Neighborhood Tour, Museum Tour |
> | **Entertainment District** | Fun, unusual inputs | Obsessive-Compulsive Tour, Couch Potato Tour |
> | **Tourist District** | First-time user experience | Collector's Tour, Supermodel Tour |
> | **Hotel District** | Background processes | All-Nighter Tour, TOGOF Tour (Tour Of Good Old Features — verify that existing features still work after changes) |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 226 — Question 9: Five Levels of Exploration

> [!question] Question
> **Question 9: Five Levels of Exploration**
>
> Describe the five levels of exploration (Ghazi 2017). When should you use each?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.6 Five Levels of Exploration
>
> ET and scripted testing form a spectrum :
>
> | Level | Tester Receives | Example |
> |-------|----------------|---------|
> | **1. Freestyle** | Only the test object | "Here's our app. Find problems." |
> | **2. High exploration** | Charter with goals | "Explore attachments for security issues." |
> | **3. Medium** | Charter + starting points | "Try PDFs > 10 MB, ZIP files, Unicode names." |
> | **4. Low exploration** | Detailed activities | "Upload PDF, upload ZIP, upload while offline." |
> | **5. Fully scripted** | Steps + expected results | "Step 1: Click Attach. Step 2: Select file. Expected: success." |
>
> **Industrial finding:** Ericsson used 80% scripted / 20% ET; the evidence-based recommendation was **~57% exploratory** .
>
> {: .highlight }
> > **Exam Tip:** Know the five levels and concrete examples. The "right" level depends on context (finding new defects → higher; regulatory → lower).
>
> #### Purpose
>
> These study notes cover two complementary testing approaches: **exploratory testing** (qualitative, human-driven discovery) and **operational profile-based testing** (quantitative, usage-driven prioritization). The lecture traces ET from its definition through structured heuristics and empirical evidence, then connects it to operational profiles — from Musa's foundational work (1993) through modern developments like operational coverage and Android Cloud Profiles.
>
> **Primary Sources:**
> - Musa 1993, Operational Profiles in Software-Reliability Engineering
> - Whittaker 2009, Exploratory Software Testing
> - Hendrickson 2013, Explore It!
>
> **Key Research Papers:**
> - Itkonen & Mantyla 2007, 2014: ET vs. scripted testing experiments
> - Afzal et al. 2015: Equal-time ET experiment
> - Ghazi et al. 2017: Five levels of exploration
> - Miranda & Bertolino 2016, 2018: Operational coverage
> - Bleier et al. 2025: Android Cloud Profiles

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 227 — Question 10: ET Effectiveness Evidence

> [!question] Question
> **Question 10: ET Effectiveness Evidence**
>
> Summarize the empirical evidence for ET effectiveness. Include defect detection rates, efficiency comparisons, and industry adoption.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### [Empirical Evidence](effectiveness)
>
> Comprehensive effectiveness data:
> - Five controlled experiments comparing ET vs. scripted testing
> - Industrial case studies and defect detection rates
> - The role of tester knowledge and experience
>
> #### Industrial Defect Detection Rates
>
> Studies of ET in real organizations show consistently high defect detection rates :
>
> | Organization | ET Method | Defect Rate |
> |--------------|-----------|-------------|
> | Industrial sessions | Session-based ET | 4.8-8.7 defects/hour |
> | Benchmarks | Usage-based testing | <3 defects/hour |
> | Benchmarks | Functional testing | 2.47 defects/hour |
>
> Six distinct ET approaches observed in industry :
>
> 1. **Session-based ET** (structured, chartered)
> 2. **Functional testing of features** (feature-focused exploration)
> 3. **Exploratory smoke testing** (quick coverage check)
> 4. **Exploratory regression testing** (explore after changes)
> 5. **Subcontracted ET** (real end-users explore)
> 6. **Freestyle ET** (unstructured exploration)

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 228 — Question 11: Defending ET to Management

> [!question] Question
> **Question 11: Defending ET to Management**
>
> A manager says "ET is just ad-hoc testing." How would you respond with evidence?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Empirical Evidence for Exploratory Testing
>
> The effectiveness of exploratory testing has been studied through multiple controlled experiments and industrial case studies. The evidence converges on three robust findings: ET matches scripted testing in defect detection, is dramatically more efficient, and produces fewer false positives.
>
> #### ET vs. Ad-Hoc Testing
>
> {: .important }
> > "Don't mix ET with Session Based Testing. The plainest definition of exploratory testing is test design and test execution at the same time. ET is an approach, not another testing technique." — Industry practitioner
>
> | Aspect | Ad-Hoc Testing | Exploratory Testing |
> |--------|----------------|---------------------|
> | Planning | None | Charter, goals, heuristics |
> | Structure | Random, unguided | Structured by techniques and sessions |
> | Documentation | None | Session notes, defect logs |
> | Reproducibility | Low | Medium (via session reports) |
> | Skill dependency | Low | High (domain knowledge, test design intuition) |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 229 — Question 12: ET Coverage Paradox

> [!question] Question
> **Question 12: ET Coverage Paradox**
>
> Why does ET achieve lower coverage but comparable defect counts to scripted testing?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.8 The Coverage Paradox
>
> ET consistently achieves **lower structural coverage** than scripted testing (Shah 2014 ), yet matches or exceeds it in defect counts. This apparent contradiction has three explanations:
>
> 1. **Coverage measures traversal, not fault-revealing power.** Code coverage records which statements or branches were executed — not whether those executions stressed the system. Scripted tests systematically execute all branches, but many of those executions use "expected" inputs on "expected" paths. The code runs without finding a bug not because the bug isn't there, but because the input didn't trigger it.
>
> 2. **Defects cluster.** Most bugs are concentrated in a small fraction of the codebase — the complex, edge-case-heavy modules. ET testers, guided by heuristics and active reasoning, naturally gravitate toward complexity and anomalies. They reach high-defect areas without covering the full structural map.
>
> 3. **ET exercises paths with higher fault-revealing inputs.** Even when an ET tester and a scripted tester both execute the same branch, the ET tester is more likely to do so with adversarial, boundary-probing, or semantically interesting inputs. Coverage counts the path once; it doesn't distinguish between a routine traversal and a targeted probe.
>
> {: .highlight }
> > **Exam Tip:** Coverage is a **necessary but not sufficient** condition for fault detection. Executing code does not guarantee finding bugs in it — it depends on *how* the code is executed. ET achieves comparable fault detection with lower coverage because it optimises the *quality* of each execution, not the breadth.
>
> #### ET Complements Scripted Testing
>
> The evidence consistently shows ET and scripted testing are **complementary**, not competing approaches:
>
> ```mermaid
> flowchart LR
>     subgraph et["Exploratory Testing"]
>         direction TB
>         E1["Usability defects"]
>         E2["GUI defects"]
>         E3["Edge cases"]
>         E4["Unknown unknowns"]
>     end
>
>     subgraph st["Scripted Testing"]
>         direction TB
>         S1["Specification conformance"]
>         S2["Regression detection"]
>         S3["Systematic coverage"]
>         S4["Traceability to requirements"]
>     end
>
>     subgraph overlap["Both Find"]
>         direction TB
>         O1["Functional defects"]
>         O2["Logic errors"]
>     end
>
>     et --- overlap --- st
>
>     style et fill:#c8e6c9,stroke:#388e3c
>     style st fill:#bbdefb,stroke:#1976d2
>     style overlap fill:#fff9c4,stroke:#f9a825
> ```
>
> | Dimension | ET Strength | Scripted Strength |
> |-----------|-------------|-------------------|
> | Defect types | Usability, GUI, edge cases  | Conformance, specification-based |
> | Efficiency | Higher (no design overhead) | — |
> | Coverage | — | Higher systematic coverage  |
> | Traceability | — | Full traceability to requirements |
> | Adaptability | High (responds to discoveries) | Low (follows script) |
>
> > "ET is not a replacement for existing test-case based approaches, but a complementary testing approach suitable for certain situations"

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 230 — Question 13: Operational Profile Definition

> [!question] Question
> **Question 13: Operational Profile Definition**
>
> What is an operational profile? Give a concrete example with probabilities.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.1 What is an Operational Profile?
>
> > "Set of operations with occurrence probabilities — quantitative characterization of how the system will be used"
>
> **Example (telephone switch):**
>
> | Operation | Rate/hr | Probability |
> |-----------|---------|-------------|
> | Add call | 10,000 | 0.500 |
> | Query call | 4,000 | 0.200 |
> | Edit call | 3,000 | 0.150 |
> | Remove call | 3,000 | 0.150 |
> | **Total** | **20,000** | **1.000** |
>
> #### 3.3 Operational Modes
>
> The same operation may have different probabilities in different contexts :
>
> | Factor | Example Modes |
> |--------|---------------|
> | **Time** | Peak, Prime, Off |
> | **User type** | Customer, Admin, System |
> | **Experience** | Novice, Expert |
> | **Capability** | Full, Degraded, Maintenance |
> | **Criticality** | Normal, Emergency, Shutdown |
>
> {: .highlight }
> > **Exam Tip:** An operational mode is not just "who uses the system" — it includes time, capability, and criticality.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 231 — Question 14: Function vs Operation vs Run

> [!question] Question
> **Question 14: Function vs Operation vs Run**
>
> Explain the difference between a function, an operation, and a run (Musa 1993).

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.2 Operations, Functions, and Runs
>
> | Concept | Perspective | Example |
> |---------|-------------|---------|
> | **Function** | User (requirements) | "Relocate telephone" |
> | **Operation** | Design (development) | "Removal" + "Install" |
> | **Run** | Smallest unit | Single "removal" execution |
>
> #### Purpose
>
> These study notes cover two complementary testing approaches: **exploratory testing** (qualitative, human-driven discovery) and **operational profile-based testing** (quantitative, usage-driven prioritization). The lecture traces ET from its definition through structured heuristics and empirical evidence, then connects it to operational profiles — from Musa's foundational work (1993) through modern developments like operational coverage and Android Cloud Profiles.
>
> **Primary Sources:**
> - Musa 1993, Operational Profiles in Software-Reliability Engineering
> - Whittaker 2009, Exploratory Software Testing
> - Hendrickson 2013, Explore It!
>
> **Key Research Papers:**
> - Itkonen & Mantyla 2007, 2014: ET vs. scripted testing experiments
> - Afzal et al. 2015: Equal-time ET experiment
> - Ghazi et al. 2017: Five levels of exploration
> - Miranda & Bertolino 2016, 2018: Operational coverage
> - Bleier et al. 2025: Android Cloud Profiles

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 232 — Question 15: Operational Modes

> [!question] Question
> **Question 15: Operational Modes**
>
> What is an operational mode? Give three examples.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.3 Operational Modes
>
> The same operation may have different probabilities in different contexts :
>
> | Factor | Example Modes |
> |--------|---------------|
> | **Time** | Peak, Prime, Off |
> | **User type** | Customer, Admin, System |
> | **Experience** | Novice, Expert |
> | **Capability** | Full, Degraded, Maintenance |
> | **Criticality** | Normal, Emergency, Shutdown |
>
> {: .highlight }
> > **Exam Tip:** An operational mode is not just "who uses the system" — it includes time, capability, and criticality.
>
> #### 5.2 Operational Coverage
>
> Traditional coverage treats all code equally. **Operational coverage** weights code by usage :
>
> **Worked example:**
>
> | Method | Branches | Covered | Usage |
> |--------|----------|---------|-------|
> | `login()` | 4 | 3 | 50% |
> | `search()` | 6 | 2 | 30% |
> | `checkout()` | 4 | 4 | 15% |
> | `adminPanel()` | 6 | 0 | 5% |
>
> **Traditional:** (3+2+4+0)/20 = **45%**
> **Operational:** (3/4)×0.50 + (2/6)×0.30 + (4/4)×0.15 + (0/6)×0.05 = **62.5%**
>
> Operational coverage outperforms traditional in **8 of 9 cases** (p<2.2e-16) .
>
> {: .highlight }
> > **Exam Tip:** Know the operational coverage formula (weighted sum) and be able to calculate it.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 233 — Question 16: Profile Probabilities Sum to 1.0

> [!question] Question
> **Question 16: Profile Probabilities Sum to 1.0**
>
> Why must operational profile probabilities sum to 1.0? What happens if the sum is greater or less?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.1 What is an Operational Profile?
>
> > "Set of operations with occurrence probabilities — quantitative characterization of how the system will be used"
>
> **Example (telephone switch):**
>
> | Operation | Rate/hr | Probability |
> |-----------|---------|-------------|
> | Add call | 10,000 | 0.500 |
> | Query call | 4,000 | 0.200 |
> | Edit call | 3,000 | 0.150 |
> | Remove call | 3,000 | 0.150 |
> | **Total** | **20,000** | **1.000** |
>
> #### 4.2 From Rates to Probabilities
>
> $$P(\text{operation}) = \frac{\text{Rate(operation)}}{\text{Sum(all rates)}}$$
>
> **Sources** (in order of quality): Field data → System logs → Surveys → Expert estimate → Best guess.
>
> {: .highlight }
> > **Exam Tip:** Know the probability formula. Be able to calculate probabilities given occurrence rates. Probabilities must sum to 1.0.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 234 — Question 17: 6-Step OP Procedure

> [!question] Question
> **Question 17: 6-Step OP Procedure**
>
> Walk through the 6-step OP procedure (Musa 1999) using a university enrollment system as an example.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.1 The 6-Step Procedure
>
> Musa defines a six-step procedure :
>
> | Step | Action | Key Question |
> |------|--------|-------------|
> | 1 | **Determine operational modes** | What distinct usage patterns exist? |
> | 2 | **Identify initiators** | Who or what triggers operations? |
> | 3 | **Select representation** | Tabular or graphical? |
> | 4 | **Create operations list** | What operations exist in each mode? |
> | 5 | **Determine occurrence rates** | How often does each operation occur? |
> | 6 | **Calculate probabilities** | Normalize: sum = 1.0 |
>
> **Cost:** ~1 staff-month for an average project (10 developers, 100 KLOC) .
>
> **Step 3 — Tabular vs Graphical:**
>
> | Representation | Structure | Use When |
> |----------------|-----------|----------|
> | **Tabular (flat)** | Simple table: operation, rate, probability | Single initiator type; ≤ ~30 operations; straightforward system |
> | **Graphical (tree)** | Hierarchical: initiator types branch into operations | Multiple initiator types; large operation count; complex system; communication to non-technical stakeholders |
>
> > **Rule of thumb (Musa):** Start with tabular. Switch to graphical when you have multiple initiator types whose operations do not overlap, or when the list grows large enough that structure aids comprehension.
>
> {: .highlight }
> > **Exam Tip:** Tabular = one initiator type, small list. Graphical = multiple initiator types or complex hierarchy. The key driver is the number and type of initiators, not personal preference.
>
> #### Purpose
>
> These study notes cover two complementary testing approaches: **exploratory testing** (qualitative, human-driven discovery) and **operational profile-based testing** (quantitative, usage-driven prioritization). The lecture traces ET from its definition through structured heuristics and empirical evidence, then connects it to operational profiles — from Musa's foundational work (1993) through modern developments like operational coverage and Android Cloud Profiles.
>
> **Primary Sources:**
> - Musa 1993, Operational Profiles in Software-Reliability Engineering
> - Whittaker 2009, Exploratory Software Testing
> - Hendrickson 2013, Explore It!
>
> **Key Research Papers:**
> - Itkonen & Mantyla 2007, 2014: ET vs. scripted testing experiments
> - Afzal et al. 2015: Equal-time ET experiment
> - Ghazi et al. 2017: Five levels of exploration
> - Miranda & Bertolino 2016, 2018: Operational coverage
> - Bleier et al. 2025: Android Cloud Profiles

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 235 — Question 18: Tabular vs Graphical Representation

> [!question] Question
> **Question 18: Tabular vs Graphical Representation**
>
> When should you use tabular vs. graphical representation for an operational profile?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.1 What is an Operational Profile?
>
> > "Set of operations with occurrence probabilities — quantitative characterization of how the system will be used"
>
> **Example (telephone switch):**
>
> | Operation | Rate/hr | Probability |
> |-----------|---------|-------------|
> | Add call | 10,000 | 0.500 |
> | Query call | 4,000 | 0.200 |
> | Edit call | 3,000 | 0.150 |
> | Remove call | 3,000 | 0.150 |
> | **Total** | **20,000** | **1.000** |
>
> #### 3.3 Operational Modes
>
> The same operation may have different probabilities in different contexts :
>
> | Factor | Example Modes |
> |--------|---------------|
> | **Time** | Peak, Prime, Off |
> | **User type** | Customer, Admin, System |
> | **Experience** | Novice, Expert |
> | **Capability** | Full, Degraded, Maintenance |
> | **Criticality** | Normal, Emergency, Shutdown |
>
> {: .highlight }
> > **Exam Tip:** An operational mode is not just "who uses the system" — it includes time, capability, and criticality.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 236 — Question 19: OP Calculation (Practical)

> [!question] Question
> **Question 19: OP Calculation (Practical)**
>
> Calculate the operational profile for this system:
>
> | Endpoint | Rate/hr |
> |----------|---------|
> | GET /users | 4,000 |
> | POST /orders | 2,500 |
> | GET /products | 3,000 |
> | PUT /users | 500 |

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.1 What is an Operational Profile?
>
> > "Set of operations with occurrence probabilities — quantitative characterization of how the system will be used"
>
> **Example (telephone switch):**
>
> | Operation | Rate/hr | Probability |
> |-----------|---------|-------------|
> | Add call | 10,000 | 0.500 |
> | Query call | 4,000 | 0.200 |
> | Edit call | 3,000 | 0.150 |
> | Remove call | 3,000 | 0.150 |
> | **Total** | **20,000** | **1.000** |
>
> #### 3.3 Operational Modes
>
> The same operation may have different probabilities in different contexts :
>
> | Factor | Example Modes |
> |--------|---------------|
> | **Time** | Peak, Prime, Off |
> | **User type** | Customer, Admin, System |
> | **Experience** | Novice, Expert |
> | **Capability** | Full, Degraded, Maintenance |
> | **Criticality** | Normal, Emergency, Shutdown |
>
> {: .highlight }
> > **Exam Tip:** An operational mode is not just "who uses the system" — it includes time, capability, and criticality.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 237 — Question 20: AT&T and HP Results

> [!question] Question
> **Question 20: AT&T and HP Results**
>
> What were the results of OP adoption at AT&T and HP?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Why Exploratory Testing?
>
> The empirical evidence across five controlled experiments consistently shows :
>
> | Finding | Evidence |
> |---------|----------|
> | **Matches scripted testing** in defect detection | No significant difference in 4 of 5 experiments |
> | **4-6x more efficient** when total effort counted | ET: 4.58h vs. TCT: 19.47h for equivalent results  |
> | **Fewer false positives** | TCT produces 2x more false defect reports  |
> | **88% industry adoption** | Mainstream practice, not academic theory  |
>
> However, ET consistently achieves **lower systematic coverage** than scripted testing , creating a fundamental trade-off between efficiency and coverage assurance.
>
> #### 1.2 The SRE Context
>
> Operational profile is **Step 2 of 5** in the Software Reliability Engineering process :
>
> 1. Define the product
> 2. **Develop operational profiles**
> 3. Establish reliability objectives
> 4. Plan and execute tests
> 5. Apply test results
>
> {: .highlight }
> > **Exam Tip:** Know where operational profile sits in the SRE 5-step process (Step 2). The profile feeds test planning (Step 4) — without it, test allocation is guesswork.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 238 — Question 21: Operational Coverage

> [!question] Question
> **Question 21: Operational Coverage**
>
> Explain operational coverage with a worked example. How does it differ from traditional coverage?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.2 Operational Coverage
>
> Traditional coverage treats all code equally. **Operational coverage** weights code by usage :
>
> **Worked example:**
>
> | Method | Branches | Covered | Usage |
> |--------|----------|---------|-------|
> | `login()` | 4 | 3 | 50% |
> | `search()` | 6 | 2 | 30% |
> | `checkout()` | 4 | 4 | 15% |
> | `adminPanel()` | 6 | 0 | 5% |
>
> **Traditional:** (3+2+4+0)/20 = **45%**
> **Operational:** (3/4)×0.50 + (2/6)×0.30 + (4/4)×0.15 + (0/6)×0.05 = **62.5%**
>
> Operational coverage outperforms traditional in **8 of 9 cases** (p<2.2e-16) .
>
> {: .highlight }
> > **Exam Tip:** Know the operational coverage formula (weighted sum) and be able to calculate it.
>
> #### 2.8 The Coverage Paradox
>
> ET consistently achieves **lower structural coverage** than scripted testing (Shah 2014 ), yet matches or exceeds it in defect counts. This apparent contradiction has three explanations:
>
> 1. **Coverage measures traversal, not fault-revealing power.** Code coverage records which statements or branches were executed — not whether those executions stressed the system. Scripted tests systematically execute all branches, but many of those executions use "expected" inputs on "expected" paths. The code runs without finding a bug not because the bug isn't there, but because the input didn't trigger it.
>
> 2. **Defects cluster.** Most bugs are concentrated in a small fraction of the codebase — the complex, edge-case-heavy modules. ET testers, guided by heuristics and active reasoning, naturally gravitate toward complexity and anomalies. They reach high-defect areas without covering the full structural map.
>
> 3. **ET exercises paths with higher fault-revealing inputs.** Even when an ET tester and a scripted tester both execute the same branch, the ET tester is more likely to do so with adversarial, boundary-probing, or semantically interesting inputs. Coverage counts the path once; it doesn't distinguish between a routine traversal and a targeted probe.
>
> {: .highlight }
> > **Exam Tip:** Coverage is a **necessary but not sufficient** condition for fault detection. Executing code does not guarantee finding bugs in it — it depends on *how* the code is executed. ET achieves comparable fault detection with lower coverage because it optimises the *quality* of each execution, not the breadth.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 239 — Question 22: Android Cloud Profiles

> [!question] Question
> **Question 22: Android Cloud Profiles**
>
> What are Android Cloud Profiles and why do they matter? What percentage of methods do users exercise?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Android Cloud Profiles
>
> Bleier et al. (2025) discovered that operational profiles can be obtained **for free** from production telemetry :
>
> | Metric | Value |
> |--------|-------|
> | **Availability** | 99.89% of top-1000 Android apps |
> | **Average profile size** | 7.88% of total methods |
> | **Coverage ceiling** | No automated tool exceeds 70% profile coverage |
>
> **Key findings:**
> - Cloud Profiles are **not** strict supersets of developer Baseline Profiles
> - Monkey (random) outperformed model-based tools: 37.45% vs. 32.51%
> - ~30% of user-relevant behavior requires **human exploration**
>
> #### Purpose
>
> These study notes cover two complementary testing approaches: **exploratory testing** (qualitative, human-driven discovery) and **operational profile-based testing** (quantitative, usage-driven prioritization). The lecture traces ET from its definition through structured heuristics and empirical evidence, then connects it to operational profiles — from Musa's foundational work (1993) through modern developments like operational coverage and Android Cloud Profiles.
>
> **Primary Sources:**
> - Musa 1993, Operational Profiles in Software-Reliability Engineering
> - Whittaker 2009, Exploratory Software Testing
> - Hendrickson 2013, Explore It!
>
> **Key Research Papers:**
> - Itkonen & Mantyla 2007, 2014: ET vs. scripted testing experiments
> - Afzal et al. 2015: Equal-time ET experiment
> - Ghazi et al. 2017: Five levels of exploration
> - Miranda & Bertolino 2016, 2018: Operational coverage
> - Bleier et al. 2025: Android Cloud Profiles

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 240 — Question 23: Saturation Handoff

> [!question] Question
> **Question 23: Saturation Handoff**
>
> Why do OP and ET complement each other? Explain the "saturation handoff."

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.4 The OP↔ET Bridge — Two-Phase Testing Strategy
>
> **Phase 1 — Quantitative (OP):**
> 1. Build operational profile from usage data
> 2. Generate tests proportional to usage frequency
> 3. Measure operational coverage
> 4. Continue until saturation (~70%)
>
> **Phase 2 — Qualitative (ET):**
> 1. Use OP priorities to guide charters
> 2. Apply heuristics and tours to high-priority features
> 3. Find usability, edge-case, and interaction defects
> 4. Convert findings to scripted regression tests
>
> {: .highlight }
> > **Exam Tip:** Know the two-phase strategy. OP first (quantitative) → ET second (qualitative) → convert findings to scripted tests. The saturation point (~70%) triggers the switch.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 241 — Question 24: Two-Phase Testing Strategy

> [!question] Question
> **Question 24: Two-Phase Testing Strategy**
>
> Describe the two-phase testing strategy. Why should OP come first?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.4 The OP↔ET Bridge — Two-Phase Testing Strategy
>
> **Phase 1 — Quantitative (OP):**
> 1. Build operational profile from usage data
> 2. Generate tests proportional to usage frequency
> 3. Measure operational coverage
> 4. Continue until saturation (~70%)
>
> **Phase 2 — Qualitative (ET):**
> 1. Use OP priorities to guide charters
> 2. Apply heuristics and tours to high-priority features
> 3. Find usability, edge-case, and interaction defects
> 4. Convert findings to scripted regression tests
>
> {: .highlight }
> > **Exam Tip:** Know the two-phase strategy. OP first (quantitative) → ET second (qualitative) → convert findings to scripted tests. The saturation point (~70%) triggers the switch.
>
> #### 1.1 Testing What Matters
>
> Both ET and operational profiles share a common goal: **test what matters most to users**. They differ in approach:
>
> | Aspect | Scripted Testing | Exploratory Testing | Operational Profile |
> |--------|------------------|---------------------|---------------------|
> | **Approach** | Pre-designed test cases | Simultaneous design & execution | Tests proportional to usage |
> | **Best for** | Regression, coverage metrics | Discovery, edge cases | Reliability prediction |
> | **Repeatability** | High | Lower | High |
> | **Documentation** | Upfront (test plans) | Session reports | Quantitative (rates, probabilities) |
> | **Defect types found** | Known, specified | Unknown, emergent | High-frequency, usage-driven |
>
> **Scripted + Exploratory = Coverage:** Scripted testing systematically exercises known requirements and guards against regression — it finds *specified* defects. Exploratory testing discovers unexpected behaviour that no test plan anticipated — it finds *emergent* defects. Neither alone is sufficient: scripted testing misses what was never specified; exploratory testing misses what requires systematic repetition to verify. Together they cover both dimensions, which is why the combination is standard industry practice .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 242 — Question 25: Startup Testing Decision

> [!question] Question
> **Question 25: Startup Testing Decision**
>
> A startup has limited testing time. Should they build an OP or train testers in ET? Why?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.1 What is Exploratory Testing?
>
> Exploratory testing is **simultaneous learning, test design, and test execution** . The tester observes the system, forms hypotheses, and tests them immediately.
>
> Key characteristics:
> - **Not ad-hoc:** ET uses charters, heuristics, and sessions for structure
> - **Cognitive engagement:** The tester's thinking drives test design in real time
> - **Feedback-driven:** Each test result informs the next test
>
> > "The result of each test leads you to design the next" — Elisabeth Hendrickson
>
> #### ET vs. Ad-Hoc Testing
>
> {: .important }
> > "Don't mix ET with Session Based Testing. The plainest definition of exploratory testing is test design and test execution at the same time. ET is an approach, not another testing technique." — Industry practitioner
>
> | Aspect | Ad-Hoc Testing | Exploratory Testing |
> |--------|----------------|---------------------|
> | Planning | None | Charter, goals, heuristics |
> | Structure | Random, unguided | Structured by techniques and sessions |
> | Documentation | None | Session notes, defect logs |
> | Reproducibility | Low | Medium (via session reports) |
> | Skill dependency | Low | High (domain knowledge, test design intuition) |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 243 — Question 26: Accountability Mechanisms

> [!question] Question
> **Question 26: Accountability Mechanisms**
>
> Compare the accountability mechanisms of SBTM and operational profiles.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Android Cloud Profiles
>
> Bleier et al. (2025) discovered that operational profiles can be obtained **for free** from production telemetry :
>
> | Metric | Value |
> |--------|-------|
> | **Availability** | 99.89% of top-1000 Android apps |
> | **Average profile size** | 7.88% of total methods |
> | **Coverage ceiling** | No automated tool exceeds 70% profile coverage |
>
> **Key findings:**
> - Cloud Profiles are **not** strict supersets of developer Baseline Profiles
> - Monkey (random) outperformed model-based tools: 37.45% vs. 32.51%
> - ~30% of user-relevant behavior requires **human exploration**
>
> #### 2.4 Session-Based Test Management (SBTM)
>
> **The four pillars** :
>
> | Pillar | Details |
> |--------|---------|
> | **Charter** | What to explore, how, and what problems to seek |
> | **Time Box** | 60-120 minutes |
> | **Reviewable Result** | Bug reports, coverage notes, issues |
> | **Debriefing** | Post-session review with manager/team |
>
> **Debriefing questions:** How did you spend your time? What did you find? Did you need special knowledge? Is there more to do?
>
> {: .highlight }
> > **Exam Tip:** Know the four SBTM pillars (Charter, Time Box, Reviewable Result, Debriefing) and the debriefing questions.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 244 — Question 27: Banking App Strategy (Practical)

> [!question] Question
> **Question 27: Banking App Strategy (Practical)**
>
> Design a testing strategy for a banking mobile app using both OP and ET. Include specific charters and tours.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.4 The OP↔ET Bridge — Two-Phase Testing Strategy
>
> **Phase 1 — Quantitative (OP):**
> 1. Build operational profile from usage data
> 2. Generate tests proportional to usage frequency
> 3. Measure operational coverage
> 4. Continue until saturation (~70%)
>
> **Phase 2 — Qualitative (ET):**
> 1. Use OP priorities to guide charters
> 2. Apply heuristics and tours to high-priority features
> 3. Find usability, edge-case, and interaction defects
> 4. Convert findings to scripted regression tests
>
> {: .highlight }
> > **Exam Tip:** Know the two-phase strategy. OP first (quantitative) → ET second (qualitative) → convert findings to scripted tests. The saturation point (~70%) triggers the switch.
>
> #### 1.1 Testing What Matters
>
> Both ET and operational profiles share a common goal: **test what matters most to users**. They differ in approach:
>
> | Aspect | Scripted Testing | Exploratory Testing | Operational Profile |
> |--------|------------------|---------------------|---------------------|
> | **Approach** | Pre-designed test cases | Simultaneous design & execution | Tests proportional to usage |
> | **Best for** | Regression, coverage metrics | Discovery, edge cases | Reliability prediction |
> | **Repeatability** | High | Lower | High |
> | **Documentation** | Upfront (test plans) | Session reports | Quantitative (rates, probabilities) |
> | **Defect types found** | Known, specified | Unknown, emergent | High-frequency, usage-driven |
>
> **Scripted + Exploratory = Coverage:** Scripted testing systematically exercises known requirements and guards against regression — it finds *specified* defects. Exploratory testing discovers unexpected behaviour that no test plan anticipated — it finds *emergent* defects. Neither alone is sufficient: scripted testing misses what was never specified; exploratory testing misses what requires systematic repetition to verify. Together they cover both dimensions, which is why the combination is standard industry practice .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 245 — Question 28: Operational vs Traditional Coverage

> [!question] Question
> **Question 28: Operational vs Traditional Coverage**
>
> Why does operational coverage give a more useful signal than traditional coverage?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.2 Operational Coverage
>
> Traditional coverage treats all code equally. **Operational coverage** weights code by usage :
>
> **Worked example:**
>
> | Method | Branches | Covered | Usage |
> |--------|----------|---------|-------|
> | `login()` | 4 | 3 | 50% |
> | `search()` | 6 | 2 | 30% |
> | `checkout()` | 4 | 4 | 15% |
> | `adminPanel()` | 6 | 0 | 5% |
>
> **Traditional:** (3+2+4+0)/20 = **45%**
> **Operational:** (3/4)×0.50 + (2/6)×0.30 + (4/4)×0.15 + (0/6)×0.05 = **62.5%**
>
> Operational coverage outperforms traditional in **8 of 9 cases** (p<2.2e-16) .
>
> {: .highlight }
> > **Exam Tip:** Know the operational coverage formula (weighted sum) and be able to calculate it.
>
> #### 2.8 The Coverage Paradox
>
> ET consistently achieves **lower structural coverage** than scripted testing (Shah 2014 ), yet matches or exceeds it in defect counts. This apparent contradiction has three explanations:
>
> 1. **Coverage measures traversal, not fault-revealing power.** Code coverage records which statements or branches were executed — not whether those executions stressed the system. Scripted tests systematically execute all branches, but many of those executions use "expected" inputs on "expected" paths. The code runs without finding a bug not because the bug isn't there, but because the input didn't trigger it.
>
> 2. **Defects cluster.** Most bugs are concentrated in a small fraction of the codebase — the complex, edge-case-heavy modules. ET testers, guided by heuristics and active reasoning, naturally gravitate toward complexity and anomalies. They reach high-defect areas without covering the full structural map.
>
> 3. **ET exercises paths with higher fault-revealing inputs.** Even when an ET tester and a scripted tester both execute the same branch, the ET tester is more likely to do so with adversarial, boundary-probing, or semantically interesting inputs. Coverage counts the path once; it doesn't distinguish between a routine traversal and a targeted probe.
>
> {: .highlight }
> > **Exam Tip:** Coverage is a **necessary but not sufficient** condition for fault detection. Executing code does not guarantee finding bugs in it — it depends on *how* the code is executed. ET achieves comparable fault detection with lower coverage because it optimises the *quality* of each execution, not the breadth.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 246 — Question 29: Cloud Profiles Validation

> [!question] Question
> **Question 29: Cloud Profiles Validation**
>
> Explain how Android Cloud Profiles validate the claim "you cannot assume how users will use your software."

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Android Cloud Profiles
>
> Bleier et al. (2025) discovered that operational profiles can be obtained **for free** from production telemetry :
>
> | Metric | Value |
> |--------|-------|
> | **Availability** | 99.89% of top-1000 Android apps |
> | **Average profile size** | 7.88% of total methods |
> | **Coverage ceiling** | No automated tool exceeds 70% profile coverage |
>
> **Key findings:**
> - Cloud Profiles are **not** strict supersets of developer Baseline Profiles
> - Monkey (random) outperformed model-based tools: 37.45% vs. 32.51%
> - ~30% of user-relevant behavior requires **human exploration**
>
> #### Purpose
>
> These study notes cover two complementary testing approaches: **exploratory testing** (qualitative, human-driven discovery) and **operational profile-based testing** (quantitative, usage-driven prioritization). The lecture traces ET from its definition through structured heuristics and empirical evidence, then connects it to operational profiles — from Musa's foundational work (1993) through modern developments like operational coverage and Android Cloud Profiles.
>
> **Primary Sources:**
> - Musa 1993, Operational Profiles in Software-Reliability Engineering
> - Whittaker 2009, Exploratory Software Testing
> - Hendrickson 2013, Explore It!
>
> **Key Research Papers:**
> - Itkonen & Mantyla 2007, 2014: ET vs. scripted testing experiments
> - Afzal et al. 2015: Equal-time ET experiment
> - Ghazi et al. 2017: Five levels of exploration
> - Miranda & Bertolino 2016, 2018: Operational coverage
> - Bleier et al. 2025: Android Cloud Profiles

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

### Card 247 — Question 30: Lecture Summary

> [!question] Question
> **Question 30: Lecture Summary**
>
> Explain the entire L07 lecture in 5 minutes. Cover ET, OP, and how they bridge together.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.4 The OP↔ET Bridge — Two-Phase Testing Strategy
>
> **Phase 1 — Quantitative (OP):**
> 1. Build operational profile from usage data
> 2. Generate tests proportional to usage frequency
> 3. Measure operational coverage
> 4. Continue until saturation (~70%)
>
> **Phase 2 — Qualitative (ET):**
> 1. Use OP priorities to guide charters
> 2. Apply heuristics and tours to high-priority features
> 3. Find usability, edge-case, and interaction defects
> 4. Convert findings to scripted regression tests
>
> {: .highlight }
> > **Exam Tip:** Know the two-phase strategy. OP first (quantitative) → ET second (qualitative) → convert findings to scripted tests. The saturation point (~70%) triggers the switch.
>
> #### Part 6: Summary — Key Takeaways
>
> | # | Takeaway |
> |---|----------|
> | 1 | **Exploratory testing** = learn, design, execute simultaneously — **4-6x more efficient** than scripted |
> | 2 | **Session-based management** makes ET auditable: charter + time box + debriefing |
> | 3 | **Five levels of exploration** from freestyle to fully scripted — choose per context |
> | 4 | **Operational profile** = operations + occurrence probabilities — quantifies usage |
> | 5 | **6-step procedure:** Modes → Initiators → Representation → List → Rates → Probabilities |
> | 6 | **Industrial evidence:** AT&T 10x improvement, HP 50% cost savings |
> | 7 | **Operational coverage** weights code by usage (62.5% vs. 45% in worked example) |
> | 8 | **Two-phase strategy:** When OP saturates (~70%) → switch to ET for the remaining 30% |
>
> **Key formulas:**
>
> $$P(\text{op}) = \frac{\text{Rate(op)}}{\text{Total Rate}}$$
>
> $$\text{OpCov} = \sum_i \frac{\text{covered}_i}{\text{total}_i} \times \text{usage}_i$$

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/verif/exploratory/RQ_L07_Exploratory_OP.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/verif/exploratory/RQ_L07_Exploratory_OP.md)

## Maintainability & DSM (32)

### Card 248 — Q1

> [!question] Question
> If most maintenance effort goes to perfective changes (enhancements) rather than bug fixes, what does this imply about how organizations should allocate their maintenance budgets?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.1 Maintenance Dominates Lifecycle Cost
>
> **What is it?**
> Software maintenance consumes 60-80% of total lifecycle cost . This includes corrective (bug fixes ~20%), adaptive (environment changes ~18%), perfective (enhancements ~25%), and preventive (refactoring ~7%) maintenance.
>
> **Key Points:**
>
> | Maintenance Type | Purpose | Share |
> |-----------------|---------|-------|
> | Corrective | Fix bugs and defects | ~20% |
> | Adaptive | Adapt to new environments (OS, hardware, APIs) | ~18% |
> | Perfective | Add features, improve performance | ~25% |
> | Preventive | Refactor, improve structure | ~7% |
>
> Most effort goes to perfective changes (enhancements), not bug fixing. Systems with above-average maintainability resolve issues twice as fast .
>
> …
>
> #### The Maintenance Iceberg
>
> Most software cost is invisible at release time. The development phase — requirements through initial deployment — accounts for only a fraction of total lifecycle expenditure. The rest is maintenance: corrective, adaptive, perfective, and preventive.
>
> | Statistic | Source |
> |-----------|--------|
> | ~70% of lifecycle effort goes to maintenance, ~30% to initial development |  |
> | 70--80% of total lifecycle cost is in operations and support (O&S) |  |
> | 80--85% of life-cycle cost is committed during requirements and design |  |
> | ROI of "Design for Maintainability" can reach 1000% vs doing nothing |  |
>
> ![Software lifecycle cost distribution — development vs maintenance phases](chart-maintenance-cost.svg)
>
> The implication is stark: **the cheapest time to invest in maintainability is before code is written**, because design decisions lock in 80--85% of future maintenance cost.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 249 — Q2

> [!question] Question
> Lehman's Law I says software must adapt, and Law II says adaptation increases complexity. How does this tension manifest in a real project, and what strategies break the cycle?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.2 Lehman's Laws of Software Evolution
>
> **What are they?**
> Lehman  formulated laws governing how real-world software evolves over time. The two most fundamental are:
>
> **Law I — Continuing Change (1974):**
> > A program that is used in a real-world environment must be continually adapted, or it becomes progressively less satisfactory
>
> **Law II — Increasing Complexity (1974):**
> > As a program evolves, its complexity increases unless work is done to maintain or reduce it
>
> These laws create an inescapable tension: you *must* change the software (Law I), but changing it makes it worse (Law II). Technical debt is not a modern invention — it is a fundamental property of software evolution.
>
> The 1996 revision  extended the set to eight laws, adding Law VII (Declining Quality — perceived quality declines unless rigorously maintained) and Law VIII (Feedback System — evolution is a multi-loop feedback process).
>
> ```mermaid
> graph TD
>     A["Law I: Continuing Change"] -->|"software must adapt"| B["Changes Required"]
>     C["Law II: Increasing Complexity"] -->|"changes add entropy"| D["Complexity Grows"]
>     B --> E["Modification"]
>     E --> D
>     D -->|"without deliberate effort"| F["Technical Debt Accumulates"]
>     F -->|"eventually"| G["System Becomes Unmaintainable"]
>     E -->|"with refactoring"| H["Complexity Managed"]
>     H -->|"enables"| B
>
>     style A fill:#e8f5e9
>     style C fill:#ffcdd2
>     style F fill:#fff3cd
>     style G fill:#d32f2f,color:#fff
>     style H fill:#019546,color:#fff
> ```
>
> #### Lehman's Laws of Software Evolution
>
> Lehman's empirical Laws I and II formalize the same pressures at the system level :
>
> | Law | Name | Statement |
> |-----|------|-----------|
> | I | Continuing Change | A system must be continually adapted, or it becomes progressively less satisfactory |
> | II | Increasing Complexity | As a system evolves, its complexity increases unless work is done to maintain or reduce it |
>
> Law I corresponds to Parnas's "Lack of Movement": stop adapting and the system loses value. Law II corresponds to "Ignorant Surgery": every modification that does not actively reduce complexity adds to it.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 250 — Q3

> [!question] Question
> Parnas identifies "Lack of Movement" and "Ignorant Surgery" as two causes of software aging. Can a system suffer from both simultaneously? Give a scenario where this happens.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Parnas's Two Causes of Aging
>
> Parnas identifies two forces that cause software to age :
>
> 1. **Lack of Movement** — failure to update the software to keep pace with a changing environment. The software becomes obsolete, even though nothing in it has changed.
> 2. **Ignorant Surgery** — changes made by people who do not understand the original design. Each such change degrades the structure, making the next change harder and more error-prone.
>
> > "Programs, like people, get old. We can't prevent aging, but we can understand its causes, take steps to limit its effects, temporarily reverse some of the damage it has caused, and prepare for the day when the software is no longer viable."
> > — D.L. Parnas (1994)
>
> #### 1.3 Parnas's Software Aging
>
> **What is it?**
> Parnas  identified two mechanisms by which software degrades:
>
> 1. **Lack of Movement** — failure to adapt to changing environment leads to obsolescence (the system falls behind its context)
> 2. **Ignorant Surgery** — changes by developers who do not understand the original design degrade internal structure
>
> ```mermaid
> graph LR
>     subgraph Causes
>         A["Lack of Movement<br>(failure to adapt)"]
>         B["Ignorant Surgery<br>(uninformed changes)"]
>     end
>     A -->|"obsolescence"| C["Aged Software"]
>     B -->|"structural decay"| C
>     C --> D["Costly Maintenance"]
>     C --> E["Eventual Rewrite"]
>
>     subgraph Prescriptions
>         F["Design for Change<br>(information hiding)"]
>         G["Keep Records<br>(documentation)"]
>         H["Seek Second Opinions<br>(reviews)"]
>     end
>
>     style A fill:#ffcdd2
>     style B fill:#ffcdd2
>     style C fill:#d32f2f,color:#fff
>     style F fill:#e8f5e9
>     style G fill:#e8f5e9
>     style H fill:#e8f5e9
> ```
>
> **Parnas's prescriptions:**
> - **Design for change:** Use information hiding so implementation details are isolated behind stable interfaces
> - **Keep records:** Maintain documentation that captures design rationale, not just code comments
> - **Seek second opinions:** Code reviews and architectural reviews catch "ignorant surgery" before it damages the system
>
> **Concrete Example:**
> Consider a payment processing system. Lack of Movement: not updating to support PSD2/SCA regulations makes the system non-compliant in the EU. Ignorant Surgery: a developer unfamiliar with the authorization flow adds a shortcut that bypasses the fraud check — the system works but is now structurally compromised.
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 251 — Q4

> [!question] Question
> A startup says "we'll fix the architecture later — right now we need to ship features." Using Lehman's Laws and the compounding effect of technical debt, argue for or against this strategy.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.2 Lehman's Laws of Software Evolution
>
> **What are they?**
> Lehman  formulated laws governing how real-world software evolves over time. The two most fundamental are:
>
> **Law I — Continuing Change (1974):**
> > A program that is used in a real-world environment must be continually adapted, or it becomes progressively less satisfactory
>
> **Law II — Increasing Complexity (1974):**
> > As a program evolves, its complexity increases unless work is done to maintain or reduce it
>
> These laws create an inescapable tension: you *must* change the software (Law I), but changing it makes it worse (Law II). Technical debt is not a modern invention — it is a fundamental property of software evolution.
>
> The 1996 revision  extended the set to eight laws, adding Law VII (Declining Quality — perceived quality declines unless rigorously maintained) and Law VIII (Feedback System — evolution is a multi-loop feedback process).
>
> ```mermaid
> graph TD
>     A["Law I: Continuing Change"] -->|"software must adapt"| B["Changes Required"]
>     C["Law II: Increasing Complexity"] -->|"changes add entropy"| D["Complexity Grows"]
>     B --> E["Modification"]
>     E --> D
>     D -->|"without deliberate effort"| F["Technical Debt Accumulates"]
>     F -->|"eventually"| G["System Becomes Unmaintainable"]
>     E -->|"with refactoring"| H["Complexity Managed"]
>     H -->|"enables"| B
>
>     style A fill:#e8f5e9
>     style C fill:#ffcdd2
>     style F fill:#fff3cd
>     style G fill:#d32f2f,color:#fff
>     style H fill:#019546,color:#fff
> ```
>
> #### Lehman's Laws of Software Evolution
>
> Lehman's empirical Laws I and II formalize the same pressures at the system level :
>
> | Law | Name | Statement |
> |-----|------|-----------|
> | I | Continuing Change | A system must be continually adapted, or it becomes progressively less satisfactory |
> | II | Increasing Complexity | As a system evolves, its complexity increases unless work is done to maintain or reduce it |
>
> Law I corresponds to Parnas's "Lack of Movement": stop adapting and the system loses value. Law II corresponds to "Ignorant Surgery": every modification that does not actively reduce complexity adds to it.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 252 — Q5

> [!question] Question
> Why does Parnas prescribe "seek second opinions" (code reviews) as a remedy for software aging? How does this connect to the concept of Ignorant Surgery?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.3 Parnas's Software Aging
>
> **What is it?**
> Parnas  identified two mechanisms by which software degrades:
>
> 1. **Lack of Movement** — failure to adapt to changing environment leads to obsolescence (the system falls behind its context)
> 2. **Ignorant Surgery** — changes by developers who do not understand the original design degrade internal structure
>
> ```mermaid
> graph LR
>     subgraph Causes
>         A["Lack of Movement<br>(failure to adapt)"]
>         B["Ignorant Surgery<br>(uninformed changes)"]
>     end
>     A -->|"obsolescence"| C["Aged Software"]
>     B -->|"structural decay"| C
>     C --> D["Costly Maintenance"]
>     C --> E["Eventual Rewrite"]
>
>     subgraph Prescriptions
>         F["Design for Change<br>(information hiding)"]
>         G["Keep Records<br>(documentation)"]
>         H["Seek Second Opinions<br>(reviews)"]
>     end
>
>     style A fill:#ffcdd2
>     style B fill:#ffcdd2
>     style C fill:#d32f2f,color:#fff
>     style F fill:#e8f5e9
>     style G fill:#e8f5e9
>     style H fill:#e8f5e9
> ```
>
> **Parnas's prescriptions:**
> - **Design for change:** Use information hiding so implementation details are isolated behind stable interfaces
> - **Keep records:** Maintain documentation that captures design rationale, not just code comments
> - **Seek second opinions:** Code reviews and architectural reviews catch "ignorant surgery" before it damages the system
>
> **Concrete Example:**
> Consider a payment processing system. Lack of Movement: not updating to support PSD2/SCA regulations makes the system non-compliant in the EU. Ignorant Surgery: a developer unfamiliar with the authorization flow adds a shortcut that bypasses the fraud check — the system works but is now structurally compromised.
>
> …
>
> #### Parnas's Two Causes of Aging
>
> Parnas identifies two forces that cause software to age :
>
> 1. **Lack of Movement** — failure to update the software to keep pace with a changing environment. The software becomes obsolete, even though nothing in it has changed.
> 2. **Ignorant Surgery** — changes made by people who do not understand the original design. Each such change degrades the structure, making the next change harder and more error-prone.
>
> > "Programs, like people, get old. We can't prevent aging, but we can understand its causes, take steps to limit its effects, temporarily reverse some of the damage it has caused, and prepare for the day when the software is no longer viable."
> > — D.L. Parnas (1994)

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 253 — Q6

> [!question] Question
> The lecture states that 80-85% of lifecycle cost is committed during requirements and design. If this is true, what are the implications for when maintainability decisions should be made?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.1 Maintenance Dominates Lifecycle Cost
>
> **What is it?**
> Software maintenance consumes 60-80% of total lifecycle cost . This includes corrective (bug fixes ~20%), adaptive (environment changes ~18%), perfective (enhancements ~25%), and preventive (refactoring ~7%) maintenance.
>
> **Key Points:**
>
> | Maintenance Type | Purpose | Share |
> |-----------------|---------|-------|
> | Corrective | Fix bugs and defects | ~20% |
> | Adaptive | Adapt to new environments (OS, hardware, APIs) | ~18% |
> | Perfective | Add features, improve performance | ~25% |
> | Preventive | Refactor, improve structure | ~7% |
>
> Most effort goes to perfective changes (enhancements), not bug fixing. Systems with above-average maintainability resolve issues twice as fast .
>
> …
>
> #### The Maintenance Iceberg
>
> Most software cost is invisible at release time. The development phase — requirements through initial deployment — accounts for only a fraction of total lifecycle expenditure. The rest is maintenance: corrective, adaptive, perfective, and preventive.
>
> | Statistic | Source |
> |-----------|--------|
> | ~70% of lifecycle effort goes to maintenance, ~30% to initial development |  |
> | 70--80% of total lifecycle cost is in operations and support (O&S) |  |
> | 80--85% of life-cycle cost is committed during requirements and design |  |
> | ROI of "Design for Maintainability" can reach 1000% vs doing nothing |  |
>
> ![Software lifecycle cost distribution — development vs maintenance phases](chart-maintenance-cost.svg)
>
> The implication is stark: **the cheapest time to invest in maintainability is before code is written**, because design decisions lock in 80--85% of future maintenance cost.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 254 — Q7

> [!question] Question
> The SIG model uses quality profiles (risk distributions) while the Maintainability Index uses averages. Construct a scenario where MI gives a misleading "good" score but SIG correctly identifies a problem.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.1 SIG Model: 8 Code Properties
>
> **What is it?**
> The Software Improvement Group (SIG) model   measures maintainability through eight code properties, benchmarked against hundreds of industry systems:
>
> | Property | What It Measures | Threshold |
> |----------|-----------------|-----------|
> | Volume | Overall source code size | <66 kLOC per component |
> | Duplication | Identical code fragments | <5% duplicated |
> | Unit complexity | Cyclomatic complexity per method | CC < 15 |
> | Unit size | Lines per method/function | <60 LOC |
> | Unit interfacing | Number of parameters | <5 parameters |
> | Module coupling | Incoming dependencies | Fan-in thresholds |
> | Component balance | Size distribution | Gini coefficient |
> | Component independence | Code without external deps | >80% independent |
>
> **How SIG maps to ISO 25010:**
> Each property affects one or more ISO sub-characteristics. For example, Module Coupling affects both Analyzability and Modifiability, while Component Independence primarily affects Modularity.
>
> **Star rating calibration:**
> SIG benchmarks systems on a 1-5 star scale using a 5%/30%/30%/30%/5% distribution. A 5-star system is in the top 5% of the benchmark — this is deliberately exclusive.
>
> …
>
> #### 3.2 Maintainability Index: Problems with a Single Number
>
> **What is it?**
> The Maintainability Index (MI) is a composite metric:
>
> $$MI = 171 - 5.2 \cdot \ln(V) - 0.23 \cdot G - 16.2 \cdot \ln(LOC)$$
>
> Where $V$ = Halstead Volume, $G$ = Cyclomatic Complexity, $LOC$ = Lines of Code.
>
> **Why it fails:**
>
> | Problem | Explanation |
> |---------|-------------|
> | Averaging hides skewness | 1 terrible module + 99 good ones = "good" MI |
> | Structure invisible | Module boundaries and dependencies are not captured |
> | Same MI, different designs | Compact spaghetti code can score the same as well-structured code |
> | Outdated components | Halstead Volume is rarely used in modern practice |
>
> **Concrete Example:**
> System A: 100 methods, all with CC=10 → MI = 72 ("moderate")
> System B: 95 methods with CC=3, 5 methods with CC=133 → same average, same MI = 72
> System B is far worse — those 5 methods are unmaintainable hotspots — but MI cannot distinguish the two.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 255 — Q8

> [!question] Question
> Why does the SIG star rating use a 5%/30%/30%/30%/5% calibration rather than equal quintiles? What would change if they used 20%/20%/20%/20%/20%?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Star Rating Calibration
>
> Properties are rated on a 1-to-5 star scale, calibrated against SIG's benchmark repository so that the distribution reflects the full range of quality achieved by real-world systems :
>
> | Stars | Benchmark Percentile |
> |-------|---------------------|
> | 5 | Top 5% of systems |
> | 4 | Next 30% |
> | 3 | Next 30% |
> | 2 | Next 30% |
> | 1 | Bottom 5% |
>
> ![SIG star rating distribution calibrated against industry benchmark](chart-sig-stars.svg)
>
> **Certification threshold:** overall maintainability rating of at least 3 stars, with each sub-characteristic scoring at least 2 stars .
>
> #### 3.1 SIG Model: 8 Code Properties
>
> **What is it?**
> The Software Improvement Group (SIG) model   measures maintainability through eight code properties, benchmarked against hundreds of industry systems:
>
> | Property | What It Measures | Threshold |
> |----------|-----------------|-----------|
> | Volume | Overall source code size | <66 kLOC per component |
> | Duplication | Identical code fragments | <5% duplicated |
> | Unit complexity | Cyclomatic complexity per method | CC < 15 |
> | Unit size | Lines per method/function | <60 LOC |
> | Unit interfacing | Number of parameters | <5 parameters |
> | Module coupling | Incoming dependencies | Fan-in thresholds |
> | Component balance | Size distribution | Gini coefficient |
> | Component independence | Code without external deps | >80% independent |
>
> **How SIG maps to ISO 25010:**
> Each property affects one or more ISO sub-characteristics. For example, Module Coupling affects both Analyzability and Modifiability, while Component Independence primarily affects Modularity.
>
> **Star rating calibration:**
> SIG benchmarks systems on a 1-5 star scale using a 5%/30%/30%/30%/5% distribution. A 5-star system is in the top 5% of the benchmark — this is deliberately exclusive.
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 256 — Q9

> [!question] Question
> A developer argues that Cognitive Complexity is unnecessary because "Cyclomatic Complexity already measures code complexity." Using the switch statement and nested-if examples, explain why CC and CogC measure fundamentally different things.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.3 Cognitive Complexity
>
> **What is it?**
> Cognitive Complexity  measures how hard code is for a human to understand, designed to match developer intuition better than Cyclomatic Complexity.
>
> **Three rules:**
> 1. **Ignore readable shorthand** — `switch` statements, null-coalescing operators
> 2. **Increment for breaks in linear flow** — `if`, `for`, `while`, `catch`, `goto`
> 3. **Extra increment per nesting level** — nested structures are harder to understand
>
> **Key differences from Cyclomatic Complexity:**
>
> | Code Pattern | CC | CogC | Why |
> |-------------|:--:|:----:|-----|
> | `switch` with 10 cases | +10 | +1 | Switch is readable shorthand |
> | Nested `if` inside loop | +1 | +2 | Nesting increases cognitive load |
> | `if-else` chain | +N | +1 | Linear if-else is easy to scan |
>
> **Validation:** 77% developer acceptance rate across 22 open-source projects on SonarCloud — developers agreed with CogC assessments more often than CC assessments.
>
> #### Cognitive Complexity
>
> Cyclomatic Complexity (CC) counts the number of linearly independent paths through a method -- useful for estimating test effort, but widely regarded as unsatisfactory for measuring how difficult code is to *understand*. A switch statement with 10 cases receives the same CC score as deeply nested control flow, despite the vast difference in cognitive burden .
>
> **Cognitive Complexity** addresses this gap with three intuitive rules:
>
> 1. **Ignore** readable shorthand structures (e.g., null-coalescing operators).
> 2. **Increment** for every break in linear flow (if, for, catch, goto, etc.).
> 3. **Add a nesting penalty** for control flow nested inside other control flow.
>
> | Aspect | Cyclomatic Complexity | Cognitive Complexity |
> |--------|----------------------|---------------------|
> | **Counts** | Independent execution paths | Breaks in linear flow + nesting depth |
> | **Switch** | +1 per case | +1 for the entire switch |
> | **Nested if inside loop** | +1 | +2 (flow break + nesting) |
> | **Design goal** | Testability (minimum test cases) | Human comprehension difficulty |
>
> A developer acceptance survey across 22 open-source projects on SonarCloud showed a 77% acceptance rate, with developers actively fixing high Cognitive Complexity code .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 257 — Q10

> [!question] Question
> The Maintainability Index formula includes Halstead Volume, which is rarely used in modern practice. If you were designing a replacement for MI, which metrics would you include and why?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.2 Maintainability Index: Problems with a Single Number
>
> **What is it?**
> The Maintainability Index (MI) is a composite metric:
>
> $$MI = 171 - 5.2 \cdot \ln(V) - 0.23 \cdot G - 16.2 \cdot \ln(LOC)$$
>
> Where $V$ = Halstead Volume, $G$ = Cyclomatic Complexity, $LOC$ = Lines of Code.
>
> **Why it fails:**
>
> | Problem | Explanation |
> |---------|-------------|
> | Averaging hides skewness | 1 terrible module + 99 good ones = "good" MI |
> | Structure invisible | Module boundaries and dependencies are not captured |
> | Same MI, different designs | Compact spaghetti code can score the same as well-structured code |
> | Outdated components | Halstead Volume is rarely used in modern practice |
>
> **Concrete Example:**
> System A: 100 methods, all with CC=10 → MI = 72 ("moderate")
> System B: 95 methods with CC=3, 5 methods with CC=133 → same average, same MI = 72
> System B is far worse — those 5 methods are unmaintainable hotspots — but MI cannot distinguish the two.
>
> #### The Maintainability Index (MI)
>
> The Maintainability Index is one of the earliest composite metrics, combining Halstead volume, cyclomatic complexity, and lines of code into a single number :
>
> $$MI = 171 - 5.2 \cdot \ln(\text{aveV}) - 0.23 \cdot \text{aveG} - 16.2 \cdot \ln(\text{aveSTAT})$$
>
> where $\text{aveV}$ = average Halstead Volume per module, $\text{aveG}$ = average Cyclomatic Complexity per module, and $\text{aveSTAT}$ = average lines of code per module.
>
> | MI Range | Interpretation |
> |----------|---------------|
> | > 85 | Easily maintainable |
> | 65 -- 85 | Moderately maintainable |
> | < 65 | Difficult to maintain |
>
> **Limitations.** The MI uses averages across all modules, which masks local hotspots: a few highly complex modules can be hidden by many simple ones. It was designed for procedural code and does not account for object-oriented features such as inheritance and coupling. Empirical evidence shows that MI is significantly influenced by software size (a confounding effect), and it correlates only moderately with technical debt at the class level (Spearman rho approximately -0.6) .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 258 — Q11

> [!question] Question
> The lecture contrasts code metrics (symptoms of local problems) with structural metrics (root causes of systemic problems). Can you have good code metrics but poor structural metrics? Give an example.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.4 Structure vs. Code Metrics
>
> **Why code metrics are not enough:**
>
> | Code Metrics Show | Structural Analysis Shows |
> |-------------------|--------------------------|
> | This method is complex (CC=47) | This change affects 17% of the system |
> | This file is too large (800 LOC) | These 12 modules form a hidden cluster |
> | This pattern is duplicated (23%) | This layering constraint is violated |
> | *Symptoms of local problems* | *Root causes of systemic problems* |
>
> Code metrics and structural metrics are **complementary**, not competing. You need both for a complete maintainability assessment. The tool for structural analysis is the **Design Structure Matrix (DSM)**.
>
> {: .exam-tip }
> > **Exam Tip:** When comparing measurement approaches, use this framework: SIG measures *code-level* maintainability, DSM measures *structural* maintainability, and Propagation Cost quantifies *change impact*. No single metric captures everything.
>
> #### 3.2 Maintainability Index: Problems with a Single Number
>
> **What is it?**
> The Maintainability Index (MI) is a composite metric:
>
> $$MI = 171 - 5.2 \cdot \ln(V) - 0.23 \cdot G - 16.2 \cdot \ln(LOC)$$
>
> Where $V$ = Halstead Volume, $G$ = Cyclomatic Complexity, $LOC$ = Lines of Code.
>
> **Why it fails:**
>
> | Problem | Explanation |
> |---------|-------------|
> | Averaging hides skewness | 1 terrible module + 99 good ones = "good" MI |
> | Structure invisible | Module boundaries and dependencies are not captured |
> | Same MI, different designs | Compact spaghetti code can score the same as well-structured code |
> | Outdated components | Halstead Volume is rarely used in modern practice |
>
> **Concrete Example:**
> System A: 100 methods, all with CC=10 → MI = 72 ("moderate")
> System B: 95 methods with CC=3, 5 methods with CC=133 → same average, same MI = 72
> System B is far worse — those 5 methods are unmaintainable hotspots — but MI cannot distinguish the two.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 259 — Q12

> [!question] Question
> A system scores 4 stars on all SIG properties except Module Coupling (2 stars). What does this tell you about the system, and what would you investigate next?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.1 SIG Model: 8 Code Properties
>
> **What is it?**
> The Software Improvement Group (SIG) model   measures maintainability through eight code properties, benchmarked against hundreds of industry systems:
>
> | Property | What It Measures | Threshold |
> |----------|-----------------|-----------|
> | Volume | Overall source code size | <66 kLOC per component |
> | Duplication | Identical code fragments | <5% duplicated |
> | Unit complexity | Cyclomatic complexity per method | CC < 15 |
> | Unit size | Lines per method/function | <60 LOC |
> | Unit interfacing | Number of parameters | <5 parameters |
> | Module coupling | Incoming dependencies | Fan-in thresholds |
> | Component balance | Size distribution | Gini coefficient |
> | Component independence | Code without external deps | >80% independent |
>
> **How SIG maps to ISO 25010:**
> Each property affects one or more ISO sub-characteristics. For example, Module Coupling affects both Analyzability and Modifiability, while Component Independence primarily affects Modularity.
>
> **Star rating calibration:**
> SIG benchmarks systems on a 1-5 star scale using a 5%/30%/30%/30%/5% distribution. A 5-star system is in the top 5% of the benchmark — this is deliberately exclusive.
>
> …
>
> #### 4.3 Coupling and Cohesion
>
> **What are they?**
>
> **Coupling** (between modules) — the degree of interdependence between modules.
> - Goal: **Minimize** coupling
> - Measured by: fan-in, fan-out, dependency density $= \frac{\text{deps}}{N(N-1)}$
> - Low coupling = modules can be changed independently
>
> **Cohesion** (within modules) — the degree to which elements within a module belong together.
> - Goal: **Maximize** cohesion
> - Measured by: LCOM (Lack of Cohesion of Methods), conceptual cohesion
> - High cohesion = module has a single, focused purpose
>
> ```mermaid
> graph TB
>     subgraph "Good: Low Coupling, High Cohesion"
>         direction TB
>         A1["Module A<br>━━━━━━<br>func1()<br>func2()<br>func3()"]
>         B1["Module B<br>━━━━━━<br>func4()<br>func5()<br>func6()"]
>         A1 -.->|"1 dependency"| B1
>     end
>     subgraph "Bad: High Coupling, Low Cohesion"
>         direction TB
>         A2["Module C<br>━━━━━━<br>func1()<br>func5()"]
>         B2["Module D<br>━━━━━━<br>func2()<br>func4()"]
>         A2 <-->|"5 dependencies"| B2
>     end
>
>     style A1 fill:#e8f5e9
>     style B1 fill:#e8f5e9
>     style A2 fill:#ffcdd2
>     style B2 fill:#ffcdd2
> ```
>
> **The ideal:** Highly cohesive modules with minimal coupling between them. DSM makes this visible — clusters on the diagonal represent high cohesion, while off-diagonal marks represent coupling.
>
> {: .exam-tip }
> > **Exam Tip:** Coupling and cohesion are inversely related in practice: splitting a module reduces its internal cohesion but increases coupling (more inter-module interfaces). The art of modular design is finding the right balance.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 260 — Q13

> [!question] Question
> Sullivan et al.'s NOV theory treats each module as a "real option." Why does this make modularity more valuable when future requirements are highly uncertain compared to when they are stable?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.2 Net Option Value (NOV) Theory
>
> **What is it?**
> Sullivan et al.  applied financial options theory to software design. Each module in a modular system represents a *real option* — the right (but not obligation) to replace it independently.
>
> - **Non-modular system:** 1 option — accept or reject the entire design
> - **Modular system:** N options — each module can be independently replaced
>
> **KWIC case study (Parnas):**
> The Key Word In Context (KWIC) system was decomposed two ways:
> - *Processing-step decomposition:* modules correspond to processing stages → coupled design (changing one stage affects all downstream stages)
> - *Information-hiding decomposition:* modules hide design decisions → modular design (changing one decision affects only one module)
>
> The information-hiding decomposition has higher NOV because it preserves more options for future change. The more uncertain future requirements are, the more valuable modularity becomes.
>
> #### Net Option Value (NOV)
>
> Sullivan et al. applied Baldwin and Clark's theory of modularity to software, showing that modular designs create **real options** -- the ability to make independent changes has quantifiable economic value .
>
> | Concept | Definition |
> |---------|-----------|
> | **Net Option Value** | Expected payoff of modularity, balancing Technical Potential against Redesign and Visibility Cost |
> | **Environment DSM (EDSM)** | Extends the standard DSM by adding exogenous environment parameters that model how external forces drive design changes |
> | **Information hiding** | Decouples design decisions likely to change, enabling independent module modification |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 261 — Q14

> [!question] Question
> In the KWIC case study, the information-hiding decomposition is more modular than the processing-step decomposition. What design principle distinguishes the two, and how would you recognize this distinction in a real codebase?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### KWIC Case Study
>
> Sullivan et al. tested the theory on Parnas's classic Key Words in Context (KWIC) system, comparing two decompositions :
>
> - **Processing-step decomposition**: modules aligned with computational steps -- highly coupled
> - **Information-hiding decomposition**: modules aligned with design decisions likely to change -- modular
>
> The options-based analysis confirmed Parnas's original conclusion: the information-hiding decomposition has **higher Net Option Value** because each module can be independently redesigned without affecting others. This provides an **economic justification** for Parnas's design principles beyond the usual engineering arguments.
>
> ![Non-modular design offers one option (accept/reject whole); modular design offers N independent replacement options](nov-options.svg)
>
> #### 6.2 Mozilla vs. Linux Case Study
>
> **The central case study** :
>
> | Metric | Mozilla v1 | Linux | Mozilla v2 |
> |--------|-----------|-------|------------|
> | Source Files | 1,684 | 1,678 | 1,508 |
> | Dependencies | 6,717 | 9,110 | 3,037 |
> | **Propagation Cost** | **17.35%** | **5.82%** | **2.78%** |
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "width": 400,
>   "height": 280,
>   "title": {
>     "text": "Propagation Cost: Mozilla vs Linux",
>     "subtitle": "Source: MacCormack et al. 2006"
>   },
>   "data": {
>     "values": [
>       {"system": "Mozilla v1 (1998)", "value": 17.35},
>       {"system": "Linux v2.1.105", "value": 5.82},
>       {"system": "Mozilla redesign (1998)", "value": 2.78}
>     ]
>   },
>   "mark": {"type": "bar", "cornerRadiusTopLeft": 4, "cornerRadiusTopRight": 4},
>   "encoding": {
>     "y": {"field": "system", "type": "nominal", "sort": null, "axis": {"title": null, "labelFontSize": 13}},
>     "x": {"field": "value", "type": "quantitative", "title": "Propagation Cost (%)"},
>     "color": {
>       "field": "system",
>       "type": "nominal",
>       "scale": {
>         "domain": ["Mozilla v1 (1998)", "Linux v2.1.105", "Mozilla redesign (1998)"],
>         "range": ["#d32f2f", "#019546", "#81c784"]
>       },
>       "legend": null
>     }
>   }
> }
> ```
>
> **Key findings:**
> 1. Linux has *more* dependencies than Mozilla v1 (9,110 vs 6,717) but dramatically lower PC (5.82% vs 17.35%). **Number of dependencies alone does not determine modularity** — structure matters.
> 2. Mozilla's purposeful redesign achieved PC = 2.78% — lower than Linux. **Architecture is a deliberate choice**, not an inevitable consequence of system size.
> 3. The redesign reduced dependencies from 6,717 to 3,037 and files from 1,684 to 1,508 — both dependency elimination and module consolidation.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 262 — Q15

> [!question] Question
> Coupling and cohesion often trade off against each other — splitting a module reduces cohesion but may reduce coupling. How would you decide when a module should be split versus kept together?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.3 Coupling and Cohesion
>
> **What are they?**
>
> **Coupling** (between modules) — the degree of interdependence between modules.
> - Goal: **Minimize** coupling
> - Measured by: fan-in, fan-out, dependency density $= \frac{\text{deps}}{N(N-1)}$
> - Low coupling = modules can be changed independently
>
> **Cohesion** (within modules) — the degree to which elements within a module belong together.
> - Goal: **Maximize** cohesion
> - Measured by: LCOM (Lack of Cohesion of Methods), conceptual cohesion
> - High cohesion = module has a single, focused purpose
>
> ```mermaid
> graph TB
>     subgraph "Good: Low Coupling, High Cohesion"
>         direction TB
>         A1["Module A<br>━━━━━━<br>func1()<br>func2()<br>func3()"]
>         B1["Module B<br>━━━━━━<br>func4()<br>func5()<br>func6()"]
>         A1 -.->|"1 dependency"| B1
>     end
>     subgraph "Bad: High Coupling, Low Cohesion"
>         direction TB
>         A2["Module C<br>━━━━━━<br>func1()<br>func5()"]
>         B2["Module D<br>━━━━━━<br>func2()<br>func4()"]
>         A2 <-->|"5 dependencies"| B2
>     end
>
>     style A1 fill:#e8f5e9
>     style B1 fill:#e8f5e9
>     style A2 fill:#ffcdd2
>     style B2 fill:#ffcdd2
> ```
>
> **The ideal:** Highly cohesive modules with minimal coupling between them. DSM makes this visible — clusters on the diagonal represent high cohesion, while off-diagonal marks represent coupling.
>
> {: .exam-tip }
> > **Exam Tip:** Coupling and cohesion are inversely related in practice: splitting a module reduces its internal cohesion but increases coupling (more inter-module interfaces). The art of modular design is finding the right balance.
>
> #### Modifiability Tactics and DSM
>
> Bogner et al. identify **15 modifiability tactics** organized in three categories :
>
> | Category | Tactics | Count |
> |----------|---------|:-----:|
> | **Increase Cohesion** | Split Module, Increase Semantic Coherence, ... | 5 |
> | **Reduce Coupling** | Encapsulate, Use an Intermediary, Restrict Dependencies, ... | 4 |
> | **Defer Binding Time** | Runtime Registration, Configuration Files, ... | 6 |
>
> ![DSM architectural patterns: vertical bus (library used by many) and horizontal bus (controller calling many)](bus-patterns.svg)
>
> These tactics map directly to observable DSM patterns:
>
> | Tactic | DSM Effect |
> |--------|-----------|
> | **Reduce Coupling** | Fewer off-diagonal entries -- dependencies between modules decrease |
> | **Increase Cohesion** | Denser diagonal blocks -- dependencies within modules increase |
> | **Split Module** | Smaller, more focused clusters with clearer boundaries |
> | **Use an Intermediary** | Replaces direct dependencies with indirect paths through a controlled interface |
>
> Nord et al. formalized this connection: DSM clustering operationalizes the "Increase Cohesion" / "Reduce Coupling" pair, while partitioning and tearing break cyclical dependencies that are sometimes called "code cancer" .
>
> ![Layered architecture dependency graph — upward dependencies (above the diagonal) indicate architectural violations](achi_graph.png)

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 263 — Q16

> [!question] Question
> The lecture lists six quality attributes enabled by modularity (testability, scalability, comprehensibility, changeability, concurrent development, reusability). Are there situations where modularity works against any of these attributes?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.1 Why Modularity Matters
>
> **What is it?**
> Modularity is the degree to which a system is composed of discrete, well-bounded components. A modular system allows changes, testing, and understanding of individual parts without needing to comprehend the whole.
>
> **Quality attributes enabled by modularity:**
>
> | Attribute | How Modularity Helps |
> |-----------|---------------------|
> | Testability | Test modules in isolation with mocks |
> | Scalability | Replace or replicate bottleneck modules |
> | Comprehensibility | Understand one module at a time |
> | Changeability | Modify without ripple effects |
> | Concurrent Development | Teams work on separate modules |
> | Reusability | Extract and share well-bounded modules |
>
> #### Modularity Beyond OO: Aspect-Oriented Analysis
>
> Ribeiro and Sousa extended DSM analysis to aspect-oriented systems, revealing that while aspects successfully modularize crosscutting concerns, they can **reduce class modularity** because classes can no longer be understood in isolation . Introducing explicit **design rules** as visible modules restored both class and crosscutting modularity -- reinforcing that information hiding interfaces must be rigorously obeyed regardless of the programming paradigm.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 264 — Q17

> [!question] Question
> A microservices architecture has low coupling between services but each service internally is a monolith with high coupling. Is this system truly modular? Why or why not?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.3 Coupling and Cohesion
>
> **What are they?**
>
> **Coupling** (between modules) — the degree of interdependence between modules.
> - Goal: **Minimize** coupling
> - Measured by: fan-in, fan-out, dependency density $= \frac{\text{deps}}{N(N-1)}$
> - Low coupling = modules can be changed independently
>
> **Cohesion** (within modules) — the degree to which elements within a module belong together.
> - Goal: **Maximize** cohesion
> - Measured by: LCOM (Lack of Cohesion of Methods), conceptual cohesion
> - High cohesion = module has a single, focused purpose
>
> ```mermaid
> graph TB
>     subgraph "Good: Low Coupling, High Cohesion"
>         direction TB
>         A1["Module A<br>━━━━━━<br>func1()<br>func2()<br>func3()"]
>         B1["Module B<br>━━━━━━<br>func4()<br>func5()<br>func6()"]
>         A1 -.->|"1 dependency"| B1
>     end
>     subgraph "Bad: High Coupling, Low Cohesion"
>         direction TB
>         A2["Module C<br>━━━━━━<br>func1()<br>func5()"]
>         B2["Module D<br>━━━━━━<br>func2()<br>func4()"]
>         A2 <-->|"5 dependencies"| B2
>     end
>
>     style A1 fill:#e8f5e9
>     style B1 fill:#e8f5e9
>     style A2 fill:#ffcdd2
>     style B2 fill:#ffcdd2
> ```
>
> **The ideal:** Highly cohesive modules with minimal coupling between them. DSM makes this visible — clusters on the diagonal represent high cohesion, while off-diagonal marks represent coupling.
>
> {: .exam-tip }
> > **Exam Tip:** Coupling and cohesion are inversely related in practice: splitting a module reduces its internal cohesion but increases coupling (more inter-module interfaces). The art of modular design is finding the right balance.
>
> #### The Feedback System Perspective
>
> Lehman's 1996 revisitation  introduced a crucial insight: E-type evolution processes are **multi-loop, multi-level feedback systems**. This has several important consequences:
>
> - **Local improvements are attenuated or inverted** -- productivity improvements in one part of the process may be cancelled out by organizational feedback loops (e.g., faster coding leads to more features requested, which leads to more complexity, which slows coding again)
> - **Self-stabilization through negative feedback** -- Laws III, IV, and V describe how organizational and cognitive constraints act as governors that keep the evolution rate approximately constant regardless of management intervention
> - **Instability from excessive positive feedback** -- when feedback loops reinforce rather than dampen change (e.g., accumulating technical debt that accelerates further debt), the system can enter a state of declining quality (Law VII)
>
> This perspective explains why simplistic process improvements (adding developers, adopting new tools) often fail to produce lasting gains: they address only the forward path of the feedback system while ignoring the return paths that regulate overall system behavior .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 265 — Q18

> [!question] Question
> Two architects examine the same DSM but one uses the convention "rows depend on columns" while the other uses "columns depend on rows." What errors could result from this confusion?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.4 DSM Operations
>
> | Operation | Purpose | Result |
> |-----------|---------|--------|
> | **Partitioning** | Reorder rows/columns for lower-triangular form | Reveals natural layering |
> | **Clustering** | Group mutually dependent elements | Identifies module boundaries |
> | **Tearing** | Remove feedback marks to break cycles | Suggests refactoring targets |
> | **Banding** | Highlight independent activities | Shows parallelization opportunities |
>
> **Partitioning algorithm:**
> 1. Find elements with no predecessors → place them first
> 2. Remove placed elements from the matrix
> 3. Repeat until all elements are placed
> 4. Result: topological sort of the dependency graph
>
> **Concrete Example — Partitioning:**
>
> **Before (original order A–G)** — 6 above-diagonal marks (↑X = violations):
>
> |   | A | B | C | D | E | F | G |
> |---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | **A** | · |   | ↑X |   |   |   |   |
> | **B** |   | · |   |   |   | ↑X |   |
> | **C** |   |   | · | ↑X |   |   | ↑X |
> | **D** |   | X |   | · |   | ↑X |   |
> | **E** | X |   | X | X | · |   | ↑X |
> | **F** |   |   |   |   |   | · |   |
> | **G** |   | X |   |   |   |   | · |
>
> **After (F→B→D→G→C→A→E)** — all marks below diagonal ✓:
>
> |   | F | B | D | G | C | A | E |
> |---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | **F** | · |   |   |   |   |   |   |
> | **B** | X | · |   |   |   |   |   |
> | **D** | X | X | · |   |   |   |   |
> | **G** |   | X |   | · |   |   |   |
> | **C** |   |   | X | X | · |   |   |
> | **A** |   |   |   |   | X | · |   |
> | **E** |   |   | X | X | X | X | · |
>
> The algorithm discovers: F has no dependencies (goes first), E provides nothing (goes last), and the rest form a dependency chain F→{B,D}→G→C→A→E.
>
> **Concrete Example — Clustering:**
>
> **Before (original order 1–7)** — dependencies scattered:
>
> …
>
> #### Modifiability Tactics and DSM
>
> Bogner et al. identify **15 modifiability tactics** organized in three categories :
>
> | Category | Tactics | Count |
> |----------|---------|:-----:|
> | **Increase Cohesion** | Split Module, Increase Semantic Coherence, ... | 5 |
> | **Reduce Coupling** | Encapsulate, Use an Intermediary, Restrict Dependencies, ... | 4 |
> | **Defer Binding Time** | Runtime Registration, Configuration Files, ... | 6 |
>
> ![DSM architectural patterns: vertical bus (library used by many) and horizontal bus (controller calling many)](bus-patterns.svg)
>
> These tactics map directly to observable DSM patterns:
>
> | Tactic | DSM Effect |
> |--------|-----------|
> | **Reduce Coupling** | Fewer off-diagonal entries -- dependencies between modules decrease |
> | **Increase Cohesion** | Denser diagonal blocks -- dependencies within modules increase |
> | **Split Module** | Smaller, more focused clusters with clearer boundaries |
> | **Use an Intermediary** | Replaces direct dependencies with indirect paths through a controlled interface |
>
> Nord et al. formalized this connection: DSM clustering operationalizes the "Increase Cohesion" / "Reduce Coupling" pair, while partitioning and tearing break cyclical dependencies that are sometimes called "code cancer" .
>
> ![Layered architecture dependency graph — upward dependencies (above the diagonal) indicate architectural violations](achi_graph.png)

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 266 — Q19

> [!question] Question
> After partitioning a DSM, three marks remain above the diagonal. What do these marks tell you about the system, and what are your options for addressing them?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Modifiability Tactics and DSM
>
> Bogner et al. identify **15 modifiability tactics** organized in three categories :
>
> | Category | Tactics | Count |
> |----------|---------|:-----:|
> | **Increase Cohesion** | Split Module, Increase Semantic Coherence, ... | 5 |
> | **Reduce Coupling** | Encapsulate, Use an Intermediary, Restrict Dependencies, ... | 4 |
> | **Defer Binding Time** | Runtime Registration, Configuration Files, ... | 6 |
>
> ![DSM architectural patterns: vertical bus (library used by many) and horizontal bus (controller calling many)](bus-patterns.svg)
>
> These tactics map directly to observable DSM patterns:
>
> | Tactic | DSM Effect |
> |--------|-----------|
> | **Reduce Coupling** | Fewer off-diagonal entries -- dependencies between modules decrease |
> | **Increase Cohesion** | Denser diagonal blocks -- dependencies within modules increase |
> | **Split Module** | Smaller, more focused clusters with clearer boundaries |
> | **Use an Intermediary** | Replaces direct dependencies with indirect paths through a controlled interface |
>
> Nord et al. formalized this connection: DSM clustering operationalizes the "Increase Cohesion" / "Reduce Coupling" pair, while partitioning and tearing break cyclical dependencies that are sometimes called "code cancer" .
>
> ![Layered architecture dependency graph — upward dependencies (above the diagonal) indicate architectural violations](achi_graph.png)
>
> #### 5.4 DSM Operations
>
> | Operation | Purpose | Result |
> |-----------|---------|--------|
> | **Partitioning** | Reorder rows/columns for lower-triangular form | Reveals natural layering |
> | **Clustering** | Group mutually dependent elements | Identifies module boundaries |
> | **Tearing** | Remove feedback marks to break cycles | Suggests refactoring targets |
> | **Banding** | Highlight independent activities | Shows parallelization opportunities |
>
> **Partitioning algorithm:**
> 1. Find elements with no predecessors → place them first
> 2. Remove placed elements from the matrix
> 3. Repeat until all elements are placed
> 4. Result: topological sort of the dependency graph
>
> **Concrete Example — Partitioning:**
>
> **Before (original order A–G)** — 6 above-diagonal marks (↑X = violations):
>
> |   | A | B | C | D | E | F | G |
> |---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | **A** | · |   | ↑X |   |   |   |   |
> | **B** |   | · |   |   |   | ↑X |   |
> | **C** |   |   | · | ↑X |   |   | ↑X |
> | **D** |   | X |   | · |   | ↑X |   |
> | **E** | X |   | X | X | · |   | ↑X |
> | **F** |   |   |   |   |   | · |   |
> | **G** |   | X |   |   |   |   | · |
>
> **After (F→B→D→G→C→A→E)** — all marks below diagonal ✓:
>
> |   | F | B | D | G | C | A | E |
> |---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | **F** | · |   |   |   |   |   |   |
> | **B** | X | · |   |   |   |   |   |
> | **D** | X | X | · |   |   |   |   |
> | **G** |   | X |   | · |   |   |   |
> | **C** |   |   | X | X | · |   |   |
> | **A** |   |   |   |   | X | · |   |
> | **E** |   |   | X | X | X | X | · |
>
> The algorithm discovers: F has no dependencies (goes first), E provides nothing (goes last), and the rest form a dependency chain F→{B,D}→G→C→A→E.
>
> **Concrete Example — Clustering:**
>
> **Before (original order 1–7)** — dependencies scattered:
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 267 — Q20

> [!question] Question
> A DSM has a large cluster of 15 mutually dependent elements. From a maintainability perspective, why is this concerning, and what would clustering reveal about this group?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.4 DSM Operations
>
> | Operation | Purpose | Result |
> |-----------|---------|--------|
> | **Partitioning** | Reorder rows/columns for lower-triangular form | Reveals natural layering |
> | **Clustering** | Group mutually dependent elements | Identifies module boundaries |
> | **Tearing** | Remove feedback marks to break cycles | Suggests refactoring targets |
> | **Banding** | Highlight independent activities | Shows parallelization opportunities |
>
> **Partitioning algorithm:**
> 1. Find elements with no predecessors → place them first
> 2. Remove placed elements from the matrix
> 3. Repeat until all elements are placed
> 4. Result: topological sort of the dependency graph
>
> **Concrete Example — Partitioning:**
>
> **Before (original order A–G)** — 6 above-diagonal marks (↑X = violations):
>
> |   | A | B | C | D | E | F | G |
> |---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | **A** | · |   | ↑X |   |   |   |   |
> | **B** |   | · |   |   |   | ↑X |   |
> | **C** |   |   | · | ↑X |   |   | ↑X |
> | **D** |   | X |   | · |   | ↑X |   |
> | **E** | X |   | X | X | · |   | ↑X |
> | **F** |   |   |   |   |   | · |   |
> | **G** |   | X |   |   |   |   | · |
>
> **After (F→B→D→G→C→A→E)** — all marks below diagonal ✓:
>
> |   | F | B | D | G | C | A | E |
> |---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | **F** | · |   |   |   |   |   |   |
> | **B** | X | · |   |   |   |   |   |
> | **D** | X | X | · |   |   |   |   |
> | **G** |   | X |   | · |   |   |   |
> | **C** |   |   | X | X | · |   |   |
> | **A** |   |   |   |   | X | · |   |
> | **E** |   |   | X | X | X | X | · |
>
> The algorithm discovers: F has no dependencies (goes first), E provides nothing (goes last), and the rest form a dependency chain F→{B,D}→G→C→A→E.
>
> **Concrete Example — Clustering:**
>
> **Before (original order 1–7)** — dependencies scattered:
>
> …
>
> #### Clustering
>
> Group elements into **modules** that maximize intra-group dependencies and minimize inter-group dependencies. The goal is to find subsets of DSM elements that are "mutually exclusive or minimally interacting" . A well-clustered DSM shows a **block-diagonal** pattern: dense blocks along the diagonal (cohesive modules) with sparse entries elsewhere (loose coupling) .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 268 — Q21

> [!question] Question
> Explain why the ordering of rows and columns in a DSM matters even though the mathematical dependency information is the same regardless of ordering.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.4 DSM Operations
>
> | Operation | Purpose | Result |
> |-----------|---------|--------|
> | **Partitioning** | Reorder rows/columns for lower-triangular form | Reveals natural layering |
> | **Clustering** | Group mutually dependent elements | Identifies module boundaries |
> | **Tearing** | Remove feedback marks to break cycles | Suggests refactoring targets |
> | **Banding** | Highlight independent activities | Shows parallelization opportunities |
>
> **Partitioning algorithm:**
> 1. Find elements with no predecessors → place them first
> 2. Remove placed elements from the matrix
> 3. Repeat until all elements are placed
> 4. Result: topological sort of the dependency graph
>
> **Concrete Example — Partitioning:**
>
> **Before (original order A–G)** — 6 above-diagonal marks (↑X = violations):
>
> |   | A | B | C | D | E | F | G |
> |---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | **A** | · |   | ↑X |   |   |   |   |
> | **B** |   | · |   |   |   | ↑X |   |
> | **C** |   |   | · | ↑X |   |   | ↑X |
> | **D** |   | X |   | · |   | ↑X |   |
> | **E** | X |   | X | X | · |   | ↑X |
> | **F** |   |   |   |   |   | · |   |
> | **G** |   | X |   |   |   |   | · |
>
> **After (F→B→D→G→C→A→E)** — all marks below diagonal ✓:
>
> |   | F | B | D | G | C | A | E |
> |---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | **F** | · |   |   |   |   |   |   |
> | **B** | X | · |   |   |   |   |   |
> | **D** | X | X | · |   |   |   |   |
> | **G** |   | X |   | · |   |   |   |
> | **C** |   |   | X | X | · |   |   |
> | **A** |   |   |   |   | X | · |   |
> | **E** |   |   | X | X | X | X | · |
>
> The algorithm discovers: F has no dependencies (goes first), E provides nothing (goes last), and the rest form a dependency chain F→{B,D}→G→C→A→E.
>
> **Concrete Example — Clustering:**
>
> **Before (original order 1–7)** — dependencies scattered:
>
> …
>
> #### 5.1 What Is a DSM?
>
> **Definition:** A Design Structure Matrix (DSM)  is a square matrix showing relationships between elements in a system. Also known as Dependency Structure Matrix.
>
> **How to read it:**
> - Each row and column represents a system element (file, module, class)
> - An X in row $i$, column $j$ means element $i$ depends on element $j$
> - The diagonal represents self-relationships (always present)
> - Reading across a row: what this element depends on
> - Reading down a column: what depends on this element

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 269 — Q22

> [!question] Question
> Compare the Tearing and Partitioning operations. When would you use each, and can they produce contradictory recommendations?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.4 DSM Operations
>
> | Operation | Purpose | Result |
> |-----------|---------|--------|
> | **Partitioning** | Reorder rows/columns for lower-triangular form | Reveals natural layering |
> | **Clustering** | Group mutually dependent elements | Identifies module boundaries |
> | **Tearing** | Remove feedback marks to break cycles | Suggests refactoring targets |
> | **Banding** | Highlight independent activities | Shows parallelization opportunities |
>
> **Partitioning algorithm:**
> 1. Find elements with no predecessors → place them first
> 2. Remove placed elements from the matrix
> 3. Repeat until all elements are placed
> 4. Result: topological sort of the dependency graph
>
> **Concrete Example — Partitioning:**
>
> **Before (original order A–G)** — 6 above-diagonal marks (↑X = violations):
>
> |   | A | B | C | D | E | F | G |
> |---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | **A** | · |   | ↑X |   |   |   |   |
> | **B** |   | · |   |   |   | ↑X |   |
> | **C** |   |   | · | ↑X |   |   | ↑X |
> | **D** |   | X |   | · |   | ↑X |   |
> | **E** | X |   | X | X | · |   | ↑X |
> | **F** |   |   |   |   |   | · |   |
> | **G** |   | X |   |   |   |   | · |
>
> **After (F→B→D→G→C→A→E)** — all marks below diagonal ✓:
>
> |   | F | B | D | G | C | A | E |
> |---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | **F** | · |   |   |   |   |   |   |
> | **B** | X | · |   |   |   |   |   |
> | **D** | X | X | · |   |   |   |   |
> | **G** |   | X |   | · |   |   |   |
> | **C** |   |   | X | X | · |   |   |
> | **A** |   |   |   |   | X | · |   |
> | **E** |   |   | X | X | X | X | · |
>
> The algorithm discovers: F has no dependencies (goes first), E provides nothing (goes last), and the rest form a dependency chain F→{B,D}→G→C→A→E.
>
> **Concrete Example — Clustering:**
>
> **Before (original order 1–7)** — dependencies scattered:
>
> …
>
> #### Tearing
>
> When partitioning cannot eliminate all feedback marks, **tearing** selects specific feedback dependencies to "break" by treating them as assumptions that will be iterated upon. This converts cycles into manageable sequential steps .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 270 — Q23

> [!question] Question
> A system has a module that appears as both a vertical bus (many modules depend on it) and it depends on several other modules. Is this a library, a controller, or something else? What are the architectural implications?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.6 Bus Patterns
>
> **Vertical Bus (Library):**
> - Column with many marks (many modules depend on it)
> - No outgoing dependencies
> - Examples: logging framework, utility library, error handling
>
> **Horizontal Bus (Controller):**
> - Row with many marks (depends on many modules)
> - Few incoming dependencies
> - Examples: main controller, orchestration service, entry point
>
> **DSM examples** (· = diagonal, **★** = bus element):
>
> **Vertical Bus** — column E has many marks (A, B, C, F all depend on E):
>
> |   | A | B | C | D | **★E** | F |
> |---|:-:|:-:|:-:|:-:|:-:|:-:|
> | **A** | · |   |   |   | X |   |
> | **B** |   | · |   |   | X |   |
> | **C** |   |   | · |   | X |   |
> | **D** |   |   |   | · |   |   |
> | **★E** |   |   |   |   | · |   |
> | **F** |   |   |   |   | X | · |
>
> **Horizontal Bus** — row E has many marks (E depends on A, B, C, F):
>
> |   | A | B | C | D | E | F |
> |---|:-:|:-:|:-:|:-:|:-:|:-:|
> | **A** | · |   |   |   |   |   |
> | **B** |   | · |   |   |   |   |
> | **C** |   |   | · |   |   |   |
> | **D** |   |   |   | · |   |   |
> | **★E** | X | X | X |   | · | X |
> | **F** |   |   |   |   |   | · |
>
> **Why bus patterns matter:** They are architecturally intentional (libraries *should* be widely used; controllers *should* orchestrate many services), but they inflate propagation cost because they create many transitive paths through the system.
>
> #### Modifiability Tactics and DSM
>
> Bogner et al. identify **15 modifiability tactics** organized in three categories :
>
> | Category | Tactics | Count |
> |----------|---------|:-----:|
> | **Increase Cohesion** | Split Module, Increase Semantic Coherence, ... | 5 |
> | **Reduce Coupling** | Encapsulate, Use an Intermediary, Restrict Dependencies, ... | 4 |
> | **Defer Binding Time** | Runtime Registration, Configuration Files, ... | 6 |
>
> ![DSM architectural patterns: vertical bus (library used by many) and horizontal bus (controller calling many)](bus-patterns.svg)
>
> These tactics map directly to observable DSM patterns:
>
> | Tactic | DSM Effect |
> |--------|-----------|
> | **Reduce Coupling** | Fewer off-diagonal entries -- dependencies between modules decrease |
> | **Increase Cohesion** | Denser diagonal blocks -- dependencies within modules increase |
> | **Split Module** | Smaller, more focused clusters with clearer boundaries |
> | **Use an Intermediary** | Replaces direct dependencies with indirect paths through a controlled interface |
>
> Nord et al. formalized this connection: DSM clustering operationalizes the "Increase Cohesion" / "Reduce Coupling" pair, while partitioning and tearing break cyclical dependencies that are sometimes called "code cancer" .
>
> ![Layered architecture dependency graph — upward dependencies (above the diagonal) indicate architectural violations](achi_graph.png)

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 271 — Q24

> [!question] Question
> The lecture shows that a single above-diagonal mark in a layered DSM represents an upward dependency violation. In practice, are all violations equally harmful? What factors determine severity?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Three Fundamental Dependency Patterns
>
> | Pattern | DSM Signature | Meaning | Software Example |
> |---------|--------------|---------|-----------------|
> | **Independent** | No marks between A and B | No relationship, can work in parallel | Unrelated services |
> | **Dependent** | Mark below diagonal only | Sequential, layered — B depends on A | UI layer depends on API layer |
> | **Coupled** | Marks both directions | Mutual dependency, cyclic | Circular imports between modules |
>
> **DSM examples** (· = diagonal):
>
> **Independent** — no marks between A and B:
>
> |   | A | B |
> |---|:-:|:-:|
> | **A** | · |   |
> | **B** |   | · |
>
> **Dependent** — B depends on A (mark below diagonal):
>
> |   | A | B |
> |---|:-:|:-:|
> | **A** | · |   |
> | **B** | X | · |
>
> **Coupled** — mutual dependency (marks in both directions):
>
> |   | A | B |
> |---|:-:|:-:|
> | **A** | · | ↑X |
> | **B** | X | · |
>
> (↑X = above-diagonal mark, indicating a feedback/violation)
>
> **Design goal:** Maximize independent and dependent patterns. Minimize coupled patterns (cycles create ripple effects).
>
> #### 5.5 Layering and Violations
>
> **Rule:** After partitioning, a well-architected system has most marks below the diagonal. Marks above the diagonal = layering violations.
>
> - **Below diagonal (green):** Valid dependency — higher layer depends on lower layer
> - **Above diagonal (red):** Violation — lower layer depends on higher layer (upward dependency)
>
> **Concrete Example — Clean layered system** (8 elements, all marks below diagonal):
>
> |   | A | E | B | C | D | F | G | H |
> |---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | **A** | · |   |   |   |   |   |   |   |
> | **E** |   | · |   |   |   |   |   |   |
> | **B** | X |   | · |   |   |   |   |   |
> | **C** | X |   |   | · |   |   |   |   |
> | **D** | X |   |   |   | · |   |   |   |
> | **F** |   |   | X |   |   | · |   |   |
> | **G** |   |   |   |   | X |   | · |   |
> | **H** |   |   |   |   | X |   | X | · |
>
> **With violation — E depends on G** (upward dependency ↑X):
>
> |   | A | E | B | C | D | F | G | H |
> |---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | **A** | · |   |   |   |   |   |   |   |
> | **E** |   | · |   |   |   |   | ↑X |   |
> | **B** | X |   | · |   |   |   |   |   |
> | **C** | X |   |   | · |   |   |   |   |
> | **D** | X |   |   |   | · |   |   |   |
> | **F** |   |   | X |   |   | · |   |   |
> | **G** |   |   |   |   | X |   | · |   |
> | **H** |   |   |   |   | X |   | X | · |
>
> E→G is above the diagonal — a higher layer depends on a lower layer, violating the layering constraint. Changes to G can now break E, which defeats the purpose of layering.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 272 — Q25

> [!question] Question
> Linux has more absolute dependencies than Mozilla v1 (9,110 vs 6,717) but much lower propagation cost (5.82% vs 17.35%). Explain how this is possible and what it reveals about the relationship between dependency count and modularity.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 6.2 Mozilla vs. Linux Case Study
>
> **The central case study** :
>
> | Metric | Mozilla v1 | Linux | Mozilla v2 |
> |--------|-----------|-------|------------|
> | Source Files | 1,684 | 1,678 | 1,508 |
> | Dependencies | 6,717 | 9,110 | 3,037 |
> | **Propagation Cost** | **17.35%** | **5.82%** | **2.78%** |
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "width": 400,
>   "height": 280,
>   "title": {
>     "text": "Propagation Cost: Mozilla vs Linux",
>     "subtitle": "Source: MacCormack et al. 2006"
>   },
>   "data": {
>     "values": [
>       {"system": "Mozilla v1 (1998)", "value": 17.35},
>       {"system": "Linux v2.1.105", "value": 5.82},
>       {"system": "Mozilla redesign (1998)", "value": 2.78}
>     ]
>   },
>   "mark": {"type": "bar", "cornerRadiusTopLeft": 4, "cornerRadiusTopRight": 4},
>   "encoding": {
>     "y": {"field": "system", "type": "nominal", "sort": null, "axis": {"title": null, "labelFontSize": 13}},
>     "x": {"field": "value", "type": "quantitative", "title": "Propagation Cost (%)"},
>     "color": {
>       "field": "system",
>       "type": "nominal",
>       "scale": {
>         "domain": ["Mozilla v1 (1998)", "Linux v2.1.105", "Mozilla redesign (1998)"],
>         "range": ["#d32f2f", "#019546", "#81c784"]
>       },
>       "legend": null
>     }
>   }
> }
> ```
>
> **Key findings:**
> 1. Linux has *more* dependencies than Mozilla v1 (9,110 vs 6,717) but dramatically lower PC (5.82% vs 17.35%). **Number of dependencies alone does not determine modularity** — structure matters.
> 2. Mozilla's purposeful redesign achieved PC = 2.78% — lower than Linux. **Architecture is a deliberate choice**, not an inevitable consequence of system size.
> 3. The redesign reduced dependencies from 6,717 to 3,037 and files from 1,684 to 1,508 — both dependency elimination and module consolidation.
>
> #### The Mozilla vs. Linux Case Study
>
> MacCormack et al. compared two large open-source systems to demonstrate that architecture is a **deliberate managerial choice**, not merely a byproduct of functional requirements :
>
> | Metric | Linux 2.1.105 | Mozilla (1998) | Mozilla (post-redesign) |
> |--------|:---:|:---:|:---:|
> | **Propagation Cost** | 5.82% | 17.35% | 2.78% |
> | **Vertical buses** | 14 | 2 | improved |
> | **Dependency density** (per 1000 pairs) | 3.4 | 2.4 | lower |
>
> Despite having *fewer* raw dependencies per element pair, Mozilla's 1998 architecture was far more coupled than Linux because its dependencies formed long indirect chains. After a purposeful re-design, Mozilla's propagation cost dropped from 17.35% to 2.78% -- a change to a file now impacted **80% fewer files** on average.
>
> ![DSM heatmaps: Mozilla (left) shows scattered dependencies; Linux (right) shows block-diagonal clusters](mozilla-linux-comparison.png)
>
> ![Mozilla DSM after redesign: block-diagonal clusters with sparse inter-cluster dependencies](mozilla-re2.png)
>
> {: .important }
> > Architecture is not wholly determined by function. The Mozilla re-design proves that architects can significantly adapt a design's structure through purposeful effort .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 273 — Q26

> [!question] Question
> Geipel and Schweitzer found that >50% of dependencies are "change neutral." What are the implications of this finding for teams that use static dependency analysis to prioritize refactoring?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 6.3 Dependency Concentration
>
> **What is it?**
> Geipel and Schweitzer  studied 35 Java projects and found:
>
> - **>50% of dependencies** are "change neutral" — they never transmit a single change in the entire development history
> - **Top 10%** of dependencies cause **>70%** of all change propagation (measured in Eclipse)
> - Static DSM **overestimates** change risk because it treats all dependencies equally
>
> …
>
> #### The Concentration Phenomenon
>
> Geipel and Schweitzer studied 35 large open-source Java projects and found that static dependency structure alone is a **poor predictor** of actual change dynamics :
>
> | Finding | Value |
> |---------|-------|
> | Projects where >50% of dependencies were "change neutral" | 32 out of 35 |
> | Share of propagation caused by the top 10% of dependencies | >50% (>70% in Eclipse) |
> | Co-change probability for elements *with* a dependency | 15--60% |
> | Co-change probability for elements *without* a dependency | <5% |
>
> Standard DSM analysis assumes **homogeneity** -- every dependency is equally likely to transmit a change. In reality, most dependencies never transmit a single change during the entire development history, and a small fraction is responsible for the majority of change propagation. This makes static-only propagation estimates "highly inaccurate" .
>
> {: .warning }
> > The higher the concentration of change propagation in a small fraction of dependencies, the better refactoring effort can be **targeted** -- focus on the 10% of "active" dependencies rather than minimizing all dependencies globally .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 274 — Q27

> [!question] Question
> Nord et al.'s enhanced PC assigns dependency weights. What practical challenges would a team face when trying to assign these weights in a real system with thousands of dependencies?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 6.4 Enhanced Propagation Cost
>
> **What is it?**
> Nord et al.  extended PC with dependency weights to address the limitation that original PC treats all dependencies equally.
>
> **The problem:** Original PC yields the same value (33%) before and after applying a strictly layered pattern — it cannot detect the modifiability improvement.
>
> **The solution:** Assign dependency strength $w_{ij} \in [0, 1]$:
> - $w_{ij} = 0.1$ → strong encapsulation tactics prevent ripple (e.g., interface segregation)
> - $w_{ij} = 1.0$ → no tactics, full propagation (e.g., direct field access)
>
> **Three aggregation variants:**
>
> | Variant | What It Measures | Use Case |
> |---------|-----------------|----------|
> | SUM | Total exposure (cumulative) | Worst-case planning |
> | AVG | Expected propagation (mean) | Average-case estimation |
> | MAX | Worst-case single path | Risk analysis |
>
> **Result:** Enhanced PC detects improvement from encapsulation tactics (24% → 13%) that original PC misses entirely.
>
> #### Enhanced Propagation Cost
>
> Nord et al. demonstrated that the original binary PC metric fails to detect modifiability improvements from architectural transformations. For example, converting a tightly coupled system to a strictly layered pattern yields the **same PC value** (33%) before and after -- a false negative .
>
> Their enhanced variants introduce **dependency weights** (0 to 1) reflecting the strength of architectural shielding:
>
> | Weight | Meaning | Example |
> |:------:|---------|---------|
> | **0.1** (small) | Strong tactics prevent ripple effect | Encapsulated interface |
> | **0.5** (medium) | Some tactics but insufficient shielding | Partial abstraction |
> | **1.0** (large) | No tactics, full ripple propagation | Direct dependency |
>
> Three aggregation formulas for parallel paths:
>
> | Formula | Semantics | Use Case |
> |---------|-----------|----------|
> | **SUM** | Cumulative exposure across all paths | Total risk assessment |
> | **AVG** | Expected propagation assuming equal probability | Typical-case analysis |
> | **MAX** | Worst-case propagation along least-protected path | Conservative estimation |
>
> Applying the "Encapsulate" and "Use an Intermediary" tactics reduced enhanced PC from 24%/18%/23% (SUM/AVG/MAX) down to 13%/13%/13%, correctly detecting the modifiability improvement that binary PC missed .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 275 — Q28

> [!question] Question
> The ABB case study achieved 75-83% effort reduction through refactoring with only ~3 hours/week of expert consultation. Why might such a small investment produce such large returns? Under what conditions would this approach fail?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 7.1 Case Studies
>
> | Case | Metric | Before | After | Source |
> |------|--------|--------|-------|--------|
> | Microsoft Windows 7 | Inter-module deps (top 5%) | 1.10x growth | 0.85x reduction |  |
> | ABB DID (30kLOC) | New component effort | 6-8 weeks | 1-2 weeks (-75%) |  |
> | ABB DID | Code duplication | 5,647 lines | 338 lines (-82%) |  |
> | 4 companies (3 MLOC) | Automatic refactoring | — | 55% improved, 10% degraded |  |
> | Mozilla | Propagation Cost | 17.35% | 2.78% (-84%) |  |
>
> **Key lessons:**
> 1. **Targeted refactoring works:** Microsoft focused on the top 5% most-coupled modules and achieved 0.85x dependency reduction while non-refactored modules grew 1.10x
> 2. **Modest investment, large returns:** ABB used ~3 hours/week of SE expert consultation for 3 months and achieved 75-83% effort reduction
> 3. **Automatic refactoring has limits:** In 55% of cases it improved maintainability, but 10% showed degradation  — human oversight remains essential
> 4. **Regression is the primary risk:** 76% of Microsoft developers identified regression bugs as the top concern when refactoring
>
> **Concrete Example — ABB DID:**
> ABB's Drives Interface Device (DID) had 30,000 lines of C++ code for controlling industrial drives. Adding a new cooling method required modifying 59 different files — 8-12 weeks of work. After modular refactoring guided by an SE expert, the same type of change took only 1-2 weeks. Code duplication dropped from 5,647 lines to 338 lines (-82%).
>
> {: .exam-tip }
> > **Exam Tip:** Remember three numbers from the case studies: **0.85x** (Microsoft dependency reduction), **-82%** (ABB duplication reduction), **75%** (ABB effort reduction). These quantify the ROI of refactoring.
>
> #### 6.2 Mozilla vs. Linux Case Study
>
> **The central case study** :
>
> | Metric | Mozilla v1 | Linux | Mozilla v2 |
> |--------|-----------|-------|------------|
> | Source Files | 1,684 | 1,678 | 1,508 |
> | Dependencies | 6,717 | 9,110 | 3,037 |
> | **Propagation Cost** | **17.35%** | **5.82%** | **2.78%** |
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "width": 400,
>   "height": 280,
>   "title": {
>     "text": "Propagation Cost: Mozilla vs Linux",
>     "subtitle": "Source: MacCormack et al. 2006"
>   },
>   "data": {
>     "values": [
>       {"system": "Mozilla v1 (1998)", "value": 17.35},
>       {"system": "Linux v2.1.105", "value": 5.82},
>       {"system": "Mozilla redesign (1998)", "value": 2.78}
>     ]
>   },
>   "mark": {"type": "bar", "cornerRadiusTopLeft": 4, "cornerRadiusTopRight": 4},
>   "encoding": {
>     "y": {"field": "system", "type": "nominal", "sort": null, "axis": {"title": null, "labelFontSize": 13}},
>     "x": {"field": "value", "type": "quantitative", "title": "Propagation Cost (%)"},
>     "color": {
>       "field": "system",
>       "type": "nominal",
>       "scale": {
>         "domain": ["Mozilla v1 (1998)", "Linux v2.1.105", "Mozilla redesign (1998)"],
>         "range": ["#d32f2f", "#019546", "#81c784"]
>       },
>       "legend": null
>     }
>   }
> }
> ```
>
> **Key findings:**
> 1. Linux has *more* dependencies than Mozilla v1 (9,110 vs 6,717) but dramatically lower PC (5.82% vs 17.35%). **Number of dependencies alone does not determine modularity** — structure matters.
> 2. Mozilla's purposeful redesign achieved PC = 2.78% — lower than Linux. **Architecture is a deliberate choice**, not an inevitable consequence of system size.
> 3. The redesign reduced dependencies from 6,717 to 3,037 and files from 1,684 to 1,508 — both dependency elimination and module consolidation.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 276 — Q29

> [!question] Question
> The lecture lists "vertical buses penalized unfairly" as a limitation of propagation cost. A logging library used by every module in a 100-module system contributes significantly to PC. Should this library be refactored to reduce PC? Why or why not?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 6.5 Propagation Cost Limitations
>
> | Limitation | Why It Matters |
> |-----------|---------------|
> | Ignores dependency nature | Strong and weak dependencies treated equally |
> | No module cohesion | High cohesion within modules is invisible |
> | Vertical buses penalized | Libraries used by many modules inflate PC unfairly |
> | Cluster choice affects results | Different algorithms give different answers |
> | Binary dependencies only | Cannot distinguish API call from deep internal coupling |
>
> **Remember:** DSM is a tool for insight, not a definitive measure. Combine with code metrics (SIG) and change history (Geipel) for a complete picture.
>
> {: .exam-tip }
> > **Exam Tip:** When discussing PC limitations, always mention Geipel's concentration finding and Nord's weighted enhancement as partial solutions. This shows depth of understanding.
>
> #### 6.1 Propagation Cost Formula
>
> **What is it?**
> Propagation Cost (PC)  measures how far a change to one element ripples through the system.
>
> **Step 1:** Build the visibility matrix by summing powers of the DSM:
>
> $$V = \sum_{n=0}^{k} M^n = M^0 + M^1 + M^2 + \cdots$$
>
> - $M^0$ = Identity (element sees itself)
> - $M^1$ = DSM (direct dependencies, 1 hop)
> - $M^n$ = indirect dependencies ($n$ hops)
>
> **Step 2:** Binarize: $v_{ij} = 1$ if $V_{ij} > 0$ (element $j$ is reachable from $i$)
>
> **Step 3:** Calculate PC:
>
> $$PC = \frac{\sum_{j=1}^{N}\sum_{i=1}^{N} v_{ij}}{N^2}$$
>
> **Interpretation:** PC = 17% means a random change to one element affects approximately 17% of all elements on average. Lower PC = better modularity.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 277 — Q30

> [!question] Question
> Mozilla's redesign reduced PC from 17.35% to 2.78%. Kim et al. found that refactoring at Microsoft reduced dependencies for the top 5% of modules but increased module size (LOC). How can refactoring simultaneously improve structure while making modules larger?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 6.2 Mozilla vs. Linux Case Study
>
> **The central case study** :
>
> | Metric | Mozilla v1 | Linux | Mozilla v2 |
> |--------|-----------|-------|------------|
> | Source Files | 1,684 | 1,678 | 1,508 |
> | Dependencies | 6,717 | 9,110 | 3,037 |
> | **Propagation Cost** | **17.35%** | **5.82%** | **2.78%** |
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "width": 400,
>   "height": 280,
>   "title": {
>     "text": "Propagation Cost: Mozilla vs Linux",
>     "subtitle": "Source: MacCormack et al. 2006"
>   },
>   "data": {
>     "values": [
>       {"system": "Mozilla v1 (1998)", "value": 17.35},
>       {"system": "Linux v2.1.105", "value": 5.82},
>       {"system": "Mozilla redesign (1998)", "value": 2.78}
>     ]
>   },
>   "mark": {"type": "bar", "cornerRadiusTopLeft": 4, "cornerRadiusTopRight": 4},
>   "encoding": {
>     "y": {"field": "system", "type": "nominal", "sort": null, "axis": {"title": null, "labelFontSize": 13}},
>     "x": {"field": "value", "type": "quantitative", "title": "Propagation Cost (%)"},
>     "color": {
>       "field": "system",
>       "type": "nominal",
>       "scale": {
>         "domain": ["Mozilla v1 (1998)", "Linux v2.1.105", "Mozilla redesign (1998)"],
>         "range": ["#d32f2f", "#019546", "#81c784"]
>       },
>       "legend": null
>     }
>   }
> }
> ```
>
> **Key findings:**
> 1. Linux has *more* dependencies than Mozilla v1 (9,110 vs 6,717) but dramatically lower PC (5.82% vs 17.35%). **Number of dependencies alone does not determine modularity** — structure matters.
> 2. Mozilla's purposeful redesign achieved PC = 2.78% — lower than Linux. **Architecture is a deliberate choice**, not an inevitable consequence of system size.
> 3. The redesign reduced dependencies from 6,717 to 3,037 and files from 1,684 to 1,508 — both dependency elimination and module consolidation.
>
> #### Key Findings
>
> | Finding | Detail |
> |---------|--------|
> | Top 5% of preferentially refactored modules | Inter-module dependencies decreased by factor **0.85** |
> | Non-refactored modules | Dependencies increased by factor **1.10** |
> | Engineer definition of refactoring | 78% defined it as any change improving readability/maintainability |
> | Primary risk identified | 76% cited regression bugs |
> | Effect on module size | Refactoring increased LOC even while reducing complexity |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 278 — Q31

> [!question] Question
> If you could only choose one metric to track over time — Maintainability Index, SIG star rating, or Propagation Cost — which would you choose for a 10-year enterprise system, and why?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.2 Maintainability Index: Problems with a Single Number
>
> **What is it?**
> The Maintainability Index (MI) is a composite metric:
>
> $$MI = 171 - 5.2 \cdot \ln(V) - 0.23 \cdot G - 16.2 \cdot \ln(LOC)$$
>
> Where $V$ = Halstead Volume, $G$ = Cyclomatic Complexity, $LOC$ = Lines of Code.
>
> **Why it fails:**
>
> | Problem | Explanation |
> |---------|-------------|
> | Averaging hides skewness | 1 terrible module + 99 good ones = "good" MI |
> | Structure invisible | Module boundaries and dependencies are not captured |
> | Same MI, different designs | Compact spaghetti code can score the same as well-structured code |
> | Outdated components | Halstead Volume is rarely used in modern practice |
>
> **Concrete Example:**
> System A: 100 methods, all with CC=10 → MI = 72 ("moderate")
> System B: 95 methods with CC=3, 5 methods with CC=133 → same average, same MI = 72
> System B is far worse — those 5 methods are unmaintainable hotspots — but MI cannot distinguish the two.
>
> #### Star Rating Calibration
>
> Properties are rated on a 1-to-5 star scale, calibrated against SIG's benchmark repository so that the distribution reflects the full range of quality achieved by real-world systems :
>
> | Stars | Benchmark Percentile |
> |-------|---------------------|
> | 5 | Top 5% of systems |
> | 4 | Next 30% |
> | 3 | Next 30% |
> | 2 | Next 30% |
> | 1 | Bottom 5% |
>
> ![SIG star rating distribution calibrated against industry benchmark](chart-sig-stars.svg)
>
> **Certification threshold:** overall maintainability rating of at least 3 stars, with each sub-characteristic scoring at least 2 stars .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

### Card 279 — Q32

> [!question] Question
> The lecture says "DSM is a tool for insight, not a definitive measure." What could go wrong if a team treats propagation cost as a KPI and optimizes for it without considering other factors?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 6.5 Propagation Cost Limitations
>
> | Limitation | Why It Matters |
> |-----------|---------------|
> | Ignores dependency nature | Strong and weak dependencies treated equally |
> | No module cohesion | High cohesion within modules is invisible |
> | Vertical buses penalized | Libraries used by many modules inflate PC unfairly |
> | Cluster choice affects results | Different algorithms give different answers |
> | Binary dependencies only | Cannot distinguish API call from deep internal coupling |
>
> **Remember:** DSM is a tool for insight, not a definitive measure. Combine with code metrics (SIG) and change history (Geipel) for a complete picture.
>
> {: .exam-tip }
> > **Exam Tip:** When discussing PC limitations, always mention Geipel's concentration finding and Nord's weighted enhancement as partial solutions. This shows depth of understanding.
>
> #### 6.1 Propagation Cost Formula
>
> **What is it?**
> Propagation Cost (PC)  measures how far a change to one element ripples through the system.
>
> **Step 1:** Build the visibility matrix by summing powers of the DSM:
>
> $$V = \sum_{n=0}^{k} M^n = M^0 + M^1 + M^2 + \cdots$$
>
> - $M^0$ = Identity (element sees itself)
> - $M^1$ = DSM (direct dependencies, 1 hop)
> - $M^n$ = indirect dependencies ($n$ hops)
>
> **Step 2:** Binarize: $v_{ij} = 1$ if $V_{ij} > 0$ (element $j$ is reachable from $i$)
>
> **Step 3:** Calculate PC:
>
> $$PC = \frac{\sum_{j=1}^{N}\sum_{i=1}^{N} v_{ij}}{N^2}$$
>
> **Interpretation:** PC = 17% means a random change to one element affects approximately 17% of all elements on average. Lower PC = better modularity.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/maintainability/RQ_A10_MaintainabilityDSM.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/maintainability/RQ_A10_MaintainabilityDSM.md)

## Software Reliability (12)

### Card 280 — Q1: Fault → Error → Failure in Practice

> [!question] Question
> **Q1: Fault → Error → Failure in Practice**
>
> Choose **one** of the following real-world failures and trace it through the full fault → error → failure chain:
>
> - CrowdStrike 2024 (8.5M devices bricked)
> - Meta/Facebook 2021 (6-hour global outage)
> - Boeing 737 MAX (MCAS system, 346 deaths)
>
> For your chosen case: (a) identify the **fault** (what was wrong in the design/code), (b) describe the **error** (what incorrect internal state occurred), and (c) explain the **failure** (what users observed).

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.2 Fault → Error → Failure Chain
>
> The three terms form a causal chain — each causes the next:
>
> | Term | Definition | Observable? | Example |
> |------|------------|-------------|---------|
> | **Fault** | Defect in code (design fault) | No (dormant in code) | Off-by-one in loop bound |
> | **Error** | Incorrect internal state | No (internal to system) | Array index out of bounds |
> | **Failure** | Observable deviation from correct service | **Yes** (externally visible) | Application crash, wrong output |
>
> ```mermaid
> flowchart LR
>     F["🔧 Fault<br>(defect in code)"]
>     E["⚠️ Error<br>(incorrect state)"]
>     FL["💥 Failure<br>(observable deviation)"]
>     F -->|"activated by<br>input"| E
>     E -->|"propagates to<br>output"| FL
>     style F fill:#fff3cd,stroke:#ffc107,color:#282828
>     style E fill:#ffe0b2,stroke:#ff9800,color:#282828
>     style FL fill:#ffcdd2,stroke:#d32f2f,color:#282828
> ```
>
> **Concrete Example — Null Pointer Bug:**
>
> | Stage | What Happens |
> |-------|-------------|
> | **Fault** | Developer forgets to check `if (user != null)` before accessing `user.name` |
> | **Error** | When `user` is `null`, the program dereferences a null pointer — internal state is corrupted |
> | **Failure** | Application throws `NullPointerException`, user sees "500 Internal Server Error" |
>
> The fault was dormant in the code for months. It only became an error when a specific input (a deleted user) triggered the code path. The error became a failure when it propagated to the HTTP response.
>
> > **Key insight:** Only **failure** is externally observable. Verification finds faults (static). Testing observes failures (dynamic).
>
> {: .highlight }
> > **Exam Tip:** Be able to trace a given scenario through all three stages. "What is the fault? What is the error? What is the failure?" is a classic exam question.
>
> #### 1.5 Fault → Error → Failure: Case Analyses
>
> **CrowdStrike 2024**
>
> | Stage | What happened |
> |-------|--------------|
> | **Fault** | A content configuration file (Channel File 291) shipped by CrowdStrike's update mechanism contained malformed data — a logic error in the content validator allowed an invalid pattern to pass quality checks |
> | **Error** | The Falcon sensor kernel driver attempted to parse the malformed file at runtime; an out-of-bounds memory read produced an invalid internal state (corrupted pointer) inside the Windows kernel |
> | **Failure** | The kernel encountered an unrecoverable exception and issued a Blue Screen of Death; 8.5 million Windows hosts could not boot, affecting hospitals, airlines, banks, and broadcasters globally |
>
> **Reliability concept:** Common-mode failure — every host running the same sensor version failed simultaneously; redundant hardware provided no protection because all instances shared the identical fault.
>
> **Meta/Facebook 2021**
>
> | Stage | What happened |
> |-------|--------------|
> | **Fault** | A routine BGP (Border Gateway Protocol) configuration change contained an error that withdrew all of Facebook's BGP route advertisements — the command that should have been scoped to a subset of routers was applied globally |
> | **Error** | Facebook's backbone routers stopped announcing their IP prefixes to the internet; DNS servers that needed to reach Facebook's authoritative name servers became unreachable; internal tools used to diagnose and fix the problem also relied on the same network and went dark |
> | **Failure** | Facebook, Instagram, and WhatsApp became globally unreachable for ~6 hours; ~3.5 billion users could not connect; engineers had to physically travel to data centres to restore access because remote management was also cut off |
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/reliability/RQ_L08_Reliability.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/reliability/RQ_L08_Reliability.md)

### Card 281 — Q2: Hardware vs Software Reliability

> [!question] Question
> **Q2: Hardware vs Software Reliability**
>
> Explain why the "bathtub curve" (infant mortality → useful life → wear-out) applies to hardware but **not** to software.
>
> What does the software reliability curve look like instead, and why?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.3 Hardware vs Software Reliability
>
> | Aspect | Hardware | Software |
> |--------|----------|----------|
> | **Failure cause** | Physical wear-out + design | Design faults **only** |
> | **Failure curve** | Bathtub (infant mortality → useful life → wear-out) | Decreasing (bugs found and fixed over time) |
> | **Repair** | Replace physical components | Fix code (patch) |
> | **Redundancy** | Physical copies (2 power supplies) | N-version diversity (different implementations) |
> | **Aging** | Degrades over time | Does not degrade — same binary, same behavior |
> | **Environment** | Temperature, vibration, humidity | Input patterns, workload, timing |
>
> **The two failure curves** (see lecture slide 6):
> - **Hardware** follows the classic **bathtub curve**: high infant mortality → low steady-state (useful life) → rising wear-out.
> - **Software** has a **decreasing curve with sawtooth spikes**: failure rate drops as bugs are found, but each update reintroduces new faults (spike), then drops again. There is **no wear-out** — only design change.
>
> **Why this matters:** Because software doesn't wear out, all software failures are triggered by specific inputs that activate dormant design faults. This means **testing and operational profiles** (what inputs the system actually receives) are critical to predicting reliability.
>
> #### Failure Rate Over Time
>
> Hardware follows the classic "bathtub curve" — infant mortality, useful life, wear-out. Software has no wear-out phase; its failure rate changes only when the code changes:
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/reliability/RQ_L08_Reliability.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/reliability/RQ_L08_Reliability.md)

### Card 282 — Q3: Define FSC for a Scenario

> [!question] Question
> **Q3: Define FSC for a Scenario**
>
> You are the quality lead for a **hospital patient portal** that allows patients to view test results, book appointments, and message their doctors.
>
> Define a 4-class Failure Severity Classification for this system. For each class, provide:
> - The severity definition
> - A concrete failure example
> - Which FSC criterion you chose (cost, capability, or human life) and why

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Failure Severity Classification
>
> Not all failures are equal. Musa defines four criteria for classifying failure severity :
>
> | Criterion | What It Measures | Example |
> |-----------|-----------------|---------|
> | **Human life impact** | Risk to safety | Medical device malfunction |
> | **Cost impact** | Financial consequences | Transaction processing error |
> | **System capability impact** | Functional degradation | Loss of backup capability |
> | **Reputation/market share** | Business consequences | Visible outage for customers |
>
> Severity classes (typically 3-5 levels) determine how failures are weighted in reliability calculations. A system may have an acceptable failure intensity for minor failures but near-zero tolerance for safety-critical ones.
>
> #### 2.2 Three Classification Criteria
>
> #### By Cost
>
> | Class | Cost Impact | Example |
> |-------|-------------|---------|
> | 1 | > $100,000 | Major outage, data loss |
> | 2 | $10K–$100K | Significant service incident |
> | 3 | $1K–$10K | Minor incident, workaround exists |
> | 4 | < $1,000 | Negligible, cosmetic |
>
> Cost components include: operational cost, repair cost, loss of business, disruption, and reputation damage. **Rule of thumb:** Class 1 failure cost ≈ total development cost .
>
> #### By System Capability
>
> | Class | Impact | Example |
> |-------|--------|---------|
> | 1 | Basic service **interruption** | Database corruption, total outage |
> | 2 | Basic service **degradation** | Slow response, partial features |
> | 3 | Inconvenience, not deferrable | Feature unavailable, user blocked |
> | 4 | Minor effects, deferrable | Cosmetic issue, typo |
>
> #### By Human Life (Safety-Critical)
>
> | Class | Impact | Applicable Domains |
> |-------|--------|--------------------|
> | 1 | Possible **loss of life** | Aerospace (DO-178C), Automotive (ISO 26262) |
> | 2 | Severe injury or damage | Medical devices (IEC 62304) |
> | 3 | Minor injury | Nuclear (IEC 61513) |
> | 4 | Minor recoverable effects | General embedded systems |
>
> **Safety-critical:** Class 1 failures require the highest assurance levels — MC/DC coverage, formal verification, and independent assessment.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/reliability/RQ_L08_Reliability.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/reliability/RQ_L08_Reliability.md)

### Card 283 — Q4: Calculate FIO from Availability

> [!question] Question
> **Q4: Calculate FIO from Availability**
>
> A payment processing system requires **99.9% availability**. Average downtime per failure is **2 minutes** (0.033 hours).
>
> Using the **exact formula**, calculate:
> 1. The maximum allowed failure intensity (λ)
> 2. The MTTF
> 3. How many failures per month (720 hours) this allows

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.4 Availability and FIO — The Exact Formula Matters
>
> **Exact availability formula:**
>
> $$A = \frac{MTTF}{MTTF + MTTR}$$
>
> Solving for failure intensity:
>
> $$\lambda = \frac{1 - A}{A \times t_m}$$
>
> Where:
> - A = availability (fraction of uptime)
> - λ = failure intensity
> - t_m = mean downtime per failure (MTTR)
>
> **Linear approximation** (valid only when λ × t_m ≪ 1):
>
> $$A \approx 1 - \lambda \times t_m \quad \Rightarrow \quad \lambda \approx \frac{1-A}{t_m}$$
>
> **Worked Example — Why the Exact Formula Matters:**
>
> Given: A = 99% (0.99), t_m = 0.1 hr (6 minutes)
>
> | Formula | Calculation | Result |
> |---------|-------------|--------|
> | **Exact** | λ = 0.01 / (0.99 × 0.1) = 0.01 / 0.099 | **≈ 0.101 failures/hr** |
> | Approximation | λ ≈ 0.01 / 0.1 | ≈ 0.100 failures/hr |
>
> For this case, the approximation is close. But the exact formula gives **~10 failures per 100 hours**, which is the correct number to use in reliability planning.
>
> …
>
> #### Failure Intensity and the FIO
>
> **Failure intensity** λ(t) is the number of failures per unit time at time t — the fundamental reliability metric . Related measures:
>
> | Metric | Formula | Meaning |
> |--------|---------|---------|
> | **Failure intensity** | λ(t) | Failures per time unit at time t |
> | **Reliability** | R(t) = e^{-λt} | Probability of no failure in interval [0, t] (for constant λ) |
> | **MTTF** | 1/λ | Mean time to next failure |
> | **MTTR** | — | Mean time to repair after failure |
> | **Availability** | A = MTTF/(MTTF + MTTR) | Fraction of time system is operational |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/reliability/RQ_L08_Reliability.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/reliability/RQ_L08_Reliability.md)

### Card 284 — Q5: When Metrics Mislead

> [!question] Question
> **Q5: When Metrics Mislead**
>
> Explain a scenario where:
> 1. **Failure density** (failures per KLOC) makes a module look safe, but **failure intensity** reveals a serious problem
> 2. **Failure intensity** looks acceptable, but the system is actually unreliable for users

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.1 Failure Intensity vs Failure Density
>
> These are two ways of expressing the same underlying quality — one for users, one for developers :
>
> | Metric | Definition | Audience | Example |
> |--------|------------|----------|---------|
> | **Failure Intensity (λ)** | Failures per time/natural unit | End users | 5 failures/hour; 2 failures/1000 transactions |
> | **Failure Density** | Failures per KLOC or FP | Developers | 1 failure/KLOC; 0.2 failures/FP |
>
> **Why both matter:** A system with low failure density (few bugs per KLOC) can still have high failure intensity if the buggy code is on the critical path that handles 90% of requests.
>
> **Example from Fenton :** Measuring absolute failure count identified 5 problematic modules. Measuring failures per KLOC identified only 1 module — the smallest module had the highest defect density but fewest total defects.
>
> #### Failure Intensity and the FIO
>
> **Failure intensity** λ(t) is the number of failures per unit time at time t — the fundamental reliability metric . Related measures:
>
> | Metric | Formula | Meaning |
> |--------|---------|---------|
> | **Failure intensity** | λ(t) | Failures per time unit at time t |
> | **Reliability** | R(t) = e^{-λt} | Probability of no failure in interval [0, t] (for constant λ) |
> | **MTTF** | 1/λ | Mean time to next failure |
> | **MTTR** | — | Mean time to repair after failure |
> | **Availability** | A = MTTF/(MTTF + MTTR) | Fraction of time system is operational |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/reliability/RQ_L08_Reliability.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/reliability/RQ_L08_Reliability.md)

### Card 285 — Q6: Prevention vs Tolerance

> [!question] Question
> **Q6: Prevention vs Tolerance**
>
> Compare **fault prevention** and **fault tolerance** as strategies for meeting FIO.
>
> For each, explain: (a) when it is more cost-effective, (b) give a concrete software example, and (c) identify its main limitation.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.2 Fault Prevention
>
> **Activities:**
> - Requirements review, design review
> - Coding standards and style guides
> - Static analysis tools (linters, type checkers)
> - CASE tools with built-in checks
>
> **Effectiveness:** Measured as the proportion of faults prevented. Early detection is most cost-effective — a fault found in design costs 10-100× less to fix than one found in production.
>
> **Best Practices:**
> - Standards compliance (ISO 9001, CMMI)
> - Training and process improvement
> - Pair programming, code review culture
>
> > **Prevention is the most cost-effective strategy** — find defects before they become code.
>
> #### Software Fault Tolerance
>
> Fault tolerance is the ability to deliver correct service in the presence of active faults . For hardware, this means physical redundancy — spare components mask random failures. For software, identical copies contain identical bugs, so fault tolerance requires **design diversity**: independently developed alternatives that are unlikely to fail on the same inputs .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/reliability/RQ_L08_Reliability.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/reliability/RQ_L08_Reliability.md)

### Card 286 — Q7: Backward Recovery and the Domino Effect

> [!question] Question
> **Q7: Backward Recovery and the Domino Effect**
>
> Explain **backward recovery** and the **domino effect** using the following scenario:
>
> > Service A processes an order, sends a "ship item" message to Service B, then fails.
>
> What happens when Service A rolls back? Why is this called the "domino effect"? How would **forward recovery** handle this differently?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.5 Recovery: Backward vs Forward
>
> | Aspect | Backward Recovery | Forward Recovery |
> |--------|-------------------|------------------|
> | **Mechanism** | Roll back to saved checkpoint | Use redundancy to continue |
> | **Overhead** | Higher (checkpoints) | Lower (no state saving) |
> | **Generality** | More general | Less general |
> | **Real-time suitability** | Difficult | Better |
> | **Problem** | **Domino effect** | Requires redundant components |
>
> **The Domino Effect:** In systems with communicating processes, a rollback in one process can invalidate messages already sent to others, forcing them to roll back too — cascading rollbacks that can undo all work.
>
> ```mermaid
> flowchart LR
>     subgraph Process_A
>         A1["Checkpoint A1"] --> A2["Work"] --> A3["Send msg"] --> A4["Checkpoint A2"] --> A5["Failure! ❌"]
>     end
>     subgraph Process_B
>         B1["Checkpoint B1"] --> B2["Receive msg"] --> B3["Work"] --> B4["Must rollback! 🔙"]
>     end
>     A3 -->|"message"| B2
>     A5 -->|"rollback to A1"| A1
>     B4 -->|"rollback to B1<br>(domino effect)"| B1
>     style A5 fill:#d32f2f,stroke:#b71c1c,color:#fff
>     style B4 fill:#ffc107,stroke:#f57f17,color:#282828
> ```
>
> #### The Domino Effect
>
> In concurrent systems, recovery blocks face a cascading problem: if process P1 rolls back, any information P1 sent to process P2 after the checkpoint becomes suspect, potentially forcing P2 to roll back as well. This can cascade until all processes have lost all progress .
>
> ```mermaid
> sequenceDiagram
>     participant P1 as Process 1
>     participant P2 as Process 2
>     participant P3 as Process 3
>
>     Note over P1,P3: Normal execution
>     P1->>P1: 💾 Checkpoint
>     P2->>P2: 💾 Checkpoint
>     P1->>P2: message M1
>     P2->>P3: message M2 (depends on M1)
>     P1->>P1: ❌ Fault detected!
>     P1->>P1: ↩️ Rollback (M1 now invalid)
>     Note over P2: M1 was received after<br>P1's checkpoint → suspect!
>     P2->>P2: ↩️ Forced rollback
>     Note over P3: M2 was based on M1<br>→ also suspect!
>     P3->>P3: ↩️ Forced rollback
>     Note over P1,P3: 😱 All progress lost!
> ```
>
> **Modern solutions** to the domino effect:
> - **Idempotent operations** — safe to retry without side effects
> - **Saga patterns** — compensating transactions instead of rollback
> - **Event sourcing** — rebuild state from the event log

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/reliability/RQ_L08_Reliability.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/reliability/RQ_L08_Reliability.md)

### Card 287 — Q8: SRGM Release Decision

> [!question] Question
> **Q8: SRGM Release Decision**
>
> A system under test has the following Goel-Okumoto parameters:
> - a = 80 faults (total expected)
> - b = 0.03 per week (detection rate per fault)
>
> The FIO target is **1.0 failure per week**.
>
> 1. What is the initial failure intensity λ(0)?
> 2. After 20 weeks of testing, what is λ(20)?
> 3. How many total weeks of testing are needed to reach the FIO?
> 4. How many faults will have been found by release time?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.7 SRGMs: Predicting When You'll Reach Your FIO
>
> Software Reliability Growth Models (SRGMs) track how failure intensity decreases over time as testing finds and fixes bugs .
>
> **Goel-Okumoto NHPP Model (1979):**
>
> $$m(t) = a(1 - e^{-bt}) \qquad \text{cumulative faults found by time } t$$
>
> $$\lambda(t) = ab \cdot e^{-bt} \qquad \text{failure intensity (decreasing!)}$$
>
> **Parameters:**
> - $a$ = total expected faults in the software
> - $b$ = per-fault detection rate (probability of finding a given fault per time unit)
>
> **Worked Example:**
> - System: a = 50 faults, b = 0.05/week
> - Initial failure intensity: λ(0) = 50 × 0.05 = **2.5 failures/week**
> - FIO target: 0.5 failures/week
> - When does λ(t) cross FIO?
>
> Solve: $0.5 = 2.5 \cdot e^{-0.05t}$ → $e^{-0.05t} = 0.2$ → $t = -\ln(0.2)/0.05 \approx$ **32 weeks**
>
> …
>
> #### Goel-Okumoto NHPP Model
>
> The foundational SRGM  models cumulative failures as a Nonhomogeneous Poisson Process:
>
> | Component | Formula | Meaning |
> |-----------|---------|---------|
> | Mean value function | m(t) = a(1 - e^{-bt}) | Expected cumulative failures by time t |
> | Failure intensity | λ(t) = ab·e^{-bt} | Decreasing failure rate |
> | Parameters | a = total expected faults, b = per-fault detection rate | Estimated from failure data |
>
> The failure intensity decreases exponentially — the hallmark of **reliability growth**. As faults are found and fixed, the system becomes more reliable.
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/reliability/RQ_L08_Reliability.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/reliability/RQ_L08_Reliability.md)

### Card 288 — Q9: Why Independence Fails

> [!question] Question
> **Q9: Why Independence Fails**
>
> Knight & Leveson's 1986 experiment found **29× more coincident failures** than the independence assumption predicts.
>
> 1. Describe the experimental setup (what was tested, how many versions, how many test cases)
> 2. List the **three causes** of correlated failures they identified
> 3. Explain why this result is devastating for the theoretical reliability claims of N-version programming

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.4 Knight & Leveson 1986: The Independence Experiment
>
> This is **the most cited result** in software fault tolerance .
>
> **Setup:**
> - 27 independently developed versions of the same program
> - Same specification, same language (Pascal)
> - 1,000,000 randomized test cases
> - Statistical test: Are version failures independent?
>
> **Result:** Independence hypothesis **rejected at 99% confidence** (χ² test)
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "title": {
>     "text": "Knight & Leveson 1986: Coincident Failures",
>     "subtitle": "27 versions, 1,000,000 test cases",
>     "subtitleFontSize": 11,
>     "subtitleColor": "#666"
>   },
>   "width": 300,
>   "height": 220,
>   "data": {
>     "values": [
>       {"type": "Predicted\n(if independent)", "failures": 1.0},
>       {"type": "Observed", "failures": 29.0}
>     ]
>   },
>   "mark": {"type": "bar", "cornerRadiusTopLeft": 4, "cornerRadiusTopRight": 4, "width": 80},
>   "encoding": {
>     "x": {"field": "type", "type": "nominal", "axis": {"labelAngle": 0, "title": null, "labelFontSize": 13}},
>     "y": {"field": "failures", "type": "quantitative", "title": "Relative Coincident Failures"},
>     "color": {
>       "field": "type", "type": "nominal",
>       "scale": {"range": ["#c8e6c9", "#d32f2f"]},
>       "legend": null
>     }
>   },
>   "config": {
>     "font": "Tahoma, sans-serif",
>     "axis": {"labelFontSize": 12, "titleFontSize": 13},
>     "view": {"stroke": null}
>   }
> }
> ```
>
> **29× more coincident failures than independence would predict.**
>
> **Why do independently developed versions fail together?**
>
> …
>
> #### The Independence Problem
>
> The reliability gain from multi-version techniques depends on the assumption that versions **fail independently**. Knight and Leveson's landmark experiment (1986) tested this assumption directly :
>
> | Parameter | Value |
> |-----------|-------|
> | Versions | 27 independently developed |
> | Test cases | 1,000,000 randomly generated |
> | Application | Launch Interceptor Program (antimissile) |
> | Individual reliability | >99.9% per version |
> | **Result** | Independence rejected at **99% confidence** |
>
> Coincident failures — where multiple versions failed on the same input — were significantly more frequent than statistical independence would predict .
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "title": "Knight & Leveson (1986): Predicted vs Actual Coincident Failures",
>   "width": 450,
>   "height": 250,
>   "data": {
>     "values": [
>       {"category": "Expected if\nindependent", "failures": 0.2, "color": "Expected (independence)"},
>       {"category": "Observed\n(actual)", "failures": 5.8, "color": "Observed"}
>     ]
>   },
>   "mark": {"type": "bar", "width": 60},
>   "encoding": {
>     "x": {"field": "category", "type": "nominal", "title": null, "axis": {"labelAngle": 0}},
>     "y": {"field": "failures", "type": "quantitative", "title": "Avg. coincident failures per version pair"},
>     "color": {"field": "color", "type": "nominal", "title": null, "scale": {"range": ["#1565c0", "#d32f2f"]}}
>   }
> }
> ```
>
> {: .note }
> > If versions failed independently, coincident failures would be extremely rare (~0.2 per pair). The actual rate was ~29x higher — independence rejected at 99% confidence .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/reliability/RQ_L08_Reliability.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/reliability/RQ_L08_Reliability.md)

### Card 289 — Q10: Voting System Reliability

> [!question] Question
> **Q10: Voting System Reliability**
>
> Three independently developed versions have individual reliability R_c = 0.95.
>
> 1. Calculate the system reliability with **majority voting** (2-of-3)
> 2. Calculate the system reliability with a **single version** (no redundancy)
> 3. Now assume failures are NOT independent: 10% of failures are coincident (all 3 fail together). Re-estimate the effective system reliability.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Voting Mechanisms
>
> **Majority Voting:**
>
> $$m \geq \left\lceil\frac{N+1}{2}\right\rceil$$
>
> Where N = number of versions, m = required agreement count.
>
> **Example:** 3 versions → need 2 to agree. 5 versions → need 3 to agree.
>
> **Other Voting Schemes:**
>
> | Scheme | Rule | Best For |
> |--------|------|----------|
> | **Consensus** | Largest agreement group wins | When exact match is unlikely |
> | **2-of-N** | Any 2 agree | Large output spaces |
> | **Weighted** | Expertise-based weights | Versions with known quality differences |
> | **Median** | Middle value selected | Continuous numerical outputs |
>
> **System Reliability (Majority Voting):**
>
> $$R_{system} = \sum_{i=m}^{N} \binom{N}{i} R_c^i (1-R_c)^{N-i}$$
>
> **Worked Example — 3-of-5 Voting:**
>
> Given: R_c = 0.9 (each version has 90% reliability), N = 5, m = 3
>
> $$R_{system} = \binom{5}{3}(0.9)^3(0.1)^2 + \binom{5}{4}(0.9)^4(0.1)^1 + \binom{5}{5}(0.9)^5(0.1)^0$$
>
> $$= 10 \times 0.729 \times 0.01 + 5 \times 0.6561 \times 0.1 + 1 \times 0.59049 \times 1$$
>
> $$= 0.0729 + 0.3281 + 0.5905 = \mathbf{0.9914}$$
>
> **Result:** System reliability improves from 90% to **99.1%** — but only if failures are independent!
>
> #### Voting Strategies
>
> The choice of voter significantly affects system reliability :
>
> | Strategy | Mechanism | When to Use |
> |----------|-----------|-------------|
> | **Majority** | >50% agreement required (e.g., 2-of-3) | Discrete outputs, high reliability needed |
> | **Plurality** | Largest agreement group wins | More versions, no single majority expected |
> | **Weighted average** | Weights by variant trustworthiness | Continuous outputs, historical performance data |
> | **Median** | Central value from sorted outputs | Continuous outputs, outlier resistance |
> | **Consensus** | Generalized majority with unique maximum | Formal correctness requirement |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/reliability/RQ_L08_Reliability.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/reliability/RQ_L08_Reliability.md)

### Card 290 — Q11: Error Budget Calculation

> [!question] Question
> **Q11: Error Budget Calculation**
>
> A video streaming service has:
> - SLO: 99.95% availability
> - Monthly traffic: 50,000,000 requests
> - Current month's incidents: two outages totaling 8 minutes, plus a degraded-quality period causing 5,000 errors
>
> Calculate:
> 1. The monthly error budget (in requests and in minutes)
> 2. How much budget has been consumed
> 3. What action should the team take?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Worked Example: Error Budget for a Checkout Service
>
> A checkout service has **SLO = 99.9%** availability over a 30-day window:
>
> | Metric | Calculation | Value |
> |--------|-------------|-------|
> | Error budget | 100% - 99.9% | **0.1%** |
> | Total requests/month | 3,000,000 | — |
> | Allowed failures/month | 3,000,000 × 0.001 | **3,000 errors** |
> | Allowed downtime/month | 30 days × 0.001 | **43 minutes** |
>
> **Scenario:** A bad deployment causes 500 errors/hour for 2 hours = 1,000 errors.
>
> - Budget consumed: 1,000 / 3,000 = **33%** in one incident
> - Remaining budget: **2,000 errors** for the rest of the month
> - Action: Mandatory postmortem (>20% consumed), but no feature freeze yet
>
> #### 6.2 Error Budgets
>
> **Formula:**
>
> $$\text{Error Budget} = 1 - \text{SLO}$$
>
> The error budget quantifies **how much unreliability you can tolerate** before you must stop shipping and fix reliability .
>
> **Worked Example — Checkout Service:**
>
> | Metric | Calculation | Value |
> |--------|-------------|-------|
> | SLO | | 99.9% |
> | Error budget | 100% − 99.9% | **0.1%** |
> | Requests/month | | 3,000,000 |
> | Allowed failures | 3M × 0.001 | **3,000 errors** |
> | Allowed downtime | 30 days × 0.001 | **43 minutes** |
>
> **Incident Analysis:**
>
> A bad deploy causes 500 errors/hour for 2 hours = **1,000 errors**.
>
> | Question | Calculation | Result |
> |----------|-------------|--------|
> | Budget consumed | 1,000 / 3,000 | **33%** |
> | > 20% threshold? | Yes | → Mandatory postmortem |
> | Budget exhausted? | No (67% remaining) | → Continue shipping |
>
> ```mermaid
> flowchart TB
>     INC["Incident: 1,000 errors"] --> PCT["1,000 / 3,000 = 33% consumed"]
>     PCT --> D1{"> 20% consumed?"}
>     D1 -->|"Yes"| PM["🔍 Mandatory postmortem"]
>     D1 -->|"No"| LOG["📝 Log & monitor"]
>     PCT --> D2{"Budget exhausted?"}
>     D2 -->|"Yes"| FREEZE["🛑 Feature freeze"]
>     D2 -->|"No"| SHIP["🚀 Continue shipping"]
>     style FREEZE fill:#d32f2f,stroke:#b71c1c,color:#fff
>     style PM fill:#ffc107,stroke:#f57f17,color:#282828
>     style SHIP fill:#019546,stroke:#2D6E2A,color:#fff
>     style INC fill:#f0f8f0,stroke:#019546,color:#282828
>     style PCT fill:#f0f8f0,stroke:#019546,color:#282828
> ```
>
> **Mixed-Unit Incidents (outage time + failed requests):**
>
> When an incident report gives both downtime *and* a failed-request count, convert everything to requests using the traffic rate before adding:
>
> $$\text{Request rate} = \frac{\text{Total requests/month}}{\text{Minutes/month}}$$
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/reliability/RQ_L08_Reliability.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/reliability/RQ_L08_Reliability.md)

### Card 291 — Q12: FIO vs SLO — Same Concept, Different Phase

> [!question] Question
> **Q12: FIO vs SLO — Same Concept, Different Phase**
>
> Explain how Musa's Failure Intensity Objective (1990s) and Google's Service Level Objective (2010s) represent the **same fundamental concept** applied in different contexts.
>
> For each of the following pairs, explain the equivalence:
> 1. FIO ↔ SLO
> 2. Failure intensity λ(t) ↔ Error rate SLI
> 3. "Just right" reliability ↔ Error budget

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 6.1 FIO ≡ SLO: Same Concept, Different Phase
>
> Musa's Failure Intensity Objective (1990s) and Google's Service Level Objective (2010s) are fundamentally the same idea  :
>
> | Classical SRE (Musa) | Modern SRE (Google) | Same Concept |
> |------|------|------|
> | FIO | SLO | Target reliability — "good enough" |
> | Failure intensity λ(t) | Error rate (SLI) | What is measured |
> | Operational profile | Critical User Journeys | What to measure |
> | Severity classification | Service tiering | Not all failures equal |
> | Demonstration chart | Burn-rate alerting | Decision mechanism |
> | "Just right" reliability | Error budget (1 − SLO) | 100% is the wrong target |
>
> **Key difference:** FIO gates **release** (pre-production). SLO governs **production velocity** (post-release).
>
> ```mermaid
> flowchart TB
>     subgraph fio["FIO: Release Gate (1990s)"]
>         T["Test"] --> M["Measure λ(t)"]
>         M --> D{"λ ≤ FIO?"}
>         D -->|"Yes"| R["Release ✅"]
>         D -->|"No"| T
>     end
>     subgraph slo["SLO: Operational Loop (2010s)"]
>         P["Production"] --> MON["Monitor SLI"]
>         MON --> B{"Budget<br>left?"}
>         B -->|"Yes"| SHIP["Ship 🚀"]
>         SHIP --> P
>         B -->|"No"| FREEZE["Freeze 🛑"]
>         FREEZE --> P
>     end
>     style T fill:#f0f8f0,stroke:#019546,color:#282828
>     style M fill:#f0f8f0,stroke:#019546,color:#282828
>     style D fill:#fff3cd,stroke:#ffc107,color:#282828
>     style R fill:#019546,stroke:#2D6E2A,color:#fff
>     style P fill:#f0f8f0,stroke:#019546,color:#282828
>     style MON fill:#f0f8f0,stroke:#019546,color:#282828
>     style B fill:#fff3cd,stroke:#ffc107,color:#282828
>     style SHIP fill:#019546,stroke:#2D6E2A,color:#fff
>     style FREEZE fill:#d32f2f,stroke:#b71c1c,color:#fff
> ```
>
> #### From FIO to SLO: Classical Meets Modern Reliability
>
> Musa's Failure Intensity Objective (1993) and Google's Service Level Objective (2016) are conceptually the same idea: define "just right" reliability to balance quality against cost and velocity  . This page traces the conceptual continuity from classical software reliability engineering to modern SRE practice.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/reliability/RQ_L08_Reliability.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/reliability/RQ_L08_Reliability.md)

## Performance Analysis (14)

### Card 292 — Q1: Business Impact of Latency

> [!question] Question
> **Q1: Business Impact of Latency**
>
> A cloud-based e-commerce platform processes 50,000 orders per day with an average order value of $80. The platform's current average response time is 1.2 seconds.
>
> A proposed infrastructure upgrade would reduce response time to 0.4 seconds, but costs $200,000/year. Using the "100ms latency = 1% sales" rule of thumb:
>
> 1. Estimate the annual revenue impact of the 800ms improvement
> 2. Is the infrastructure investment justified?
> 3. What assumptions make this calculation unreliable?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.4 Utility Curves: Not All Response Times Have Equal Business Value
>
> Different applications have different tolerance curves for response time:
>
> | Application | Curve Shape | Explanation |
> |-------------|------------|-------------|
> | **Real-time trading** | Cliff — instant drop-off | Milliseconds matter, all or nothing |
> | **Streaming video** | Cliff at buffering threshold | Fine until buffer empties, then terrible |
> | **Web page** | Gradual decline | Progressively worse experience |
> | **Batch reporting** | Flat — tolerance is high | Overnight is fine |
>
> **Performance budget helps prioritize:** Optimize the component whose utility curve has the steepest cliff first.
>
> #### Practice Questions
>
> 1. A startup's web app has mean response time of 1.5 seconds. Their competitor responds in 0.8 seconds. Using the Amazon "100ms = 1% sales" rule of thumb, estimate the potential business impact of this difference.
> 2. Why is performance engineering (design-time) more cost-effective than performance testing (test-time)?
> 3. Which ISO 25010 sub-characteristic is most relevant for a video streaming service? For a batch payroll system?

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/performance/RQ_L09_PerformanceAnalysis.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/performance/RQ_L09_PerformanceAnalysis.md)

### Card 293 — Q2: Performance Engineering vs Testing

> [!question] Question
> **Q2: Performance Engineering vs Testing**
>
> Explain why finding a performance problem during the **design phase** costs 10–100× less than finding it in **production**. Give a concrete example of a performance issue that:
>
> (a) Could have been caught during design review
> (b) Was only discovered under production load
> (c) Required architectural redesign to fix

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.3 Performance Engineering vs Performance Testing
>
> A critical distinction: performance testing is **reactive** (find problems after they exist), while performance engineering is **proactive** (prevent problems before they exist) :
>
> | Approach | When | Goal | Cost |
> |----------|------|------|------|
> | **Performance Engineering** | Requirements → Design | Predict and prevent | Low |
> | **Performance Testing** | Integration → Release | Detect and fix | Medium–High |
> | **Performance Firefighting** | Production | React and repair | Very High |
>
> ```mermaid
> flowchart LR
>     PE["Performance<br>Engineering<br>(Design time)"]
>     PT["Performance<br>Testing<br>(Test time)"]
>     FF["Firefighting<br>(Production)"]
>     PE -->|"predict"| PT
>     PT -->|"validate"| FF
>     style PE fill:#c8e6c9,stroke:#019546,color:#282828
>     style PT fill:#fff3cd,stroke:#ffc107,color:#282828
>     style FF fill:#ffcdd2,stroke:#d32f2f,color:#282828
> ```
>
> **Key insight:** Moving from reactive firefighting to proactive engineering reduces production defect escape from **30% to 5%** — a 6× improvement .
>
> #### Performance Anti-Patterns Are Architectural
>
> Performance problems are often not code-level bugs but **design-level anti-patterns** that require architectural refactoring :
>
> | Anti-Pattern | Problem | Impact |
> |-------------|---------|--------|
> | **God Class** | One controller does all work | 2&times; message traffic vs refactored design |
> | **Circuitous Treasure Hunt** | Long chains of object calls | 4,000 unnecessary DB calls |
> | **One-Lane Bridge** | Low-bandwidth path where high-bandwidth needed | Serialized bottleneck |
> | **Excessive Dynamic Allocation** | Frequent object create/destroy | GC overhead, latency spikes |
>
> These anti-patterns cannot be fixed by "tuning" — they require redesign . This is why Smith and Williams advocate for **Software Performance Engineering (SPE)**: predictive modeling during the design phase, before code is written .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/performance/RQ_L09_PerformanceAnalysis.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/performance/RQ_L09_PerformanceAnalysis.md)

### Card 294 — Q3: Little's Law — Cloud Service

> [!question] Question
> **Q3: Little's Law — Cloud Service**
>
> A Kubernetes deployment shows the following metrics during peak hour:
> - Average active pod connections: **250**
> - Average response time: **125 milliseconds**
>
> 1. Calculate the throughput (requests per second)
> 2. The SRE team wants to reduce response time to 80ms without changing throughput. How many concurrent connections will the system handle?
> 3. If the team adds a caching layer that reduces response time by 40%, what happens to concurrency at the same throughput? Explain using Little's Law.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.2 Little's Law: Cloud Service Example
>
> **Scenario:** Your cloud load balancer dashboard shows **100 active connections** and average response time is **200 milliseconds**. What is your throughput?
>
> **Solution:**
>
> $$\lambda = \frac{L}{W} = \frac{100}{0.2\text{s}} = 500 \text{ requests per second}$$
>
> **Reverse scenarios:**
>
> | Known | Unknown | Calculation | Result |
> |-------|---------|-------------|--------|
> | λ = 500 rps, W = 0.2s | L | L = 500 × 0.2 | **100 concurrent** |
> | L = 100, λ = 500 rps | W | W = 100 / 500 | **0.2s response** |
> | L = 100, W = 0.2s | λ | λ = 100 / 0.2 | **500 rps** |
>
> **More examples of Little's Law in action:**
>
> | System | Known Values | Derived |
> |--------|-------------|---------|
> | Wine cellar | L=160 bottles, λ=96 bought/year | W = 160/96 = **1.67 years** aging |
> | Hospital ward | λ=5 births/day, W=2.5 days stay | L = 5×2.5 = **12.5 beds needed** |
> | Semiconductor fab | λ=1000 wafers/day, L=45000 WIP | W = 45000/1000 = **45 day cycle time** |
>
> {: .highlight }
> > **Exam Tip:** Little's Law is the single most important equation in performance analysis. Be ready to apply it in any direction (given any two, derive the third) and in any domain (not just computer systems).
>
> #### Practice Questions
>
> 1. A microservice shows L=200 concurrent requests and λ=1000 rps. What is the average response time? If the team wants to reduce response time to 100ms, how many concurrent requests will the system handle at the same throughput?
> 2. System A has mean response time 2s with p99 at 2.5s. System B has mean response time 2s with p99 at 15s. Which system would you prefer for an e-commerce checkout? Why?
> 3. A system currently operates in the Heavy Load zone. What will happen if traffic increases by 50%? What actions could prevent entering the Buckle Zone?

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/performance/RQ_L09_PerformanceAnalysis.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/performance/RQ_L09_PerformanceAnalysis.md)

### Card 295 — Q4: Percentiles vs Averages

> [!question] Question
> **Q4: Percentiles vs Averages**
>
> Two API endpoints both report **mean response time = 500ms**:
>
> - **Endpoint A:** p50 = 450ms, p90 = 550ms, p99 = 600ms
> - **Endpoint B:** p50 = 100ms, p90 = 200ms, p99 = **8000ms**
>
> 1. Which endpoint provides a better user experience for the majority of users?
> 2. Which endpoint is more problematic from an SLA perspective (SLA: p99 < 1000ms)?
> 3. Wilson recommends reporting the 90th percentile instead of the mean. How would this change the team's priorities?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.3 Percentiles vs Averages: Why Mean Lies
>
> Performance data is **fundamentally non-normal** — it has long right tails :
>
> **Two systems with identical mean response time of 1 second:**
>
> | Scenario | Distribution | User Experience |
> |----------|-------------|-----------------|
> | **Good** | All requests between 0.8s and 1.2s | Consistent, predictable |
> | **Terrible** | 90% at 0.5s, 10% at 5.5s | Most fast, some furious |
>
> Both have mean = 1s, but user experience is completely different. This is why **percentiles** beat averages :
>
> | Percentile | What It Measures | Use Case |
> |-----------|------------------|----------|
> | **p50 (median)** | Typical user | General health check |
> | **p90** | "What most users perceive" | Primary reporting metric |
> | **p99** | Tail latency | SLA targets |
> | **p99.9** | Extreme tail | Large-scale systems (Google, Amazon) |
>
> **Wilson's recommendation:** Report the **90th percentile** as the primary metric, not the mean .
>
> **The Rule of 8:** Human productivity drops dramatically when system response times exceed **8 seconds** — users lose their train of thought, context-switch, or abandon entirely.
>
> **Practical thresholds for bottleneck detection:**
>
> | Resource | Warning Threshold |
> |----------|-------------------|
> | CPU utilization | >70% average or run queue >2/processor |
> | Disk utilization | >20% |
> | Response change | <10% may be noise, not real improvement |
>
> #### Percentile Guidelines
>
> | Metric | Use Case |
> |--------|---------|
> | **p50 (median)** | Typical user experience |
> | **p90** | "What most users actually perceive"  |
> | **p99** | Tail latency — important for SLAs |
> | **p99.9** | Critical for large-scale systems  |
>
> Wilson recommends the **90th percentile** over the mean as the primary reporting metric, and identifies practical thresholds :
>
> | Resource | Bottleneck Threshold |
> |----------|---------------------|
> | CPU utilization | >70% average or queue >2/processor |
> | Disk utilization | >20% |
> | Performance change | <10% may be noise, not real improvement |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/performance/RQ_L09_PerformanceAnalysis.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/performance/RQ_L09_PerformanceAnalysis.md)

### Card 296 — Q5: Hockey Stick Curve — Three Zones

> [!question] Question
> **Q5: Hockey Stick Curve — Three Zones**
>
> Sketch the hockey stick curve (from memory) with all three metrics (U, X, R) and the three zones (Light Load, Heavy Load, Buckle Zone).
>
> For each zone, explain:
> 1. What happens to **Utilization** (U)?
> 2. What happens to **Throughput** (X)?
> 3. What happens to **Response Time** (R)?
> 4. What is the user experience like?
>
> What happens if you add a faster CPU? Draw how the curve shifts.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.4 The Hockey Stick Curve: Three Zones Under Load
>
> When load increases, a system passes through three distinct zones :
>
> …
>
> #### Queuing Theory: The Hockey Stick Curve
>
> When utilization increases, response time follows a characteristic **hockey stick** shape — flat at low load, then climbing exponentially :
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/performance/RQ_L09_PerformanceAnalysis.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/performance/RQ_L09_PerformanceAnalysis.md)

### Card 297 — Q6: Amdahl's Law — Optimization Decision

> [!question] Question
> **Q6: Amdahl's Law — Optimization Decision**
>
> Your application profile shows:
> - Database queries: 45% of execution time
> - Business logic: 35% of execution time
> - Network I/O: 20% of execution time
>
> A new database index would make queries **3× faster** (q = 3).
>
> 1. Calculate the overall speedup using Amdahl's Law
> 2. What is the maximum possible speedup even with infinitely fast queries?
> 3. A colleague suggests also optimizing network I/O to be 2× faster. If both optimizations are applied, what is the combined speedup?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.2 Amdahl's Law: Worked Example
>
> **Problem:** You optimize a sorting algorithm that accounts for 60% of your application's critical path. The optimization makes the sort 35% faster (q = 1.35). What is the overall speedup?
>
> **Solution:**
> - α = 0.6 (fraction affected)
> - q = 1.35 (speedup of improved part)
> - (1 − α) = 0.4 (unaffected fraction)
>
> $$S = \frac{1}{0.4 + \frac{0.6}{1.35}} = \frac{1}{0.4 + 0.444} = \frac{1}{0.844} = \mathbf{1.185}$$
>
> **Result:** A 35% improvement in 60% of the code yields only **18.5% overall improvement**.
>
> **Practical implications:**
>
> 1. **Profile first** — find actual hotspots (where α is large)
> 2. **Measure α** — what fraction of time does this code represent?
> 3. **Calculate max gain** — is the optimization effort worthwhile?
> 4. **Optimize the common case** — not cold code
>
> ```mermaid
> flowchart LR
>     P["Profile"] --> M["Measure α"]
>     M --> C{"α large<br>enough?"}
>     C -->|"Yes"| O["Optimize (q)"]
>     C -->|"No"| S["Skip — low impact"]
>     O --> V["Verify S = 1/((1-α)+α/q)"]
>     style P fill:#c8e6c9,stroke:#019546,color:#282828
>     style C fill:#fff3cd,stroke:#ffc107,color:#282828
>     style S fill:#ffcdd2,stroke:#d32f2f,color:#282828
>     style O fill:#c8e6c9,stroke:#019546,color:#282828
> ```
>
> {: .highlight }
> > **Anti-pattern:** Micro-optimizing code that runs 1% of the time. Even a 10× improvement in that code gives only 0.9% overall speedup.
>
> #### 3.1 Amdahl's Law: The Serial Fraction Ceiling (1967)
>
> **The fundamental question:** If you speed up part of a system, how much does the *whole* system improve?
>
> **Amdahl's Law** :
>
> $$S = \frac{1}{(1 - \alpha) + \frac{\alpha}{q}}$$
>
> | Symbol | Meaning | Example |
> |--------|---------|---------|
> | **S** | Overall speedup | How much faster the whole system gets |
> | **α** | Fraction affected | Percentage of execution that benefits |
> | **q** | Speedup of improved part | How much faster that part becomes |
>
> **Ceiling:** When q → ∞ (infinite speedup of the improved part):
>
> $$S_{max} = \frac{1}{1 - \alpha} = \frac{1}{f}$$
>
> where f is the **serial fraction** (the part that cannot be parallelized).
>
> **Implications:**
>
> | Serial Fraction (f) | Max Speedup | Even with ∞ processors |
> |---------------------|-------------|------------------------|
> | 50% | 2× | Can never exceed 2× |
> | 10% | 10× | Can never exceed 10× |
> | 5% | 20× | Can never exceed 20× |
> | 1% | 100× | Can never exceed 100× |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/performance/RQ_L09_PerformanceAnalysis.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/performance/RQ_L09_PerformanceAnalysis.md)

### Card 298 — Q7: Gustafson vs Amdahl — When Each Applies

> [!question] Question
> **Q7: Gustafson vs Amdahl — When Each Applies**
>
> A data science team runs machine learning training jobs. Their pipeline has two phases:
> - **Data loading** (serial): 10 minutes, cannot be parallelized
> - **Model training** (parallel): 50 minutes on 1 GPU
>
> 1. Using Amdahl's Law with 10 GPUs, what is the expected training time?
> 2. Under Gustafson's assumption, what could the team accomplish with 10 GPUs in the original 60-minute window?
> 3. Which law is more appropriate for this scenario and why?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.3 Gustafson's Law: Scale the Problem, Not the Time (1988)
>
> Amdahl assumes a **fixed problem size** — but real users often **scale the problem** with more processors :
>
> | | Amdahl | Gustafson |
> |-|--------|-----------|
> | **Assumption** | Fixed problem size | Fixed execution time |
> | **Serial work** | Stays constant | Stays constant |
> | **Parallel work** | Stays constant | **Grows with N** |
> | **Outlook** | Pessimistic (ceiling) | Optimistic (near-linear) |
> | **Use when** | Latency-bound (single request) | Throughput-bound (batch processing) |
>
> **Gustafson's key result:** On **1024 processors**, he measured **1016–1021× speedup** — near-linear scaling!
>
> **Example: Weather Simulation**
>
> | Processors | Problem Size | Serial Work | Parallel Work | Time |
> |-----------|-------------|-------------|---------------|------|
> | 1 | Small grid | 5 min | 55 min | 60 min |
> | 100 | **Large grid** | 5 min | 55 min | **60 min** |
>
> With 100 processors, you don't compute the same grid 100× faster — you compute a **100× finer grid** in the same time. The serial work (initialization, I/O) stays fixed, but the parallel work (computation) scales with processor count.
>
> {: .highlight }
> > **Exam Tip:** Know when to apply each law. Amdahl: "How much faster can this single task run?" (latency). Gustafson: "How much more work can we do in the same time?" (throughput).
>
> #### 3.1 Amdahl's Law: The Serial Fraction Ceiling (1967)
>
> **The fundamental question:** If you speed up part of a system, how much does the *whole* system improve?
>
> **Amdahl's Law** :
>
> $$S = \frac{1}{(1 - \alpha) + \frac{\alpha}{q}}$$
>
> | Symbol | Meaning | Example |
> |--------|---------|---------|
> | **S** | Overall speedup | How much faster the whole system gets |
> | **α** | Fraction affected | Percentage of execution that benefits |
> | **q** | Speedup of improved part | How much faster that part becomes |
>
> **Ceiling:** When q → ∞ (infinite speedup of the improved part):
>
> $$S_{max} = \frac{1}{1 - \alpha} = \frac{1}{f}$$
>
> where f is the **serial fraction** (the part that cannot be parallelized).
>
> **Implications:**
>
> | Serial Fraction (f) | Max Speedup | Even with ∞ processors |
> |---------------------|-------------|------------------------|
> | 50% | 2× | Can never exceed 2× |
> | 10% | 10× | Can never exceed 10× |
> | 5% | 20× | Can never exceed 20× |
> | 1% | 100× | Can never exceed 100× |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/performance/RQ_L09_PerformanceAnalysis.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/performance/RQ_L09_PerformanceAnalysis.md)

### Card 299 — Q8: USL — Diagnosing Retrograde Throughput

> [!question] Question
> **Q8: USL — Diagnosing Retrograde Throughput**
>
> A microservice cluster shows the following throughput measurements:
>
> | Instances | Throughput (rps) |
> |-----------|-----------------|
> | 1 | 100 |
> | 2 | 185 |
> | 4 | 330 |
> | 8 | 500 |
> | 16 | 450 |
> | 32 | 320 |
>
> 1. What USL parameter (α or β) is likely causing the degradation?
> 2. Explain physically what is happening as instances increase beyond 8
> 3. What architectural change would you propose to address this?
> 4. Why does simply "adding more servers" make the problem worse?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.4 Universal Scalability Law (USL): Why Adding Servers Can Make Things Worse (2002)
>
> The USL extends Amdahl's Law by adding **coherence costs** — the overhead of keeping data consistent across processors :
>
> $$S(N) = \frac{N}{1 + \alpha(N-1) + \beta N(N-1)}$$
>
> | Parameter | Physical Meaning | Growth | Example |
> |-----------|-----------------|--------|---------|
> | **α** (contention) | Waiting for shared resources | Linear with N | Database locks, message queues |
> | **β** (coherence) | Maintaining global consistency | **Quadratic** with N | Cache invalidation, distributed consensus |
>
> **Three scalability regimes:**
>
> ```mermaid
> graph LR
>     A["Amdahl<br>(β = 0)<br>Plateau only"]
>     G["Gustafson<br>Scaled speedup<br>Near-linear"]
>     U["USL<br>(β > 0)<br>Peak + degradation"]
>     A -->|"Fixed problem"| G
>     A -->|"Add coherence"| U
>     style A fill:#4CAF50,color:#fff
>     style G fill:#2196F3,color:#fff
>     style U fill:#d32f2f,color:#fff
> ```
>
> **When β = 0:** USL reduces to Amdahl's Law (plateau only).
> **When β > 0:** The system **degrades beyond a peak** — adding more servers actually makes performance *worse*. This is called **retrograde throughput**.
>
> **Why retrograde throughput happens:** When you add the 101st server to a distributed cache, the cache invalidation traffic (which grows as N²) can overwhelm the benefit of the extra compute capacity. At some point, the coherence overhead exceeds the marginal throughput gain.
>
> #### Amdahl's Law in the Cloud: The USL Connection
>
> The Universal Scalability Law  explains why "just add more servers" doesn't always work:
>
> **S(N) = N / [1 + &alpha;(N&minus;1) + &beta;N(N&minus;1)]**
>
> In cloud architectures:
>
> | USL Parameter | Cloud Manifestation |
> |---------------|-------------------|
> | **&alpha; (contention)** | Shared databases, message queues, API gateways |
> | **&beta; (coherence)** | Distributed cache invalidation, consensus protocols, cross-service transactions |
>
> The coherence term &beta;N(N&minus;1) grows **quadratically** — explaining why adding servers beyond a certain point causes **retrograde throughput**: the system gets slower, not faster .
>
> > "Bottlenecks are more likely to arise in the application software than in the hardware. So throwing more hardware at a performance problem might not necessarily help." — Gunther

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/performance/RQ_L09_PerformanceAnalysis.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/performance/RQ_L09_PerformanceAnalysis.md)

### Card 300 — Q9: Identify the Anti-Pattern

> [!question] Question
> **Q9: Identify the Anti-Pattern**
>
> For each scenario, identify the performance anti-pattern and propose a fix:
>
> **(a)** A REST API endpoint calls the database once to get a list of 100 user IDs, then makes 100 separate database calls to get each user's profile. Response time is 3 seconds.
>
> **(b)** A single "OrderService" microservice handles order creation, payment processing, inventory management, shipping, and email notifications. During peak load, payment processing latency causes all other operations to queue.
>
> **(c)** An application creates and destroys database connection objects for every request. During a load test, garbage collection pauses cause 2-second latency spikes every 30 seconds.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.5 Practical USL Application
>
> Gunther demonstrates that as few as **4 load test data points** suffice to determine α and β via regression :
>
> 1. Run load tests at 1, 2, 4, 8 servers
> 2. Measure throughput at each level
> 3. Fit the USL equation to find α and β
> 4. Predict the entire scalability curve — including the peak
>
> **Cloud manifestation of USL:**
>
> | USL Parameter | Cloud Equivalent |
> |---------------|-----------------|
> | **α** (contention) | Shared DBs, message queues, API gateways |
> | **β** (coherence) | Distributed cache invalidation, consensus protocols |
>
> **Capacity doubling time:** T_double = ln(2)/λ. For hypergrowth web services: ~6 months.
>
> > "Bottlenecks are more likely to arise in the application software than in the hardware. So throwing more hardware at a performance problem might not necessarily help." — Gunther
>
> #### 4.2 Performance Anti-Patterns
>
> Smith and Williams identified design-level anti-patterns that **cannot be fixed by tuning** — they require architectural redesign :
>
> | Anti-Pattern | What Goes Wrong | Measured Impact |
> |-------------|-----------------|-----------------|
> | **God Class** → *God Service* | One controller does all work | **2× message traffic** vs refactored design |
> | **Circuitous Treasure Hunt** → *Chatty N+1* | Long chains of calls to find data | **4,000 unnecessary DB calls** |
> | **One-Lane Bridge** → *Unsharded DB* | Serial bottleneck where high bandwidth is needed | All requests serialize |
> | **Excessive Dynamic Allocation** → *Cold starts* | Frequent create/destroy cycles | GC overhead, latency spikes |
>
> **The cloud-native evolution:** Each classical anti-pattern has a modern equivalent. God Class becomes God Service (one microservice does everything). Circuitous Treasure Hunt becomes the chatty N+1 query pattern. The underlying principle is the same: poor decomposition causes excessive communication.
>
> {: .highlight }
> > **Key insight:** These are **design-level** problems, not code-level bugs. Profiling and tuning won't help — you must **redesign**. This is why performance engineering must start at the architecture phase.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/performance/RQ_L09_PerformanceAnalysis.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/performance/RQ_L09_PerformanceAnalysis.md)

### Card 301 — Q10: Performance Bug Discovery

> [!question] Question
> **Q10: Performance Bug Discovery**
>
> Jin et al. (2012) found that **67% of performance bugs** are caused by wrong understanding of workload or API, and that profiling discovers only **5–10%** of performance bugs.
>
> 1. Why is profiling such a poor method for discovering performance bugs?
> 2. What method discovers the majority (33–57%) of performance bugs?
> 3. How would you incorporate this finding into your team's code review process?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.3 Empirical Evidence: Performance Bugs
>
> Research reveals consistent patterns about how performance bugs are found and (not) fixed:
>
> **Root causes (Jin et al., 2012)** :
>
> A study of 109 performance bugs from Apache, Chrome, GCC, Mozilla, and MySQL:
>
> | Finding | Value |
> |---------|-------|
> | Wrong understanding of workload or API | **67%** of bugs |
> | Bugs in input-dependent loops | **>75%** |
> | Median patch size | **8 lines of code** |
> | Patches with reusable detection rules | **46%** |
>
> **How developers discover performance bugs (Nistor et al., 2013)** :
>
> | Discovery Method | Performance Bugs | Non-Performance Bugs |
> |-----------------|-----------------|---------------------|
> | **Code reasoning** (reading + thinking) | **33–57%** | 5–16% |
> | Observing slowness | 30–49% | 85–95% |
> | **Profiling** | **5–10%** | — |
> | Regression tests | 2–9% | — |
>
> **The neglect gap (Zaman et al., 2011)** :
>
> Comparing security vs performance bugs in Firefox:
> - Security bugs triaged **3.64× faster**
> - Security bugs fixed **2.8× faster**
> - Performance bugs touch **2.6× more files** per fix
> - **62% of performance bugs never assigned** a developer
>
> {: .highlight }
> > **Exam Tip:** The surprise finding: **profiling discovers only 5–10%** of performance bugs. **Code reasoning** (reading and thinking about code) discovers 33–57%. This means code review for performance patterns is more effective than runtime measurement alone.
>
> #### Performance Bug Characteristics
>
> Understanding how performance bugs behave helps design better tests:
>
> | Characteristic | Value | Source |
> |---------------|-------|--------|
> | Root cause: wrong workload/API understanding | 67% |  |
> | Bugs in input-dependent loops | >75% |  |
> | Discovered by code reasoning (not profiling) | 33–57% |  |
> | Reports without reproduction steps | 54–73% |  |
> | Reports with measurements (CPU, I/O) | 34–36% |  |
> | Performance regressions vs non-perf (Chrome) | 7&times; more frequent |  |
>
> {: .note }
> > Profiling finds only 5–10% of performance bugs . **Code reasoning** — reading and thinking about code — is the primary discovery method. Testing strategies should include code review focused on performance patterns, not just runtime measurement.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/performance/RQ_L09_PerformanceAnalysis.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/performance/RQ_L09_PerformanceAnalysis.md)

### Card 302 — Q11: Test Strategy Design

> [!question] Question
> **Q11: Test Strategy Design**
>
> You are launching a ticket sales platform for a major concert. Expected traffic:
> - Normal: 5,000 concurrent users
> - On-sale moment: 200,000 concurrent users (40× spike in first 60 seconds)
> - Duration: 2-hour sale window
>
> Design a performance test strategy:
> 1. Which of the 6 test types would you use, and in what order?
> 2. What specific metrics would you monitor?
> 3. What does "realistic workload" mean for this scenario?
> 4. What is the risk if you only run a Load test but skip Stress and Soak tests?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.2 Six Types of Performance Tests
>
> Each test type answers different questions :
>
> | Test Type | Purpose | Load Level | When to Use |
> |-----------|---------|------------|-------------|
> | **Baseline** | Establish best-case response | Minimal (1 user) | Before any load testing |
> | **Load** | Verify SLA under expected traffic | Expected peak | Every release |
> | **Stress** | Find the breaking point | Beyond capacity | Capacity planning |
> | **Soak / Stability** | Reveal memory leaks, slow degradation | Sustained normal | Before production |
> | **Smoke** | Quick sanity check of changes | Changed code only | After each build |
> | **Isolation** | Diagnose specific transactions | Repeated single | Debugging known issues |
>
> ```mermaid
> flowchart TD
>     BL["Baseline<br>(1 user)"]
>     SM["Smoke<br>(quick check)"]
>     LD["Load<br>(expected traffic)"]
>     SK["Soak<br>(hours/days)"]
>     ST["Stress<br>(beyond capacity)"]
>     IS["Isolation<br>(single transaction)"]
>     BL -->|"Establish reference"| SM
>     SM -->|"Pass → full test"| LD
>     LD -->|"SLA met → endurance"| SK
>     LD -->|"SLA met → limits"| ST
>     ST -->|"Problem found"| IS
>     SK -->|"Leak found"| IS
>     style BL fill:#c8e6c9,stroke:#019546,color:#282828
>     style SM fill:#c8e6c9,stroke:#019546,color:#282828
>     style LD fill:#fff3cd,stroke:#ffc107,color:#282828
>     style SK fill:#fff3cd,stroke:#ffc107,color:#282828
>     style ST fill:#ffcdd2,stroke:#d32f2f,color:#282828
>     style IS fill:#bbdefb,stroke:#1976d2,color:#282828
> ```
>
> #### Six Types of Performance Tests
>
> Each test type serves a distinct purpose :
>
> | Type | Purpose | When to Use |
> |------|---------|-------------|
> | **Baseline** | Single user, empty system — establish comparison point | Before any load testing |
> | **Load** | Target concurrency to verify SLA compliance | Every release |
> | **Stress** | Overwhelm resources to find the "buckle point" | Capacity planning |
> | **Soak / Stability** | Extended duration to reveal memory leaks and slow degradation | Before production |
> | **Smoke** | Quick check of changed code only | After each build |
> | **Isolation** | Repeated execution of specific transactions | Diagnosing known issues |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/performance/RQ_L09_PerformanceAnalysis.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/performance/RQ_L09_PerformanceAnalysis.md)

### Card 303 — Q12: Tail Latency Calculation

> [!question] Question
> **Q12: Tail Latency Calculation**
>
> A search service fans out each user query to **80 backend shards**. Each shard has a 0.5% probability of responding slowly (>200ms).
>
> 1. Calculate the probability that a user query hits at least one slow shard
> 2. If the team implements **tied requests** (sending each sub-request to 2 shards simultaneously, cancelling the slower reply), what is the new probability of a slow response per sub-request?
> 3. What is the total cost in terms of additional traffic?
> 4. How would true **hedged requests** (delayed backup only issued after the 95th-percentile threshold) differ in traffic overhead, and why?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 6.3 Tail-Tolerant Techniques
>
> Dean and Barroso propose solutions that **tolerate** tail latency rather than trying to eliminate it :
>
> | Technique | How It Works | Result |
> |-----------|-------------|--------|
> | **Hedged requests** | Send to server 1; if no reply within the 95th-percentile threshold, send a delayed backup to server 2; cancel the slower one when either replies | p99.9: 1800ms → **74ms** (+2% traffic) |
> | **Tied requests** | Send to 2 servers simultaneously, cancel the slower one | Median −21%, p99 −38% |
> | **"Good enough"** responses | Return partial results from fast servers | Graceful degradation |
>
> ```mermaid
> sequenceDiagram
>     participant C as Client
>     participant S1 as Server 1
>     participant S2 as Server 2 (backup)
>     C->>S1: Request (t=0)
>     Note over C: Wait for 95th-pct threshold
>     C->>S2: Backup request (t=threshold, ~5% of requests only)
>     S2-->>C: Fast reply ✅ (cancel S1)
> ```
>
> **Why hedged requests are so effective — and why overhead is only +2%:** The backup request is *delayed*, not simultaneous. It is only issued if the first server has not replied within the 95th-percentile expected latency. Because ~95% of requests complete before that threshold, only ~5% ever trigger the backup — and those often cancel quickly once one reply arrives. Unconditional duplication to two servers simultaneously would cost ~100% extra traffic; the delayed backup design reduces that to ~2%. You're not making the slow server faster — you're giving the slow tail a second chance to hit a fast one.
>
> #### Practice Questions
>
> 1. A microservice request fans out to 50 backend services. Each service has a 2% chance of responding slowly (>500ms). What is the probability that the user experiences a slow response? What technique would you use to mitigate this?
> 2. Why are hedged requests so effective despite adding only 2% more traffic? Under what conditions would hedged requests NOT help?
> 3. A team wants to implement per-service SLOs. Their call chain is A → B → C, with total SLO of p99 < 300ms. How would you allocate the budget? What happens when Service B consistently uses 150ms?
> 4. Bezemer found 88% of DevOps teams don't model performance. What are the barriers? What practical steps could close this gap?

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/performance/RQ_L09_PerformanceAnalysis.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/performance/RQ_L09_PerformanceAnalysis.md)

### Card 304 — Q13: Per-Service SLO Budget

> [!question] Question
> **Q13: Per-Service SLO Budget**
>
> A three-service call chain has a total SLO of p99 < 400ms:
>
> ```
> User → API Gateway → Recommendation Engine → Database Service → Response
> ```
>
> Current measurements:
> - API Gateway: p99 = 30ms
> - Recommendation Engine: p99 = 280ms
> - Database Service: p99 = 50ms
> - Total: p99 = 360ms (within SLO)
>
> 1. Allocate a per-service SLO budget for each service
> 2. The Recommendation Engine team wants to add a new ML model that increases their p99 to 350ms. Should this be approved?
> 3. What trade-off does the team face? How does error budget thinking apply here?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 6.5 Per-Service SLOs as Performance Budgets
>
> The modern cloud-native approach maps classical performance engineering to per-service SLOs:
>
> | Classical PE | Cloud Equivalent |
> |-------------|-----------------|
> | Budget per component | **SLO per service** (p99 < 200ms) |
> | Budget tracking | **SLO burn-rate** monitoring |
> | Risk acceptance | **Error budget**: tolerable violation |
> | 1–5% project cost | **SRE team** allocation |
>
> **Example — End-to-end latency decomposition:**
> - Service A: SLO p99 < 50ms
> - Service B: SLO p99 < 100ms
> - Service C: SLO p99 < 50ms
> - **Total budget: p99 < 200ms**
>
> Each service owns its SLO. The call chain maps to a **wait chain** model from queuing theory.
>
> ```mermaid
> flowchart LR
>     U["User<br>Request"]
>     A["Service A<br>SLO: p99 < 50ms"]
>     B["Service B<br>SLO: p99 < 100ms"]
>     C["Service C<br>SLO: p99 < 50ms"]
>     R["Response<br>Total < 200ms"]
>     U --> A --> B --> C --> R
>     style A fill:#c8e6c9,stroke:#019546,color:#282828
>     style B fill:#fff3cd,stroke:#ffc107,color:#282828
>     style C fill:#c8e6c9,stroke:#019546,color:#282828
>     style R fill:#bbdefb,stroke:#1976d2,color:#282828
> ```
>
> #### Practice Questions
>
> 1. A microservice request fans out to 50 backend services. Each service has a 2% chance of responding slowly (>500ms). What is the probability that the user experiences a slow response? What technique would you use to mitigate this?
> 2. Why are hedged requests so effective despite adding only 2% more traffic? Under what conditions would hedged requests NOT help?
> 3. A team wants to implement per-service SLOs. Their call chain is A → B → C, with total SLO of p99 < 300ms. How would you allocate the budget? What happens when Service B consistently uses 150ms?
> 4. Bezemer found 88% of DevOps teams don't model performance. What are the barriers? What practical steps could close this gap?

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/performance/RQ_L09_PerformanceAnalysis.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/performance/RQ_L09_PerformanceAnalysis.md)

### Card 305 — Q14: The Convergence of Classical PE and Cloud-Native

> [!question] Question
> **Q14: The Convergence of Classical PE and Cloud-Native**
>
> Map each classical performance engineering concept to its cloud-native equivalent:
>
> | Classical PE Concept | Cloud-Native Equivalent |
> |---------------------|-------------------------|
> | Performance budget per component | ? |
> | Budget tracking during development | ? |
> | Risk acceptance (some degradation OK) | ? |
> | 1–5% project cost for PE activities | ? |
> | Queuing theory models | ? |
>
> Explain why Dean & Barroso claim that the "physics hasn't changed" even though the tools and scale are completely different.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Per-Service SLOs as Performance Budgets
>
> Jewell's performance budget concept  maps naturally to microservices:
>
> | Classical PE | Cloud-Native Equivalent |
> |-------------|------------------------|
> | Performance budget per component | SLO per service (e.g., p99 < 200ms) |
> | Budget tracking during development | SLO burn-rate monitoring in production |
> | Risk containment vs acceptance | Error budget: how much SLO violation is tolerable |
> | 1–5% project cost for PE | SRE team allocation |
>
> Each service owns its SLO. The end-to-end latency budget is decomposed across the call chain — analogous to the "wait chain" model where N-tier architectures are queuing nodes .
>
> For error budgets and SLO practices, see [From FIO to SLO](../reliability/slo-bridge.md).
>
> #### Proactive Performance Engineering
>
> Jewell's Performance Engineering and Management Method (PEMM) integrates performance into every lifecycle phase :
>
> - **Performance budget**: Allocate time/resources (not money) per component — track actual vs budget during development
> - **Investment**: 1–5% of total project cost for dedicated PE activities
> - **Risk balance**: Find cost-effective equilibrium between risk containment and risk acceptance
>
> The payoff: moving from reactive "firefighting" to proactive "Performance Driven" mode reduces production defect escape from 30% to just 5% .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/performance/RQ_L09_PerformanceAnalysis.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/performance/RQ_L09_PerformanceAnalysis.md)

## Queuing Theory (30)

### Card 306 — Q1: Why does variability cause queuing?

> [!question] Question
> **Q1: Why does variability cause queuing?**
>
> Two systems both have average arrival rate λ = 1 req/min and average service rate μ = 1 req/min. System A has deterministic (fixed) interarrival and service times. System B has stochastic (random) times. Which system queues, and why?

> [!answer]- Reveal answer / cues — official answer
> System A never queues — arrivals and departures are perfectly synchronized, so there is always exactly 1 request in the system.
>
> System B queues despite the same average rates. Random variation means some interarrival gaps are shorter than the service time, creating temporary bursts that outpace service. The queue peaks at 3 in the lecture example, even though λ = μ on average.
>
> **Key insight:** Queuing is driven by variability, not by average load.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 307 — Q2: Identify the queues

> [!question] Question
> **Q2: Identify the queues**
>
> A food delivery app receives orders from users, dispatches them to restaurants, and assigns delivery drivers. Identify at least three queues in this system and classify each as open or closed.

> [!answer]- Reveal answer / cues — official answer
> 1. **Order queue** (user → restaurant): orders arrive externally, get processed → **open network**
> 2. **Kitchen queue** (orders waiting to be cooked): orders arrive, food departs → **open network**
> 3. **Driver dispatch queue** (orders waiting for driver assignment): if the driver pool is fixed (e.g., 50 active drivers who recirculate after delivery) → **closed network** with M = 50
>
> Other valid answers: payment processing queue, notification queue, rating/review queue.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 308 — Q3: Economic inevitability

> [!question] Question
> **Q3: Economic inevitability**
>
> Explain why "infinite capacity is infinitely expensive" makes queues unavoidable. Give an example where over-provisioning would be wasteful.

> [!answer]- Reveal answer / cues — official answer
> Provisioning for peak demand means resources sit idle during off-peak. Example: a university Moodle server sized for 5000 concurrent exam submissions would need massive hardware, but exams only happen a few times per semester. During normal usage, 99% of that capacity is wasted.
>
> The economic optimum is to provision for typical load + some headroom, accept that queues will form during peaks, and manage response time through the hockey stick curve (stay below 75% utilization).

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 309 — Q4: When does queuing theory NOT help?

> [!question] Question
> **Q4: When does queuing theory NOT help?**
>
> Name a performance scenario where queuing theory models would be a poor choice and explain why.

> [!answer]- Reveal answer / cues — official answer
> Queuing theory is a poor fit when:
> - **Arrivals are highly correlated** (e.g., flash crowd from a viral tweet) — violates the homogeneity assumption
> - **Service times depend on queue length** (e.g., garbage collection pauses that worsen under load) — violates homogeneity
> - **The system has complex state-dependent routing** (e.g., circuit breakers, retry storms) — analytical models can't capture the feedback loops; simulation is needed
>
> In these cases, simulation (e.g., JMT) or load testing gives better results than analytical formulas.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 310 — Q5: Kendall notation

> [!question] Question
> **Q5: Kendall notation**
>
> Classify each system using Kendall notation (A/B/C):
>
> a) A web server with a single-threaded event loop processing requests with exponential interarrival and service times
> b) A toll booth with deterministic 15-second service time and random arrivals
> c) A call center with 8 agents taking calls from a queue

> [!answer]- Reveal answer / cues — official answer
> a) **M/M/1** — exponential arrivals (M), exponential service (M), 1 server
> b) **M/D/1** — exponential arrivals (M), deterministic service (D), 1 server
> c) **M/M/8** — exponential arrivals (M), exponential service (M), 8 servers (agents)

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 311 — Q6: Open vs closed

> [!question] Question
> **Q6: Open vs closed**
>
> Your company runs an internal CI/CD system. 20 developers push commits throughout the day. Each push triggers a build that takes ~5 minutes. After seeing the build result, the developer works for ~30 minutes before pushing again. Is this an open or closed system? What is M and Z?

> [!answer]- Reveal answer / cues — official answer
> This is a **closed system**:
> - M = 20 developers (fixed population that recirculates)
> - Z = 30 minutes (think time — time between seeing build result and next push)
> - S ≈ 5 minutes (service time per build)
>
> It's closed because the same 20 developers cycle through: push → wait for build → work → push again. The arrival rate is not independent of the system — it's determined by M, R, and Z.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 312 — Q7: Kendall notation — advanced

> [!question] Question
> **Q7: Kendall notation — advanced**
>
> A Kubernetes cluster auto-scales between 2 and 10 pods. Requests arrive with general (non-exponential) interarrival times. The cluster has a buffer queue that holds at most 100 pending requests. What is the Kendall notation?

> [!answer]- Reveal answer / cues — official answer
> **G/M/m/m+r** where:
> - G = general interarrival distribution
> - M = exponential service (assuming)
> - m = 2–10 (dynamic server count)
> - m+r = m + 100 (system capacity = servers + buffer)
>
> In practice, this is modeled as M/G/m/m+r  because the auto-scaling behavior makes the exact notation context-dependent. The key point is that it's a finite-capacity system.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 313 — Q8: Queue configurations

> [!question] Question
> **Q8: Queue configurations**
>
> A hospital emergency room has a triage nurse who assigns patients to one of three priority levels (critical, urgent, routine). Two doctors treat patients, always taking the highest-priority patient first. What queue configuration is this?

> [!answer]- Reveal answer / cues — official answer
> **Multiple prioritized queues, multiple servers (MQMS)** — 3 priority queues feeding 2 servers (doctors) with preemptive priority discipline. In Kendall notation: roughly M/G/2 with priority scheduling.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 314 — Q9: Method selection

> [!question] Question
> **Q9: Method selection**
>
> You're asked to predict response times for a new microservice that hasn't been built yet. You know the expected service demands from a prototype. The system will serve a fixed pool of 500 mobile app users. Which analysis method should you use?

> [!answer]- Reveal answer / cues — official answer
> **Mean Value Analysis (MVA)** — you have a closed system (M = 500 users) with known service demands but no measurement data from production. Operational analysis requires real measurements, and simulation is overkill when MVA can solve the closed network analytically.
>
> If the system had complex routing or priority queues, you'd use **simulation** instead.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 315 — Q10: Derive metrics from counters

> [!question] Question
> **Q10: Derive metrics from counters**
>
> You monitor a Redis cache server for T = 120 seconds. During this window: A = 6000 requests arrive, C = 6000 complete, and the server was busy for B = 48 seconds. Calculate all six derived metrics.

> [!answer]- Reveal answer / cues — official answer
> | Metric | Formula | Calculation | Result |
> |--------|---------|-------------|--------|
> | λ | A/T | 6000/120 | **50 req/sec** |
> | X | C/T | 6000/120 | **50 req/sec** |
> | S | B/C | 48/6000 | **8 ms/req** |
> | U | B/T | 48/120 | **40%** |
>
> For N and R we need W (time in system), which isn't given directly. But we can derive R from the M/M/1 formula if we assume exponential service:
>
> R = S/(1−ρ) = 0.008/(1−0.4) = **13.3 ms**
> N = X × R = 50 × 0.0133 = **0.67 requests** in system
>
> **Sanity check (Little's Law):** N = X × R = 50 × 0.0133 = 0.67 ✓

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 316 — Q11: Counter identification

> [!question] Question
> **Q11: Counter identification**
>
> A DevOps engineer says: "Our API gateway processed 45,000 requests in the last 15 minutes. The p50 latency is 120ms and the server CPU was at 65% during that window." Map these to the five counters (T, A, C, W, B).

> [!answer]- Reveal answer / cues — official answer
> | Statement | Counter | Value |
> |-----------|---------|-------|
> | "last 15 minutes" | T | 900 sec |
> | "45,000 requests" | A (and likely C, if flow balance holds) | 45,000 |
> | "p50 latency 120ms" | Related to R (= W/C), but this is a percentile, not the sum W | Need conversion |
> | "CPU at 65%" | U = B/T → B = U × T | B = 0.65 × 900 = 585 sec |
>
> **Missing:** W (total time in system) is not directly available from p50 latency. If we approximate R ≈ 120ms (median ≈ mean for exponential), then W ≈ R × C = 0.12 × 45,000 = 5,400 req-sec. But this is an approximation — p50 ≠ mean for skewed distributions.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 317 — Q12: Assumption violations

> [!question] Question
> **Q12: Assumption violations**
>
> You observe A = 10,000 and C = 9,200 over a 5-minute window. Which assumption is violated? What could cause this? How would you fix the analysis?

> [!answer]- Reveal answer / cues — official answer
> **Flow balance** is violated: A − C = 800 requests were lost or are still in the system.
>
> Possible causes:
> - Server crashed or restarted during observation (requests lost)
> - Observation window is too short relative to service time (requests still being processed)
> - Requests are being dropped by a finite buffer
>
> **Fix:** Either (1) extend the observation period until A ≈ C, or (2) if the system is lossy, model it with a finite-buffer queue (M/M/c/K) and account for rejection probability.
>
> Rule of thumb: observation period should be 10–100× the average busy period.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 318 — Q13: System vs resource level

> [!question] Question
> **Q13: System vs resource level**
>
> You have system-level measurements: X = 100 req/sec, R = 50ms. You also know the app server visits the database V = 3 times per request. Using the Forced Flow Law, what is the database throughput?

> [!answer]- Reveal answer / cues — official answer
> **Forced Flow Law:** X_db = V_db × X = 3 × 100 = **300 queries/sec**
>
> The database sees 3× more traffic than the front-end. This is why databases often become bottlenecks — the visit ratio amplifies system-level load.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 319 — Q14: Worked example — full pipeline

> [!question] Question
> **Q14: Worked example — full pipeline**
>
> A Moodle API server is monitored for T = 60 sec during an exam. Counters: B = 36 sec, A = C = 1800. Derive S, U, X, and estimate R using M/M/1 formula. Perform a Little's Law sanity check.

> [!answer]- Reveal answer / cues — official answer
> **Step 1 — Derived metrics:**
> - S = B/C = 36/1800 = **0.02 sec = 20 ms/req**
> - U = B/T = 36/60 = **0.60 = 60%**
> - X = C/T = 1800/60 = **30 req/sec**
>
> **Step 2 — Response time (M/M/1):**
> R = S/(1−ρ) = 0.02/(1−0.6) = 0.02/0.4 = **0.05 sec = 50 ms**
>
> **Step 3 — Little's Law sanity check:**
> N = X × R = 30 × 0.05 = **1.5 requests** in system ✓
>
> At 60% utilization, the server is moderately loaded. Response time is 2.5× service time. If load increases to 90% utilization, R would jump to 0.02/(1−0.9) = **200 ms** — a 4× increase from a 50% load increase.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 320 — Q15: Little's Law — basic

> [!question] Question
> **Q15: Little's Law — basic**
>
> A coffee shop serves X = 2 customers/min with average visit time R = 10 min. How many customers are in the shop on average?

> [!answer]- Reveal answer / cues — official answer
> **Little's Law:** N = X × R = 2 × 10 = **20 customers**
>
> This holds regardless of how many baristas, the queue discipline, or whether arrivals are random or scheduled. The only requirement is flow balance (customers eventually leave).

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 321 — Q16: Little's Law — reverse

> [!question] Question
> **Q16: Little's Law — reverse**
>
> Your monitoring shows an average of N = 4.5 requests in the system and throughput X = 1.5 req/sec. What is the average response time?

> [!answer]- Reveal answer / cues — official answer
> **Little's Law rearranged:** R = N/X = 4.5/1.5 = **3 seconds**

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 322 — Q17: Little's Law — consistency check

> [!question] Question
> **Q17: Little's Law — consistency check**
>
> You measure X = 200 req/sec, R = 25 ms, and N = 10 requests in system. Are these measurements consistent?

> [!answer]- Reveal answer / cues — official answer
> **Check:** N = X × R = 200 × 0.025 = **5.0**
>
> But measured N = 10. This is **inconsistent** — N should be 5, not 10.
>
> Possible causes:
> - R measurement is wrong (e.g., measuring only server time, not including queue wait)
> - N measurement includes requests in a different part of the system (boundary mismatch)
> - Measurement tools are sampling different time windows
>
> Little's Law is a tautology — if the numbers don't match, the measurements are wrong, not the law .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 323 — Q18: Utilization Law

> [!question] Question
> **Q18: Utilization Law**
>
> A database server has service demand D = 40 ms/txn and the system throughput is X = 20 txn/sec. What is the database utilization? If there are 2 database replicas, what is the per-replica utilization?

> [!answer]- Reveal answer / cues — official answer
> **Single server:** U = X × D = 20 × 0.04 = **0.80 = 80%** — dangerously close to the hockey stick!
>
> **With 2 replicas:** U = X × D / m = 20 × 0.04 / 2 = **0.40 = 40%** — comfortable headroom.
>
> Adding one replica drops utilization from 80% to 40%, dramatically improving response time (from 5×S to 1.67×S using the hockey stick formula).

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 324 — Q19: Service Demand — bottleneck identification

> [!question] Question
> **Q19: Service Demand — bottleneck identification**
>
> A web application has three resources with the following per-transaction demands:
>
> | Resource | Visits (V) | Service time per visit (S) |
> |----------|-----------|---------------------------|
> | Nginx | 1 | 2 ms |
> | App server | 1 | 12 ms |
> | PostgreSQL | 5 | 6 ms |
>
> Find the service demand for each resource, identify the bottleneck, and calculate the maximum system throughput.

> [!answer]- Reveal answer / cues — official answer
> **Step 1 — Service demands (D = V × S):**
> - D_nginx = 1 × 2 = **2 ms**
> - D_app = 1 × 12 = **12 ms**
> - D_postgres = 5 × 6 = **30 ms** ← D_max
>
> **Step 2 — Bottleneck:** PostgreSQL (highest D)
>
> **Step 3 — Maximum throughput:**
> X_max = 1/D_max = 1/0.030 = **33.3 TPS**
>
> No amount of Nginx or app server optimization can push throughput past 33.3 TPS. To improve, reduce PostgreSQL demand: add caching (reduce V from 5 to 2), optimize queries (reduce S), or add read replicas.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 325 — Q20: Forced Flow Law

> [!question] Question
> **Q20: Forced Flow Law**
>
> System throughput is X = 10 txn/sec. Each transaction visits the cache V_cache = 8 times and the database V_db = 2 times. What is the throughput at each resource?

> [!answer]- Reveal answer / cues — official answer
> **Forced Flow Law:** X_k = V_k × X
>
> - X_cache = 8 × 10 = **80 queries/sec**
> - X_db = 2 × 10 = **20 queries/sec**
>
> The cache handles 4× more traffic than the database. This is the whole point of caching — redirect visits away from the slow resource to reduce its demand.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 326 — Q21: Utilization Law — what-if analysis

> [!question] Question
> **Q21: Utilization Law — what-if analysis**
>
> Current state: X = 0.45 txn/sec, D_postgres = 32 ms, U_postgres = 1.44%. You add a caching layer that reduces PostgreSQL visits from V = 4 to V = 1 (cache handles the other 3). What is the new D_postgres and U_postgres?

> [!answer]- Reveal answer / cues — official answer
> **New service demand:**
> D_postgres = V × S = 1 × 8 ms = **8 ms** (was 32 ms)
>
> **New utilization:**
> U_postgres = X × D = 0.45 × 0.008 = **0.36%** (was 1.44%)
>
> Utilization dropped by 4× because the visit count dropped by 4×. The caching layer didn't change service time S — it reduced the number of visits V, which is often the more effective optimization.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 327 — Q22: Combined laws

> [!question] Question
> **Q22: Combined laws**
>
> A system has X = 50 txn/sec. The app server has D_app = 15 ms and the DB has D_db = 25 ms. Calculate: (a) utilization of each, (b) the bottleneck, (c) max throughput, and (d) what happens if you double the DB service time.

> [!answer]- Reveal answer / cues — official answer
> **(a) Utilization:**
> - U_app = X × D_app = 50 × 0.015 = **75%**
> - U_db = X × D_db = 50 × 0.025 = **125%** — **impossible!** Utilization can't exceed 100%.
>
> This means the system **cannot sustain** X = 50 txn/sec. The actual throughput is capped by the bottleneck.
>
> **(b) Bottleneck:** Database (D_db = 25 ms > D_app = 15 ms)
>
> **(c) Max throughput:** X_max = 1/D_max = 1/0.025 = **40 TPS**
>
> At 40 TPS: U_db = 40 × 0.025 = 100%, U_app = 40 × 0.015 = 60%.
>
> **(d) If DB service time doubles:** D_db = 50 ms, X_max = 1/0.050 = **20 TPS** — throughput halves.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 328 — Q23: Hockey stick calculation

> [!question] Question
> **Q23: Hockey stick calculation**
>
> A server has service time S = 10 ms. Calculate response time at utilization levels of 50%, 80%, 90%, and 95%.

> [!answer]- Reveal answer / cues — official answer
> Using R = S/(1−ρ):
>
> | ρ | R = 10/(1−ρ) | R/S multiplier |
> |---|-------------|---------------|
> | 50% | 10/0.5 = **20 ms** | 2× |
> | 80% | 10/0.2 = **50 ms** | 5× |
> | 90% | 10/0.1 = **100 ms** | 10× |
> | 95% | 10/0.05 = **200 ms** | 20× |
>
> Going from 80% to 95% utilization (a modest 19% increase in load) causes a 4× increase in response time (50ms → 200ms). This is the hockey stick effect.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 329 — Q24: Hockey stick — SLA compliance

> [!question] Question
> **Q24: Hockey stick — SLA compliance**
>
> Your SLA requires response time R ≤ 100 ms. Service time S = 15 ms. What is the maximum utilization you can tolerate?

> [!answer]- Reveal answer / cues — official answer
> **Rearrange:** R = S/(1−ρ) → 1−ρ = S/R → ρ = 1 − S/R
>
> ρ = 1 − 15/100 = 1 − 0.15 = **85%**
>
> You must keep utilization below 85% to meet the SLA. In practice, you'd target 70–75% to leave headroom for traffic spikes.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 330 — Q25: Tail latency

> [!question] Question
> **Q25: Tail latency**
>
> Your microservice architecture fans out each user request to 50 backend services in parallel. Each service has a 2% probability of being slow (>500ms). What is the probability that any given user request experiences a slow response?

> [!answer]- Reveal answer / cues — official answer
> **Tail amplification formula:** P(any slow) = 1 − (1 − p)^N
>
> P(any slow) = 1 − (1 − 0.02)^50 = 1 − (0.98)^50
>
> (0.98)^50 = 0.364
>
> P(any slow) = 1 − 0.364 = **63.6%**
>
> Nearly two-thirds of user requests will experience a slow response, even though each individual service is slow only 2% of the time . This is why distributed systems must optimize tail latency (p99), not average latency.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 331 — Q26: Interactive system sizing

> [!question] Question
> **Q26: Interactive system sizing**
>
> An online IDE has think time Z = 45 sec (editing code), service time S = 2 sec (compile + run), target utilization ρ ≤ 70%, target response R ≤ 5 sec. How many concurrent developers can use it?

> [!answer]- Reveal answer / cues — official answer
> **Step 1 — Max throughput:**
> X = ρ/S = 0.70/2 = **0.35 txn/sec**
>
> **Step 2 — Interactive Response Time Law:**
> M = X × (R + Z) = 0.35 × (5 + 45) = 0.35 × 50 = **17.5 → 17 developers**
>
> Beyond 17 concurrent users, either response time exceeds 5 sec or utilization exceeds 70%.
>
> **Verification with Little's Law:**
> N = X × R = 0.35 × 5 = 1.75 requests in system ✓ (reasonable for 17 users)

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 332 — Q27: Adding servers — cost analysis

> [!question] Question
> **Q27: Adding servers — cost analysis**
>
> Continuing Q26: management wants to support 50 developers. How many servers are needed?

> [!answer]- Reveal answer / cues — official answer
> With 1 server: 17 developers.
>
> Needed: 50 / 17 ≈ 3 servers (with the simplifying assumption that load distributes evenly).
>
> With c servers, max throughput = c × (ρ/S) = c × 0.35 txn/sec.
> M = c × 0.35 × (R + Z)
>
> For M = 50: c = 50 / (0.35 × 50) = 50/17.5 = **2.86 → 3 servers**
>
> Three servers support ~52 developers.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 333 — Q28: Response time decomposition

> [!question] Question
> **Q28: Response time decomposition**
>
> A request goes through three resources in sequence: Nginx (D = 3 ms), App server (D = 20 ms), PostgreSQL (D = 15 ms). System throughput is X = 30 txn/sec. Calculate the response time at each resource and the total system response time.

> [!answer]- Reveal answer / cues — official answer
> **Step 1 — Utilization at each resource:**
> - U_nginx = X × D = 30 × 0.003 = 9%
> - U_app = 30 × 0.020 = 60%
> - U_postgres = 30 × 0.015 = 45%
>
> **Step 2 — Response time at each (M/M/1):**
> - R_nginx = D/(1−U) = 0.003/(1−0.09) = **3.3 ms**
> - R_app = 0.020/(1−0.60) = **50 ms**
> - R_postgres = 0.015/(1−0.45) = **27.3 ms**
>
> **Step 3 — Total (sequential):**
> R_total = 3.3 + 50 + 27.3 = **80.6 ms**
>
> The app server contributes 62% of the total response time despite having only 60% utilization. It's the bottleneck (highest D), and optimizing it yields the most improvement.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 334 — Q29: Performance engineering workflow

> [!question] Question
> **Q29: Performance engineering workflow**
>
> You're tasked with improving a slow checkout page. Using the 7-step performance engineering workflow, describe what you would do at each step.

> [!answer]- Reveal answer / cues — official answer
> 1. **Build:** The checkout page already exists — instrument it with counters
> 2. **Measure:** Collect T, A, C, B from HTTP logs and Prometheus for each component (web, API, payment gateway, DB) over a 10-minute peak window
> 3. **Derive:** Calculate X, U, S, R for each resource. Build a service demand table
> 4. **Model:** Apply Utilization Law to find D_max → identify the bottleneck. Use Forced Flow Law to understand visit ratios
> 5. **Predict:** "What if we add a cache?" → recalculate D with reduced V for DB. "What if traffic doubles?" → check if any U exceeds 75%
> 6. **Validate:** Deploy the cache, measure again, compare actual vs predicted improvement
> 7. **Refine:** If prediction was off, investigate — maybe the model missed a resource (network? external API?). Add more counters, iterate

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

### Card 335 — Q30: When to simulate

> [!question] Question
> **Q30: When to simulate**
>
> Your team is debating whether to use analytical models or simulation for a new message queue system with the following characteristics: 3 priority levels, finite buffer of 1000 messages, batch processing (consumer pulls 10 messages at a time), and variable consumer count (auto-scaling). Which approach would you recommend, and why?

> [!answer]- Reveal answer / cues — official answer
> **Simulation** is the right choice here. The system has multiple features that violate standard analytical model assumptions:
>
> 1. **3 priority levels** — analytical priority queue formulas exist for M/M/c with preemptive priority, but they become complex and require distributional assumptions
> 2. **Finite buffer** — M/G/m/m+r models exist but are harder to solve analytically
> 3. **Batch processing** — pulling 10 messages at a time creates correlated service, which standard models don't handle
> 4. **Auto-scaling** — dynamic server count violates the steady-state assumption
>
> Use JMT or a custom discrete-event simulation. Validate the simulation against a simplified analytical model (e.g., M/M/c for the base case without priorities or batching) to build confidence.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/queuing/RQ-A09-Queuing.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/queuing/RQ-A09-Queuing.md)

## Security (12)

### Card 336 — Q1: Fault-Error-Failure in Security

> [!question] Question
> **Q1: Fault-Error-Failure in Security**
>
> A junior developer writes a SQL query using string concatenation instead of parameterized queries. An attacker discovers this endpoint and submits `' OR 1=1 --` as a username.
>
> 1. Trace the **fault → error → failure** chain (Avizienis 2004) for this SQL injection attack. Identify each stage precisely.
> 2. Now trace the same chain for a **regular bug** in the same code — e.g., the query crashes when a user's name contains an apostrophe (like "O'Brien"). What is different about the fault stage?
> 3. Both scenarios share the same root fault. Why does the security case represent a fundamentally different risk category, even though the fix (parameterized queries) is identical?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.3 Fault-Error-Failure Chain in Security
>
> The dependability taxonomy  provides a causal model that applies directly to security:
>
> ```mermaid
> flowchart LR
>     F["Fault<br>(Vulnerability)"]
>     E["Error<br>(Exploited State)"]
>     FL["Failure<br>(Security Breach)"]
>     F -->|"Activation<br>(Attack)"| E
>     E -->|"Propagation"| FL
>     style F fill:#fff3cd,stroke:#ffc107,color:#282828
>     style E fill:#ffcdd2,stroke:#d32f2f,color:#282828
>     style FL fill:#d32f2f,stroke:#b71c1c,color:#ffffff
> ```
>
> | Dependability Term | Security Interpretation | Example |
> |--------------------|------------------------|---------|
> | **Fault** | Vulnerability in code or design | Missing bounds check (Heartbleed) |
> | **Error** | Exploited internal state | Memory contents leaked to attacker |
> | **Failure** | Observable security violation | Private keys, passwords exposed |
> | **Malicious external fault** | Attack | Crafted TLS heartbeat request |
>
> The key insight: in security, the fault (vulnerability) may exist for years without causing an error. The **activation** of the fault requires a deliberate, malicious external action — the attack. This distinguishes security faults from accidental faults in reliability.
>
> **Four means of dealing with faults** (Avizienis 2004):
>
> | Means | Description | Security Example |
> |-------|-------------|------------------|
> | **Fault prevention** | Avoid introducing faults | Secure coding standards, CERT rules |
> | **Fault tolerance** | Continue operating despite faults | Input validation, sandboxing |
> | **Fault removal** | Find and eliminate faults | SAST, DAST, code review, pen testing |
> | **Fault forecasting** | Predict future faults | Threat modeling, risk assessment |
>
> #### The Fault-Error-Failure Chain in Security
>
> The causal chain **fault → error → failure** from dependability theory applies to security, with one critical addition: **attacks** are deliberate faults introduced by an adversary :
>
> ```mermaid
> flowchart LR
>     F["🔧 Fault<br>(flaw in code)"]
>     E["⚠️ Error<br>(incorrect state)"]
>     Fail["💥 Failure<br>(breach)"]
>     A["🎯 Attack<br>(malicious fault)"]
>
>     F -->|"activates"| E
>     A -->|"triggers"| E
>     E -->|"propagates"| Fail
>
>     style F fill:#fff3cd,stroke:#ffc107,color:#282828
>     style E fill:#fce4ec,stroke:#e91e63,color:#282828
>     style Fail fill:#f8d7da,stroke:#dc3545,color:#282828
>     style A fill:#e8eaf6,stroke:#3f51b5,color:#282828
> ```
>
> A **vulnerability** exists when a fault (e.g., missing bounds check) can be activated by an attack (e.g., crafted input) to produce an error (e.g., buffer overread) that propagates to a failure (e.g., data exfiltration). The Heartbleed vulnerability (CVE-2014-0160) illustrates this chain: a missing bounds check in OpenSSL's heartbeat extension allowed attackers to read up to 64KB of server memory per request .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/security/RQ_L10_Security.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/security/RQ_L10_Security.md)

### Card 337 — Q2: Finding vs Preventing — The CTO's Dilemma

> [!question] Question
> **Q2: Finding vs Preventing — The CTO's Dilemma**
>
> A startup CTO with a 20-person engineering team and limited budget asks: "Should we invest in SAST tools or threat modeling first?" You have the following data:
>
> - McGraw's **50/50 split**: half of security issues are design flaws (found by threat modeling), half are implementation bugs (found by tools)
> - IBM Cost of a Data Breach 2024: average cost **$4.88M**, average detection time **194 days**
> - Avizienis's **4 means** of dependability: fault prevention, fault tolerance, fault removal, fault forecasting
>
> (a) Using McGraw's data, argue why investing in only ONE approach leaves ~50% of vulnerabilities unaddressed.
> (b) If you must pick ONE to start with, which do you recommend for a fast-moving startup that deploys daily? Justify your answer.
> (c) Map each of the 4 means from Avizienis to a concrete security practice. Which means does threat modeling fall under? Which does SAST fall under?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.4 Finding vs Preventing: McGraw's 50/50 Split
>
> McGraw identifies two fundamentally different categories of security problems :
>
> | Category | Prevalence | Found By | Example |
> |----------|-----------|----------|---------|
> | **Implementation bugs** | ~50% | Code-level tools (SAST, fuzzing) | Buffer overflow, SQL injection |
> | **Design flaws** | ~50% | Architecture analysis (threat modeling) | Missing trust boundary, insecure protocol |
>
> This split has a critical practical consequence: **no amount of code scanning will find design flaws**, and no amount of architecture review will catch implementation bugs. Effective security requires both reactive (find & fix) and proactive (prevent) strategies working together.
>
> **Reactive (Find & Fix):**
> - Fuzzing, penetration testing
> - SAST, DAST, IAST
> - Code review (though <1% of review comments address security )
> - Costly: average breach = $4.88M
>
> **Proactive (Prevent):**
> - Security requirements engineering (SQUARE )
> - Threat modeling (STRIDE )
> - Secure design principles (Saltzer & Schroeder )
> - DevSecOps pipeline integration
>
> #### McGraw's 50/50 Split
>
> McGraw argues that roughly **50% of security problems are implementation bugs** (buffer overflows, SQL injection) and **50% are design flaws** (insecure architecture, missing authentication) . This means:
>
> - Code-level tools (SAST, linters) only address half the problem
> - Design-level analysis (threat modeling, architecture review) is equally essential
> - His **7 Touchpoints** model interleaves constructive and destructive activities across every SDLC phase
>
> Howard's **SD3** — Secure by Design, Secure by Default, Secure in Deployment — operationalizes prevention at every stage . "You cannot build a secure system until you understand your threats" — threat modeling alone finds approximately 50% of security flaws.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/security/RQ_L10_Security.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/security/RQ_L10_Security.md)

### Card 338 — Q3: Tool Selection Under Constraints

> [!question] Question
> **Q3: Tool Selection Under Constraints**
>
> Your team has a CI/CD pipeline deploying **5× per day**. Budget allows only **ONE** security testing tool. Here are the trade-offs:
>
> | Tool | Strength | Weakness |
> |------|----------|----------|
> | SAST | Finds bugs early, runs on source code | ~70% false positive rate (Rice's Theorem — undecidable in general) |
> | DAST | Tests running application, low false positives | Adds ~14 min to pipeline (Rangnau 2020), only finds runtime issues |
> | SCA | Catches known CVEs in dependencies | Cannot find custom code bugs, depends on CVE database currency |
>
> 1. For each tool, calculate the **practical impact** on your 5×/day deployment cycle. Which tool causes the least friction?
> 2. Rajapakse 2021 found that DevSecOps tools are only about **30% effective** at finding vulnerabilities. How does this change your cost-benefit analysis?
> 3. Make your recommendation and justify it. Under what circumstances would you change your answer?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.2 Static Application Security Testing (SAST)
>
> SAST analyzes source code without executing it. Chess & West describe a spectrum of analysis techniques, ordered by increasing precision and cost :
>
> | Technique | What It Checks | False Positive Rate | Cost |
> |-----------|---------------|---------------------|------|
> | **Lexical analysis** | Pattern matching on tokens | Very high | Very low |
> | **AST matching** | Syntax tree patterns | High | Low |
> | **Data flow analysis** | How data moves through code | Moderate | Medium |
> | **Control flow analysis** | Execution path feasibility | Moderate | Medium |
> | **Abstract interpretation** | Sound approximation of semantics | Lower | High |
> | **Model checking** | Exhaustive state exploration | Lowest | Very high |
>
> **Why false positives are inherent:** Rice's Theorem proves that any nontrivial semantic property of a general program is undecidable. Security tools deliberately choose to **over-report** (false positives) rather than **under-report** (missed vulnerabilities). The practical result: approximately **70% of SAST results are false positives** .
>
> > "Static analysis is like a spell checker for security bugs." — Chess 2007
>
> **Practical impact of false positives:**
> - Alert fatigue: developers stop trusting tools
> - Triage cost: each false positive consumes review time
> - Industry challenge: only **30%** of scan results are actionable
>
> #### SAST vs. DAST vs. IAST vs. RASP
>
> Modern security testing increasingly uses hybrid approaches :
>
> | Tool Type | How It Works | Strengths | Weaknesses |
> |-----------|-------------|-----------|------------|
> | **SAST** | Analyzes source/bytecode | Early feedback, full code coverage | False positives (Rice's Theorem), no runtime context |
> | **DAST** | Probes running app externally | Finds runtime issues, low false positives | Slow, limited coverage, no code location |
> | **IAST** | Agent inside running app | Combines SAST+DAST precision, code-level detail | Requires instrumented runtime |
> | **RASP** | Self-protecting runtime agent | Real-time attack blocking | Performance overhead, not a testing tool |
> | **SCA** | Scans dependencies | Finds known CVEs in libraries | Cannot detect novel vulnerabilities |
>
> ```mermaid
> flowchart LR
>     IDE["<b>🖥️ IDE</b><br>IDE SAST<br>Real-time"]
>     Build["<b>🔨 Build</b><br>SAST · SCA"]
>     Test["<b>🧪 Test</b><br>DAST<br>HTTP scanning"]
>     Runtime["<b>🚀 Runtime</b><br>IAST · RASP"]
>
>     IDE --> Build --> Test --> Runtime
>
>     style IDE fill:#e8f5e9,stroke:#019546,color:#282828
>     style Build fill:#c8e6c9,stroke:#019546,color:#282828
>     style Test fill:#a5d6a7,stroke:#019546,color:#282828
>     style Runtime fill:#81c784,stroke:#019546,color:#282828
> ```
>
> The trend is toward **shifting left** — catching vulnerabilities as early as possible in the development cycle. IDE-integrated SAST provides real-time feedback during coding, while SCA catches known dependency vulnerabilities at build time .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/security/RQ_L10_Security.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/security/RQ_L10_Security.md)

### Card 339 — Q4: Code Review + Fuzzing — A Combined Strategy

> [!question] Question
> **Q4: Code Review + Fuzzing — A Combined Strategy**
>
> You are designing the security testing strategy for a **banking application** that processes wire transfers.
>
> - Yu 2023 found that **<1% of code review comments** address security, but when a reviewer **suggests a fix**, the resolution rate is **81.3%**
> - Takanen 2008 found that in fuzzing, **1% more code coverage ≈ 1% more bugs** found
>
> (a) What types of vulnerabilities does **code review** catch well? What does it miss? (Think: logic flaws vs. input handling edge cases)
> (b) What types of vulnerabilities does **fuzzing** catch well? What does it miss? (Think: crashes and memory errors vs. business logic bypasses)
> (c) Design a combined strategy: How would you structure security-focused code reviews to increase the <1% rate? How would you configure fuzzing to maximize coverage of critical payment paths?
> (d) For the banking context, which technique is more critical for preventing **financial fraud** vs. preventing **denial-of-service**?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.7 Code Review for Security
>
> Yu et al. (2023) conducted a large-scale empirical study of security defect detection via code review :
>
> **Study scope:** 432K code review comments across OpenStack and Qt, 2017–2022.
>
> | Metric | Value |
> |--------|-------|
> | Security-related comments | **<1%** of all review comments |
> | Top defect: Race conditions | **39%** |
> | Top defect: Crashes | 22.8% |
> | Top defect: Resource leaks | 10.9% |
> | Overall resolution rate | **65.9%** |
> | With reviewer suggestion | **81.3%** resolution |
>
> **Key findings:**
> - Manual code review finds **complex, context-dependent** security defects that automated tools miss (race conditions, logic errors)
> - When reviewers **suggest a fix**, the resolution rate jumps from 66% to 81%
> - The recommended approach is **hybrid**: automated tools for scale, human review for context
>
> #### Code Review for Security
>
> Yu et al. (2023) conducted the largest empirical study of security defect detection through code review, analyzing 432K review comments across OpenStack and Qt :
>
> | Finding | Value |
> |---------|-------|
> | Security-related comments | < 1% of all review comments |
> | Security defects resolved | 65.9% overall |
> | Resolution when reviewer suggests fix | 81.3% |
> | Top defect: race conditions | 39% of security defects |
> | Second: crashes/resource management | 22.8% |
>
> The key insight: security defects are **rare in code review** but have high resolution rates when reviewers provide concrete fix suggestions. Code review complements automated tools by catching design-level issues and security-sensitive logic that SAST cannot detect.
>
> Howard estimates that threat modeling finds ~50% of security flaws, with code review finding the complementary 50% .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/security/RQ_L10_Security.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/security/RQ_L10_Security.md)

### Card 340 — Q5: STRIDE Application

> [!question] Question
> **Q5: STRIDE Application**
>
> Consider this simplified Data Flow Diagram for a web banking application:
>
> ```
> [User] → (Login Page) → [Auth Service] → [Session Store]
>                                 ↓
> [Admin] → (Admin Panel) → [Account DB]
> ```
>
> 1. Apply **STRIDE** to identify at least **6 threats** — one per STRIDE category. For each, state:
>    - The threat description
>    - Which DFD element it targets (process, data store, data flow, or external entity)
>    - One concrete mitigation
> 2. Scandariato 2015 found that threat modeling achieves only **36% recall** — meaning 64% of real threats are missed. Looking at your 6 threats above, what **categories of threats** might you have missed? (Hint: consider insider threats, side-channel attacks, supply chain risks)
> 3. How would you improve recall? What complementary techniques could supplement STRIDE?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.3 STRIDE: Six Categories, Six Security Properties
>
> | Threat | Security Property | Example | Typical Target |
> |--------|-------------------|---------|----------------|
> | **S**poofing | Authentication | Fake login page | External interactor |
> | **T**ampering | Integrity | Modified database records | Data flow, data store |
> | **R**epudiation | Non-repudiation | Denying a transaction | Process, data store |
> | **I**nformation Disclosure | Confidentiality | Data leak (Heartbleed) | Data flow, data store |
> | **D**enial of Service | Availability | Server flood (WannaCry) | Process, data flow |
> | **E**levation of Privilege | Authorization | User → admin | Process |
>
> STRIDE is applied **per DFD element**: each element is checked against the applicable threat categories. However, Shostack himself warns that STRIDE **"makes a lousy taxonomy"** — it was designed as a **mnemonic** to help practitioners remember threat categories, not as a rigorous classification system .
>
> #### STRIDE Threat Categories
>
> Microsoft's STRIDE framework provides a mnemonic for six threat categories :
>
> | Category | Threat | Property Violated | Example |
> |----------|--------|-------------------|---------|
> | **S**poofing | Pretending to be someone else | Authentication | Stolen credentials |
> | **T**ampering | Modifying data or code | Integrity | Man-in-the-middle attack |
> | **R**epudiation | Denying an action occurred | Non-repudiation | Unsigned transactions |
> | **I**nformation Disclosure | Exposing data to unauthorized parties | Confidentiality | Heartbleed (CVE-2014-0160)  |
> | **D**enial of Service | Making a system unavailable | Availability | WannaCry ransomware  |
> | **E**levation of Privilege | Gaining unauthorized access | Authorization | Buffer overflow → root |
>
> Shostack candidly acknowledges that STRIDE "makes a lousy taxonomy" — it was designed as a **mnemonic to prompt thinking**, not a rigorous classification system . Categories overlap, and real attacks often span multiple categories.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/security/RQ_L10_Security.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/security/RQ_L10_Security.md)

### Card 341 — Q6: Method Selection for Healthcare

> [!question] Question
> **Q6: Method Selection for Healthcare**
>
> A healthcare startup is building a **patient portal** that must comply with **GDPR**. They have 3 developers, no dedicated security team, and a 6-month runway to launch.
>
> Compare three threat modeling methods:
>
> | Method | Focus | Effort |
> |--------|-------|--------|
> | STRIDE | Technical threats per DFD element | Medium — requires DFD creation |
> | PASTA | Risk-centric, attacker simulation | High — 7 stages, needs threat intelligence |
> | LINDDUN | Privacy threats (linkability, identifiability, etc.) | Medium — privacy-specific DFD analysis |
>
> (a) Given GDPR compliance is mandatory, why is STRIDE alone insufficient? What privacy-specific threats does LINDDUN catch that STRIDE misses?
> (b) The startup cannot afford all three methods. Propose a **pragmatic combination** (e.g., STRIDE + selected LINDDUN categories) and justify your choice.
> (c) Yskout 2020 proposed a **maturity model** for threat modeling adoption. At what maturity level should this startup begin, and what is their realistic 12-month growth path?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 12 Threat Modeling Methods
>
> Shevchenko et al. (2018) surveyed 12 threat modeling methods at the SEI/CMU :
>
> | Method | Focus | Strengths | Limitations |
> |--------|-------|-----------|-------------|
> | **STRIDE** | Per-element threats via DFDs | Most mature, systematic | Scalability, 36% recall |
> | **PASTA** | Risk-centric, 7-stage process | Business context | Complex, requires expertise |
> | **LINDDUN** | Privacy threats | Complements STRIDE for GDPR | Privacy-only scope |
> | **Attack Trees** | Decompose attack goals | Visual, intuitive | Manual, no tool support |
> | **CVSS Scoring** | Vulnerability severity | Standardized, quantitative | Scores may vary across experts |
> | **Trike** | Requirements-based, risk model | Formal risk assessment | Limited adoption |
>
> The survey's key conclusion: **no single best method** — selection depends on project needs, team expertise, and regulatory context . STRIDE remains the most mature and widely adopted, but organizations should consider combining methods for comprehensive coverage.
>
> #### 3.5 Alternative Threat Modeling Methods
>
> Shevchenko et al. (2018) survey 12 threat modeling methods and conclude that **no single method is recommended over another** — selection depends on project context :
>
> | Method | Focus | Best For |
> |--------|-------|----------|
> | **STRIDE** | Per-element threats | Technical system analysis |
> | **PASTA** | Risk-centric (7 stages) | Business-technical alignment |
> | **LINDDUN** | Privacy threats | GDPR/privacy-focused systems |
> | **Attack Trees** | Attacker goals | Complex multi-step attacks |
> | **VAST** | Agile/enterprise scale | Large organizations |
> | **OCTAVE** | Organizational risk | Strategic planning |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/security/RQ_L10_Security.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/security/RQ_L10_Security.md)

### Card 342 — Q7: Principle Mapping — Learning from Breaches

> [!question] Question
> **Q7: Principle Mapping — Learning from Breaches**
>
> The lecture presented 6 major security breaches. Map each to the **Saltzer & Schroeder** design principle it most directly violated:
>
> | Breach | Year | Principle Violated |
> |--------|------|--------------------|
> | Heartbleed | 2014 | ? |
> | Log4Shell | 2021 | ? |
> | Equifax | 2017 | ? |
> | SolarWinds | 2020 | ? |
> | WannaCry | 2017 | ? |
> | Target | 2013 | ? |
>
> For **TWO** breaches of your choice, explain in detail:
> (a) The vulnerability — what was the technical flaw?
> (b) Which Saltzer & Schroeder principle was violated — state the principle and its definition
> (c) How applying the principle **during design** would have prevented or mitigated the breach

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### SolarWinds (2020) — Open Design Violated
>
> | Aspect | Detail |
> |--------|--------|
> | **Timeline** | Compromise: Sep 2019 → Discovery: Dec 2020 (9 months undetected) |
> | **Root cause** | Attackers injected malicious code into the Orion build process  |
> | **Impact** | 18,000 organizations installed compromised update  |
> | **Principle violated** | Open design — security depended on build process secrecy, not on verifiable integrity |
> | **Triggered** | Executive Order 14028 mandating SBOMs and supply chain security |
>
> #### Saltzer & Schroeder's 8 Principles Still Define Secure Design After 50 Years
>
> In 1975, Saltzer and Schroeder published eight design principles for computer system protection . Remarkably, these principles remain the foundation of modern secure software engineering — from container isolation (least privilege) to open-source security (open design) to zero-trust architectures (complete mediation). Their evolution traces a clear arc from conceptual warnings to executable code artifacts.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/security/RQ_L10_Security.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/security/RQ_L10_Security.md)

### Card 343 — Q8: Input Validation — "All Input Is Evil"

> [!question] Question
> **Q8: Input Validation — "All Input Is Evil"**
>
> Howard's rule states: **"All input is evil until proven otherwise."**
>
> A REST API endpoint accepts the following JSON:
>
> ```json
> {
>   "user_name": "Alice",
>   "email": "alice@example.com",
>   "age": 25
> }
> ```
>
> 1. Design a **whitelist-based** (allowlist) validation strategy for each field. Specify: allowed characters, length limits, format constraints, and type checks.
> 2. A colleague proposes **blacklist-based** validation instead — blocking known-bad characters like `<`, `>`, `'`, `"`. Give a **concrete bypass example** that defeats this blacklist (e.g., encoding tricks, Unicode normalization).
> 3. Explain why whitelisting is fundamentally more secure than blacklisting. How does this relate to the Saltzer & Schroeder principle of **economy of mechanism**?
> 4. What is the **"input chokepoint" pattern**? How does centralizing validation at a single entry point reduce the attack surface?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### "All Input Is Evil Until Proven Otherwise"
>
> Howard's most influential maxim: treat all external input as potentially malicious . The implementation strategy:
>
> - **Whitelist over blacklist** — define what is allowed, reject everything else
> - **Input chokepoints** — centralized validation at system boundaries (not scattered throughout code)
> - **Canonical form** — normalize input before validation (prevent encoding attacks)
> - **Dangerous C functions** — never use `gets()`, `strcpy()`, `sprintf()`, `scanf()` without bounds checking
>
> Heartbleed (CVE-2014-0160) violated this principle: the OpenSSL heartbeat extension trusted the length field in the request without bounds checking, allowing attackers to read up to 64KB of server memory per heartbeat request . A 2-line bounds check would have prevented the vulnerability.
>
> #### 4.3 Input Validation
>
> Howard's foundational rule for secure coding :
>
> > "All input is evil until proven otherwise. The moment you forget this rule is the moment you are attacked."
>
> **Validation approach:**
>
> 1. **Identify** all input sources (user input, files, network, environment, databases)
> 2. **Specify** what constitutes valid data (format, range, length, type)
> 3. **Validate** using an **input chokepoint** — a single centralized validation point
> 4. **Handle** invalid data safely (reject, sanitize, or escape)
>
> **Whitelist vs. Blacklist:**
>
> | Approach | Method | Risk | Recommendation |
> |----------|--------|------|----------------|
> | **Blacklist** | Block known bad patterns | Misses new attack variants | **Avoid** |
> | **Whitelist** | Allow only known good patterns | May be more restrictive | **Prefer** |
>
> **Example:** Blacklisting `--` for SQL injection → attacker uses `/**/` comment syntax to bypass. **Whitelisting** `[A-Za-z0-9]` for usernames → any unexpected character is rejected regardless of attack technique.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/security/RQ_L10_Security.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/security/RQ_L10_Security.md)

### Card 344 — Q9: Pipeline Design

> [!question] Question
> **Q9: Pipeline Design**
>
> You are the DevSecOps engineer for a **microservices architecture** (12 services, CI/CD with GitHub Actions, deploying to Kubernetes).
>
> Design a security pipeline by specifying which tools run at each stage:
>
> | Stage | Tools/Checks | Max Time Budget |
> |-------|-------------|-----------------|
> | IDE (developer workstation) | ? | Instant feedback |
> | Pre-commit | ? | < 30 seconds |
> | Build (CI) | ? | < 5 minutes |
> | Test (CI) | ? | < 15 minutes |
> | Deploy (CD) | ? | < 2 minutes |
> | Operate (production) | ? | Continuous |
>
> (a) Rangnau 2020 measured that DAST adds **~14 minutes** to the pipeline. Where in your pipeline does DAST fit, and how do you prevent it from blocking deployments?
> (b) Rajapakse 2021 found only **~30% effectiveness** for automated security tools. With 12 services generating alerts, how do you handle **false positives** without creating alert fatigue?
> (c) What is the "shift-left" trade-off? Why can't ALL security testing shift to the IDE stage?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.2 DevSecOps Pipeline Metrics
>
> Rangnau et al. (2020) measured the practical overhead of security integration in CI/CD pipelines :
>
> | Metric | Value |
> |--------|-------|
> | Full pipeline time | **14 min 6 sec** |
> | ZAP container build | **6 min 52 sec** (49% of pipeline — bottleneck) |
> | WAST vulnerabilities found | 15 (including 1 High: SQL injection) |
> | SAS vulnerabilities found | 4 |
> | BDST findings | 60 (mostly Low severity) |
> | Effective results | **~30%** (rest are false positives) |
>
> **Pipeline configuration:** Configured to **fail and block** deployment when vulnerability thresholds are exceeded. This enforces a security gate but requires careful threshold tuning to avoid blocking legitimate releases.
>
> **Industry challenges** :
>
> | Challenge | Detail |
> |-----------|--------|
> | False positives | Only 30% of results are actionable |
> | Speed mismatch | SAST takes hours; DevOps cycles are minutes |
> | Tool age | Many tools built on 15-year-old scan models |
> | Alert fatigue | Teams stop trusting and start ignoring tools |
>
> #### 2.3 Dynamic Application Security Testing (DAST)
>
> DAST tests the running application from the outside, sending HTTP requests and analyzing responses:
>
> | Mode | Description | Strengths | Weaknesses |
> |------|-------------|-----------|------------|
> | **Passive** | Observe traffic, analyze responses | Non-disruptive, finds information leaks | Misses vulnerabilities requiring active probing |
> | **Active** | Send malicious payloads | Finds injection, XSS, misconfig | Can be disruptive, slower |
>
> **CI/CD integration metrics** (Rangnau 2020 ):
> - Full pipeline time: **14 min 6 sec**
> - ZAP container build: **6 min 52 sec** (pipeline bottleneck)
> - WAST vulnerabilities found: 15 (including 1 High SQLi)

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/security/RQ_L10_Security.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/security/RQ_L10_Security.md)

### Card 345 — Q10: Supply Chain Security

> [!question] Question
> **Q10: Supply Chain Security**
>
> Williams 2025 identifies **3 attack vectors** in software supply chains: dependencies, build infrastructure, and humans.
>
> For each vector, a real-world case demonstrates the threat:
>
> | Vector | Case | Year |
> |--------|------|------|
> | Dependencies | Log4Shell | 2021 |
> | Build infrastructure | SolarWinds | 2020 |
> | Humans (social engineering) | XZ Utils | 2024 |
>
> For each case:
> (a) Explain **how the attack worked** — what was the entry point, how did it propagate, and what was the impact?
> (b) Name **one specific countermeasure** that would have detected or prevented the attack
> (c) Explain how **SBOMs** (Software Bills of Materials) help with this attack vector — or explain their limitations if SBOMs would not have helped

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.5 Supply Chain Security
>
> Williams et al. (2025) identify three primary attack vectors in software supply chains :
>
> | Attack Vector | Description | Case Study |
> |---------------|-------------|------------|
> | **Dependencies** | Compromised or vulnerable third-party libraries | Log4Shell (Log4j embedded in thousands of products) |
> | **Build process** | Tampering with build systems or CI/CD | SolarWinds (malicious code injected during build) |
> | **Human factors** | Social engineering, insider threats, maintainer compromise | XZ Utils (multi-year social engineering of maintainer) |
>
> **Major supply chain incidents:**
>
> | Incident | Year | Vector | Impact |
> |----------|------|--------|--------|
> | **SolarWinds** | 2020 | Build compromise | 18,000 organizations, 9 months undetected  |
> | **Log4Shell** | 2021 | Vulnerable dependency | 93% of enterprise clouds vulnerable  |
> | **XZ Utils** | 2024 | Maintainer social engineering | Backdoor in compression library (caught before widespread deployment) |
>
> **Countermeasures:**
> - **Software Bill of Materials (SBOM):** Inventory of all dependencies
> - **SCA scanning:** Automated CVE checks on every build
> - **Build provenance:** Cryptographic attestation of build process (SLSA framework)
> - **Dependency pinning:** Lock specific versions, review updates
>
> #### Supply Chain Security
>
> Williams et al. (2025) identify three attack vectors threatening the entire DevSecOps model :
>
> | Vector | Attack Type | Case Study |
> |--------|------------|------------|
> | **Dependencies** | Malicious or vulnerable components | Log4Shell — accidental vulnerability in ubiquitous library  |
> | **Build infrastructure** | Compromised CI/CD pipeline | SolarWinds — malicious code injected during build  |
> | **Humans** | Social engineering of maintainers | XZ Utils — years-long social engineering to insert backdoor |
>
> Countermeasures include:
> - **SBOMs** (Software Bills of Materials) — inventory all dependencies; adoption accelerated by Log4Shell
> - **Automated VEX** — reachability analysis to reduce false positives
> - **Reproducible builds** — verify that binary matches source code
> - **ML-based detection** — identify malicious commits and dependency patterns

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/security/RQ_L10_Security.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/security/RQ_L10_Security.md)

### Card 346 — Q11: CVSS Analysis — Prioritizing Patches

> [!question] Question
> **Q11: CVSS Analysis — Prioritizing Patches**
>
> A vulnerability in your company's web framework receives the following CVSS v3.1 scores:
>
> **Base Score: 8.1 (High)**
> `AV:N / AC:H / PR:N / UI:N / S:U / C:H / I:H / A:H`
>
> **Temporal Score: 7.1**
> - Exploit Code Maturity: Unproven (multiplier 0.91)
> - Remediation Level: Official Fix available (multiplier 0.95)
> - Report Confidence: Confirmed (multiplier 1.00)
> - Calculation: Roundup(8.1 × 0.91 × 0.95 × 1.00) = Roundup(7.002) = **7.1**
>
> **Environmental Score: 4.0**
> - The affected component handles only **public, non-sensitive data**
> - The system is behind a WAF with rate limiting
>
> (a) Explain what each **metric group** (Base, Temporal, Environmental) tells you and why the score drops from 8.1 → 7.1 → 4.0.
> (b) Based on these scores, should you **patch immediately** (emergency change) or **schedule for next sprint** (2 weeks)? Justify your decision.
> (c) Compare with **Log4Shell** (CVSS Base 10.0, `AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`). Both vulnerabilities are "network accessible" — why was Log4Shell vastly more urgent? Identify the **2 specific CVSS base metric differences**, then explain how **temporal factors** at the time of Log4Shell's disclosure (exploit code maturity, remediation availability) constitute a third dimension of urgency.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.7 CVSS: Quantifying Risk on a 0-10 Scale
>
> The Common Vulnerability Scoring System (CVSS) provides a standardized way to assess vulnerability severity  :
>
> **Three metric groups:**
>
> | Group | Measures | Set By | Changes Over Time? |
> |-------|----------|--------|-------------------|
> | **Base** (0-10) | Exploitability + Impact | Analyst | No |
> | **Temporal** | Exploit maturity, patch availability | Vendor | Yes |
> | **Environmental** | Target distribution, CIA requirements | User organization | Per deployment |
>
> **Severity scale:**
>
> | Rating | Score Range | Example |
> |--------|------------|---------|
> | None | 0.0 | Informational finding |
> | Low | 0.1 – 3.9 | Minor information disclosure |
> | Medium | 4.0 – 6.9 | Cross-site scripting |
> | High | 7.0 – 8.9 | Heartbleed (CVSS 7.5) |
> | **Critical** | **9.0 – 10.0** | **Log4Shell (CVSS 10.0)** |
>
> **Example: Log4Shell (CVE-2021-44228)** :
>
> | Base Metric | Value | Rationale |
> |-------------|-------|-----------|
> | Attack Vector | Network | Exploitable remotely |
> | Attack Complexity | Low | No special conditions needed |
> | Privileges Required | None | No authentication required |
> | User Interaction | None | No user action needed |
> | Scope | Changed | Impacts beyond vulnerable component |
> | Confidentiality Impact | High | Full read access |
> | Integrity Impact | High | Full write access |
> | Availability Impact | High | Complete denial of service |
> | **Base Score** | **10.0 (Critical)** | Maximum severity |
>
> #### CVSS: Scoring Vulnerability Severity
>
> The Common Vulnerability Scoring System quantifies vulnerability severity on a 0-10 scale using three metric groups  :
>
> | Metric Group | What It Measures | When Applied |
> |-------------|-----------------|--------------|
> | **Base** | Intrinsic vulnerability characteristics (attack vector, complexity, impact on CIA) | At disclosure |
> | **Temporal** | How the threat evolves over time (exploit maturity, patch availability) | Over time |
> | **Environmental** | Organization-specific context (asset criticality, existing mitigations) | Per deployment |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/security/RQ_L10_Security.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/security/RQ_L10_Security.md)

### Card 347 — Q12: Comprehensive Case Analysis — Security Architect Challenge

> [!question] Question
> **Q12: Comprehensive Case Analysis — Security Architect Challenge**
>
> You are the **security architect** for a fintech company processing $2M in daily transactions. A penetration test reveals three findings:
>
> 1. **SQL injection** in the payment API (CVSS 9.8) — parameterized queries not used in 3 endpoints
> 2. **Vulnerable Log4j dependency** (v2.14.1) in the logging service — known RCE exploit available
> 3. **No threat model** exists for the authentication and authorization flow
>
> Using the lecture's frameworks, create a **remediation plan** with three horizons:
>
> **Immediate (this week):**
> - Which finding do you fix first and why? (Consider CVSS scores, exploit availability, blast radius)
> - What emergency mitigations can you deploy before the code fix is ready?
>
> **Short-term (this quarter):**
> - How do you integrate security into the SDLC to prevent recurrence?
> - Which DevSecOps tools would catch each of the 3 findings automatically?
> - How do you address the <1% security comment rate in code reviews (Yu 2023)?
>
> **Long-term (this year):**
> - Design the threat modeling program: which method, what cadence, who participates?
> - How do you implement supply chain security (SBOMs, dependency scanning, build verification)?
> - Reference at least **3 specific frameworks or methods** from the lecture in your plan

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.5 Supply Chain Security
>
> Williams et al. (2025) identify three primary attack vectors in software supply chains :
>
> | Attack Vector | Description | Case Study |
> |---------------|-------------|------------|
> | **Dependencies** | Compromised or vulnerable third-party libraries | Log4Shell (Log4j embedded in thousands of products) |
> | **Build process** | Tampering with build systems or CI/CD | SolarWinds (malicious code injected during build) |
> | **Human factors** | Social engineering, insider threats, maintainer compromise | XZ Utils (multi-year social engineering of maintainer) |
>
> **Major supply chain incidents:**
>
> | Incident | Year | Vector | Impact |
> |----------|------|--------|--------|
> | **SolarWinds** | 2020 | Build compromise | 18,000 organizations, 9 months undetected  |
> | **Log4Shell** | 2021 | Vulnerable dependency | 93% of enterprise clouds vulnerable  |
> | **XZ Utils** | 2024 | Maintainer social engineering | Backdoor in compression library (caught before widespread deployment) |
>
> **Countermeasures:**
> - **Software Bill of Materials (SBOM):** Inventory of all dependencies
> - **SCA scanning:** Automated CVE checks on every build
> - **Build provenance:** Cryptographic attestation of build process (SLSA framework)
> - **Dependency pinning:** Lock specific versions, review updates
>
> #### Supply Chain Security
>
> Williams et al. (2025) identify three attack vectors threatening the entire DevSecOps model :
>
> | Vector | Attack Type | Case Study |
> |--------|------------|------------|
> | **Dependencies** | Malicious or vulnerable components | Log4Shell — accidental vulnerability in ubiquitous library  |
> | **Build infrastructure** | Compromised CI/CD pipeline | SolarWinds — malicious code injected during build  |
> | **Humans** | Social engineering of maintainers | XZ Utils — years-long social engineering to insert backdoor |
>
> Countermeasures include:
> - **SBOMs** (Software Bills of Materials) — inventory all dependencies; adoption accelerated by Log4Shell
> - **Automated VEX** — reachability analysis to reduce false positives
> - **Reproducible builds** — verify that binary matches source code
> - **ML-based detection** — identify malicious commits and dependency patterns

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/attributes/security/RQ_L10_Security.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/attributes/security/RQ_L10_Security.md)

## Cost of Quality (10)

### Card 348 — Question 1: Why Cost of Quality Matters

> [!question] Question
> **Question 1: Why Cost of Quality Matters**
>
> Why is it important to express software quality issues in financial terms rather than technical metrics?
>
> Give an example of how you would reframe a technical quality problem (e.g., "fault density increased") into business language for management.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Cost of Software Quality Foundations
>
> The Cost of Software Quality (CoSQ) provides a financial framework for organizations to translate technical quality metrics into a business vocabulary—money—that executives and upper management can use for data-driven decision-making  .
>
> #### Cost of Quality
>
> The Cost of Software Quality (CoSQ) provides a financial framework for translating technical quality metrics into business vocabulary that executives can use for data-driven decision-making.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/01-coq/RQ-A1-CoSQ.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/01-coq/RQ-A1-CoSQ.md)

### Card 349 — Question 2: The Four CoQ Categories

> [!question] Question
> **Question 2: The Four CoQ Categories**
>
> The Cost of Quality framework divides costs into four categories: Prevention, Appraisal, Internal Failure, and External Failure.
>
> Explain the difference between **conformance costs** and **nonconformance costs**. For each of the four categories, give one concrete example from a software development project.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The Four Categories
>
> ```mermaid
> flowchart TD
>     CoQ["💰 <b>Cost of Quality</b>"]
>
>     CoQ --> Conf
>     CoQ --> NonConf
>
>     subgraph Conf["✅ Conformance Costs"]
>         direction TB
>         Prev["🛡️ <b>1. Prevention</b>"]
>         Appr["🔍 <b>2. Appraisal</b>"]
>
>         Prev --- P1[Training] & P2[Reviews] & P3[Tools]
>         Appr --- A1[Testing] & A2[Inspections] & A3[Audits]
>     end
>
>     subgraph NonConf["❌ Nonconformance Costs"]
>         direction TB
>         IntF["🔧 <b>3. Internal Failure</b>"]
>         ExtF["💥 <b>4. External Failure</b>"]
>
>         IntF --- I1[Rework] & I2[Retesting] & I3[Debugging]
>         ExtF --- E1[Support] & E2[Patches] & E3[📉 Hidden costs]
>     end
> ```
>
> #### Internal Failure Costs
>
> The cost of correcting defects discovered before the product leaves the manufacturer :
> - Defect management
> - Redesign and rework
> - Retesting after failure detection

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/01-coq/RQ-A1-CoSQ.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/01-coq/RQ-A1-CoSQ.md)

### Card 350 — Question 3: Prevention vs Appraisal

> [!question] Question
> **Question 3: Prevention vs Appraisal**
>
> Weinberg observed: "When managers say 'Testing takes too long,' what they should be saying is 'Fixing the bugs takes too long.'"
>
> Explain the difference between **appraisal costs** and **internal failure costs** using this insight. Why is this distinction important for quality planning?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The Weinberg Insight
>
> > "When managers say, 'Testing takes too long,' what they should be saying is, 'Fixing the bugs in the product takes too long'—a different cost category." — G. Weinberg, _Perfect Software And Other Illusions About Testing_ (2010)
>
> **Key distinction:**
>
> - Testing = **Appraisal** cost (finding defects)
> - Debugging/Rework = **Internal failure** cost (fixing defects)
>
> The complaint "we don't have time to test" really means "we'd rather spend time fixing in production"—which is far more expensive.
>
> > Extended discussion on PAF model history and applications is available in
> > supplementary notes: [CoSQ Foundations](01-cosq-foundations.md)
>
> #### Internal Failure Costs
>
> The cost of correcting defects discovered before the product leaves the manufacturer :
> - Defect management
> - Redesign and rework
> - Retesting after failure detection

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/01-coq/RQ-A1-CoSQ.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/01-coq/RQ-A1-CoSQ.md)

### Card 351 — Question 4: The 1:10:100 Rule

> [!question] Question
> **Question 4: The 1:10:100 Rule**
>
> The 1:10:100 rule states that fixing a defect costs $1 in requirements, $10 in development, and $100+ after release.
>
> Explain why this cost escalation occurs. How does "shift-left" testing leverage this principle to reduce total CoQ?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The 1:10:100 Rule
>
> Classification schemes prove that a defect caught in requirements ($1) is 100× cheaper than one found after release ($100+), justifying the "front-loading" of quality processes .
>
> ```mermaid
> xychart-beta
>     title "Cost to Fix Defect by Phase (1:10:100 Rule)"
>     x-axis [Requirements, Development, Post-Release]
>     y-axis "Relative Cost ($)" 0 --> 120
>     bar [1, 10, 100]
> ```
>
> #### Shift-Left Testing: Early Defect Detection
>
> The Shift-Left paradigm emphasizes moving testing activities earlier in the development process to detect defects when they are cheaper and easier to fix :

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/01-coq/RQ-A1-CoSQ.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/01-coq/RQ-A1-CoSQ.md)

### Card 352 — Question 5: Traditional vs Modern CoQ Models

> [!question] Question
> **Question 5: Traditional vs Modern CoQ Models**
>
> The traditional CoQ model (1950s-1970s) suggested there is an optimal quality level below 100% conformance. The modern model (Kondo, Juran) argues the optimum can extend toward 100%.
>
> What is the key difference in assumptions between these models? What does Knox mean by "do something different"?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Traditional vs. Modern CoQ Models
>
> **Traditional Model (1950s–1970s):**
>
> - Costs of achieving quality and costs due to lack of quality have an inverse relationship
> - Total CoQ has a **point of diminishing returns**—a minimum _prior to_ 100% quality
> - Premise: If you continue doing more of the same, you eventually hit negative returns
>
> **Modern Model (Kondo 1978, Juran & Gryna 1988):**
>
> - Manufacturing experience showed increased attention to prevention leads to large reductions in appraisal costs
> - The minimum Total CoQ can extend toward 100% conformance
> - Premise: You do something **different**—improve your process—rather than just doing more of the same
>
> > **Key insight from Knox (1993):** "You will not experience a point of diminishing returns from investing in quality-attaining processes." The revised model suggests the optimum can shift toward 100% conformance through **process improvement** .
>
> #### The Traditional CoSQ Model
>
> Based on the foundational work of Campanella (1999) and Juran, the CoSQ model categorizes quality-related costs into four distinct buckets, which were later specifically adapted for software by researchers like Houston and Keats (1999)  :

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/01-coq/RQ-A1-CoSQ.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/01-coq/RQ-A1-CoSQ.md)

### Card 353 — Question 6: Process Maturity and CoQ

> [!question] Question
> **Question 6: Process Maturity and CoQ**
>
> Raytheon's empirical data showed that moving from CMM Level 1 to Level 3 reduced total CoSQ from ~65% to ~20% of project costs.
>
> Which CoQ category showed the largest reduction? Explain why process improvement has this effect on the cost structure.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Empirical Validation: Knox and Raytheon
>
> **Knox's Hypothesis (1993)** — Hewlett Packard:
>
> - As process maturity increases (CMM Level 1 → 5), total CoSQ decreases
> - Prevention and appraisal costs remain relatively stable
> - Failure costs drop dramatically
>
> **Raytheon Empirical Data (1996):** Real data validated Knox's hypothesis :
>
> |Metric|CMM Level 1 (1987)|CMM Level 3 (1996)|
> |---|---|---|
> |Total CoSQ|~65% of project|~20% of project|
> |Rework|~50%|<10%|
>
> **Result:** Fourfold reduction in rework over 8 years of process improvement.
>
> > Modern applications of quality economics in CI/CD and DevOps are explored in
> > supplementary notes: [Quality Economics in DevOps](04-quality-economics-devops.md)
>
> #### Empirical Evidence: Raytheon Case Study
>
> Real-world data from Raytheon showed significant improvements with process maturity :
>
> | Metric | CMM Level 1 | CMM Level 3 |
> |--------|-------------|-------------|
> | Total CoSQ (% of project) | ~65% | ~20% |
> | Rework (failure costs) | ~50% | <10% |
>
> This represents:
> - **3x reduction** in total CoSQ
> - **5x reduction** in rework costs

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/01-coq/RQ-A1-CoSQ.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/01-coq/RQ-A1-CoSQ.md)

### Card 354 — Question 7: Tank and Pipes Model

> [!question] Question
> **Question 7: Tank and Pipes Model**
>
> The "tank and pipes" model visualizes defects flowing into a system (injection) and being removed through V&V activities (removal).
>
> Draw or describe this model and explain what "residual defects" represent. Why is it important to track both injection and removal rates?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The "Tank and Pipes" Model
>
> This model, proposed by Capers Jones and formalized in COQUALMO , visualizes defect flow:
>
> ```mermaid
> flowchart LR
>     subgraph Injection["🔴 INJECTION"]
>         direction TB
>         R[Requirements<br>+10]
>         D[Design<br>+20]
>         C[Code<br>+50]
>     end
>
>     R --> T
>     D --> T
>     C --> T
>
>     T[("🪣<br>Defect Pool<br>(80)")]
>
>     T --> Rev
>     T --> UT
>     T --> IT
>     T --> ST
>     T -->|"5 escape"| EXT[💥 Field<br>Failure]
>
>     subgraph Removal["🟢 REMOVAL"]
>         direction TB
>         Rev[Reviews<br>−30]
>         UT[Unit Test<br>−20]
>         IT[Int Test<br>−15]
>         ST[Sys Test<br>−10]
>     end
> ```
>
> **Key concepts:**
>
> - **Injection pipes:** Defects flow INTO the system at each development phase
> - **The tank:** Cumulative "backlog" of defects residing in the system
> - **Removal pipes:** V&V activities act as filters, removing defects
> - **Residual defects:** What remains after all removal activities—these become field defects
>
> #### The "Tank and Pipes" Model
>
> Originally proposed by Capers Jones in 1975, this is the simplest model for understanding defect flow through the development process :

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/01-coq/RQ-A1-CoSQ.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/01-coq/RQ-A1-CoSQ.md)

### Card 355 — Question 8: Improvement Strategies

> [!question] Question
> **Question 8: Improvement Strategies**
>
> You have two options to reduce field defects:
> - **Option A:** Improve unit testing effectiveness from 50% to 70%
> - **Option B:** Add code inspections that catch 20% of defects before testing
>
> Both achieve the same residual defect count. Which option is more cost-effective and why?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Comparing Improvement Approaches
>
> **Scenario A: Improve Unit Testing by 20%**
>
> - UT effectiveness: 50% → 70%
> - IT and ST remain at 50%
> - Result: 6 defects reach customer (vs. 10 baseline)
>
> **Scenario B: Add Inspections (20% removal each)**
>
> - Requirements inspection → catches defects at source
> - Design inspection → catches design defects early
> - Code inspection → catches code defects before testing
> - Result: 6 defects reach customer (vs. 10 baseline)
>
> **Both achieve same residual count, but:**
>
> - Scenario A: Finds defects later (higher fix cost per defect)
> - Scenario B: Finds defects earlier (lower fix cost per defect)
>
> > **How do you choose?** Analyze the cost of each alternative AND the likelihood of achieving the assumed improvements. A 10–20% improvement is achievable; a 2× improvement is unlikely unless current processes are severely broken .
>
> For detailed analysis of code review effectiveness and ROI calculations, see
> supplementary notes: [Code Review ROI](05-code-review-roi.md)
>
> #### Shift-Left Testing: Early Defect Detection
>
> The Shift-Left paradigm emphasizes moving testing activities earlier in the development process to detect defects when they are cheaper and easier to fix :

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/01-coq/RQ-A1-CoSQ.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/01-coq/RQ-A1-CoSQ.md)

### Card 356 — Question 9: Making CoQ Actionable

> [!question] Question
> **Question 9: Making CoQ Actionable**
>
> To implement a CoQ program, you need data from multiple sources.
>
> List three data sources for CoQ measurement and explain what quality cost information each provides. Why is defect classification (origin phase, detection phase, type) essential for improvement?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Defect Classification Basics
>
> To make CoQ actionable, you need to classify defects systematically.
> At minimum, track:
>
> 1. **Origin phase** — Where was the defect injected? (Requirements, Design, Code)
> 2. **Detection phase** — Where was it found? (Review, Unit Test, System Test, Field)
> 3. **Defect type** — What kind of defect? (Logic, Interface, Data, Timing)
>
> **Kan's Origin/Where Found Matrix** cross-tabulates origin vs detection:
> - Defects on the diagonal are caught early (low cost)
> - Defects far from diagonal escaped multiple phases (high cost)
> - Patterns reveal which phases need stronger V&V
>
> > Detailed classification schemes (ODC, HP Model) are covered in
> > supplementary notes: [Defect Classification](03-defect-classification.md)
>
> #### Actionability for CoQ
>
> The matrix directly supports Cost of Quality decisions:
>
> | If you see... | It means... | Invest in... |
> |---------------|-------------|--------------|
> | High Field column | V&V not catching defects | More/earlier inspections |
> | High row total, low early columns | Injection > early removal | Prevention at that phase |
> | Defects far from diagonal | Late detection of early bugs | Shift-left activities |
>
> > **Connection to lecture:** This is the minimum classification needed to make CoQ actionable. Without knowing origin and detection phase, you can't target prevention investments.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/01-coq/RQ-A1-CoSQ.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/01-coq/RQ-A1-CoSQ.md)

### Card 357 — Question 10: Technical Debt and CoQ

> [!question] Question
> **Question 10: Technical Debt and CoQ**
>
> Technical debt can be viewed as a form of deferred quality cost.
>
> Explain how technical debt relates to the CoQ framework. What are the implications of quantifying technical debt as an increase in the "cost of change"?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Potential Technical Debt (PTD) Detection
>
> Fu et al. (2022) defined Potential Technical Debt (PTD) as sub-optimal implementations identified during review that can be resolved **before** being merged into the codebase :
>
> #### Technical Debt Quantification
>
> Technical Debt (TD) Quantification is a critical aspect of software quality management that translates technical inefficiencies into measurable effort and business risk  . Current research highlights significant challenges in how debt is identified by automated tools versus how it is admitted by developers in specialized domains like Machine Learning.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/01-coq/RQ-A1-CoSQ.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/01-coq/RQ-A1-CoSQ.md)

## Quality Planning (17)

### Card 358 — Question 1: Quality as an Afterthought

> [!question] Question
> **Question 1: Quality as an Afterthought**
>
> Wallace and Fujii (1989) found that only 10% of test plan topics were actually addressed in surveyed projects.
>
> Explain why quality activities are often skipped. What pressures cause teams to deprioritize testing? How does Google's approach (Test Certified from Day 1) prevent this problem?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.1 Quality as an Afterthought
>
> **The Problem:**
>
> > "Why do we put emphasis on a quality plan? Because in most situations quality is an afterthought."
>
> Wallace and Fujii's 1989 study found that only 10% of test plan topics were actually addressed in surveyed projects. When development and quality roles are combined, quality activities become the first casualty of schedule pressure.
>
> **Why Quality Gets Skipped:**
>
> | Pressure | Result |
> |----------|--------|
> | Deadline approaching | "We'll test later" |
> | Budget cuts | "Testing is overhead" |
> | Feature creep | "No time for tests" |
> | Optimism bias | "Our code doesn't have bugs" |
>
> **The Core Insight:**
> Without a plan, quality activities compete with features for time and resources—and features always win. The solution is to build quality activities into the process so they cannot be skipped.
>
> #### 5.3 Google Test Certified Levels
>
> Google's internal Test Certified program defines progressive maturity :
>
> | Level | Requirements |
> |-------|--------------|
> | **L1** | CI build, tests classified by size, smoke suite, flaky tests identified |
> | **L2** | No red tests at release, smoke tests pass before submit |
> | **L3** | Tests required for all nontrivial changes |
> | **L4** | Pre-submit automation runs in <30 minutes |
> | **L5** | Bug fix = regression test, 60% total coverage, 40% small tests |
>
> **Your Target:**
> - **SQR Project:** Reach Level 2 (CI green, smoke tests)
> - **IPP:** Reach Level 3 (tests required for all changes)

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

### Card 359 — Question 2: The 11 Decisions Framework

> [!question] Question
> **Question 2: The 11 Decisions Framework**
>
> A complete quality plan must address 11 decisions grouped into WHAT, WHEN, WHO, and HOW.
>
> List and briefly explain at least 8 of the 11 decisions. For a student project (SQR), which decisions are most critical to address?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.1 What a Quality Plan Must Address
>
> A Quality Plan documents 11 key decisions :
>
> | # | Decision | Question |
> |---|----------|----------|
> | 1 | **Activities** | What QA, QC, and improvement activities will we conduct? |
> | 2 | **Interactions** | How do quality activities connect to development activities? |
> | 3 | **Artifacts** | Which work products will activities apply to? |
> | 4 | **Timing** | When will activities occur? |
> | 5 | **Responsibility** | Who performs each activity? |
> | 6 | **Extent** | To what depth/breadth? |
> | 7 | **Cost/Time** | What are up-front and recurring costs? |
> | 8 | **Tools** | What tooling is required? |
> | 9 | **Training** | What skills and training are needed? |
> | 10 | **Defect Handling** | How are defects reported, tracked, resolved? |
> | 11 | **Measurements** | What metrics provide visibility into processes? |
>
> **Rule:** A complete quality plan addresses ALL 11 decisions. Missing any creates gaps.
>
> #### 11 Decisions in a Quality Plan
>
> A Quality Plan documents the following decisions:
>
> 1. **Activities** — QA, QC, and improvement activities to be conducted
> 2. **Interactions** — Between quality activities and development activities
> 3. **Artifacts** — Which work products will activities apply to
> 4. **Timing** — When activities will occur
> 5. **Responsibility** — Who performs each activity
> 6. **Extent** — To what depth/breadth
> 7. **Cost/Time** — Up-front and recurring costs
> 8. **Tools** — Required tooling
> 9. **Training** — Required skills and training
> 10. **Defect Handling** — How defects are reported, tracked, resolved
> 11. **Measurements** — Metrics providing visibility into processes

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

### Card 360 — Question 3: Quality Assurance vs Quality Control

> [!question] Question
> **Question 3: Quality Assurance vs Quality Control**
>
> Quality management includes both QA and QC activities.
>
> Explain the fundamental difference between Quality Assurance and Quality Control. Give one example of each. Why do you need both?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.2 Four Components of Quality Management
>
> A complete quality management approach includes four components :
>
> | Component | Purpose | Examples |
> |-----------|---------|----------|
> | **Quality Planning** | Identify activities, tools, training; organize execution | Test plan, quality gates, RACI matrix |
> | **Quality Assurance** | Provide confidence product *will* meet requirements | Process audits, reviews, standards |
> | **Quality Control** | Verify product *is* of required quality | Testing, inspections, static analysis |
> | **Quality Improvement** | Enhance process effectiveness | Retrospectives, root cause analysis |
>
> **Key Distinction:**
> - **Quality Assurance (QA):** Process-focused, preventive ("Are we doing things right?")
> - **Quality Control (QC):** Product-focused, detective ("Did we make the thing right?")
>
> #### Four Components of Quality Management
>
> | Component | Purpose |
> |-----------|---------|
> | **Quality Planning** | Identify required activities, tools, training; organize execution |
> | **Quality Assurance** | Activities to provide confidence that a product *will* fulfill requirements |
> | **Quality Control** | Activities to verify that a product *is* of required quality |
> | **Quality Improvement** | Enhancement of process effectiveness and efficiency |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

### Card 361 — Question 4: Criticality Levels

> [!question] Question
> **Question 4: Criticality Levels**
>
> DO-178B defines 5 criticality levels (A-E) for avionic software, while ISO 26262 uses ASIL (A-D plus QM).
>
> Explain what determines a system's criticality level. If you're building a web app (Level E/QM) vs. airplane software (Level A), how would your coverage requirements differ?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.1 Criticality Levels
>
> Not all software needs the same level of rigor. Criticality determines how much testing is required.
>
> **DO-178B Avionic Software Criticality:**
>
> | Level | Safety Impact | Coverage Requirement |
> |-------|--------------|---------------------|
> | **A** | Catastrophic failure | 100% Modified Condition/Decision Coverage (MC/DC) |
> | **B** | Hazardous/severe failure | 100% Decision Coverage |
> | **C** | Major failure | 100% Statement Coverage |
> | **D** | Minor failure | 100% Requirements Coverage |
> | **E** | No adverse effect | No coverage requirements |
>
> **ISO 26262 ASIL (Automotive):**
>
> | Level | Example Systems |
> |-------|-----------------|
> | **D** | Steering, brakes (highest) |
> | **C** | Airbags |
> | **B** | Headlights |
> | **A** | Wipers (lowest safety) |
> | **QM** | Infotainment (quality managed, no safety) |
>
> **Key Insight:** Your web app is probably QM/Level E. Don't over-engineer. Don't under-engineer.
>
> #### DO-178B Avionic Software Criticality
>
> | Level | Safety Impact | Coverage Requirement |
> |-------|--------------|---------------------|
> | **A** | Catastrophic failure | 100% Modified Condition/Decision Coverage (MC/DC) |
> | **B** | Hazardous/severe failure | 100% Decision Coverage |
> | **C** | Major failure | 100% Statement Coverage |
> | **D** | Minor failure | 100% Requirements Coverage |
> | **E** | No adverse effect | No coverage requirements |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

### Card 362 — Question 5: Microsoft Coverage by Milestone

> [!question] Question
> **Question 5: Microsoft Coverage by Milestone**
>
> Microsoft targets 65% coverage at M2, 75% at M3, and 80% at Release.
>
> Why do coverage targets increase toward release rather than staying constant? What does each milestone focus on?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.3 Microsoft Coverage by Milestone
>
> Coverage targets should **increase** as you approach release :
>
> | Milestone | Coverage | Bug Bar | Other Criteria |
> |-----------|----------|---------|----------------|
> | **M1** | — | P1 bugs fixed | Feature spec complete |
> | **M2** | **65%** | 60% crashes fixed | Threat model mitigated |
> | **M3** | **75%** | 70% crashes fixed | Performance baseline met |
> | **Release** | **80%** | All P1/P2 fixed | All mandatory policies |
>
> **Why This Works:**
> - Early milestones: Focus on building features
> - Later milestones: Focus on stabilizing quality
> - Release: High bar, no exceptions
>
> #### 3.2 Coverage Targets by Criticality
>
> Quality gates should be tailored to artifact criticality :
>
> | Condition | Low (C) | Medium (B) | High (A) |
> |-----------|---------|------------|----------|
> | Coverage type | Statement | Branch | Basis paths |
> | Code inspections | No | Yes | Yes |
> | Coding standards | Yes | Yes | Yes |
> | Testing strength | All pairs | All triples | All quadruples |
> | Cyclomatic complexity | <20 | <20 | <15 |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

### Card 363 — Question 6: Quality Gates Entry/Exit Criteria

> [!question] Question
> **Question 6: Quality Gates Entry/Exit Criteria**
>
> Quality gates have entry criteria (before starting) and exit criteria (before proceeding).
>
> For a "Code Review" gate, list at least 2 entry criteria and 2 exit criteria. What are the possible decisions (Pass, Conditional, Fail, Suspend) and when would each apply?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.2 Entry and Exit Criteria
>
> Every quality gate has entry criteria (before starting) and exit criteria (before proceeding) :
>
> **Entry Criteria (before starting):**
> - Spec approved
> - Environment ready
> - Reviewers assigned
> - Test data prepared
>
> **Exit Criteria (before proceeding):**
> - All tests pass
> - Coverage met
> - No Sev-1 bugs
> - Code review approved
>
> **Gate Decisions:**
>
> | Decision | Meaning |
> |----------|---------|
> | **Pass** | All criteria met, proceed |
> | **Conditional** | Minor issues, proceed with plan |
> | **Fail** | Major issues, must fix |
> | **Suspend** | Blocking issues, escalate |
>
> #### Entry and Exit Criteria
>
> IEEE 829-2008 specifies that test plans must define :
>
> - **Pass/Fail Criteria** — Criteria for determining if a test item passed or failed (typically based on anomaly count/severity)
> - **Suspension Criteria** — When to pause testing (e.g., defects make further testing valueless)
> - **Resumption Criteria** — What must be done to restart testing
>
> **Principle:** Define entry/exit criteria according to artifact criticality.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

### Card 364 — Question 7: Google's Three-Stage Gates

> [!question] Question
> **Question 7: Google's Three-Stage Gates**
>
> Google uses Pre-submit, Post-submit, and Release gates.
>
> Describe what happens at each gate. What checks are automated vs. manual? Why is the 80% incremental coverage requirement important at pre-submit?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.3 Google's 3-Stage Quality Gates
>
> Google uses a three-stage gate system :
>
> | Gate | When | Checks | Who |
> |------|------|--------|-----|
> | **Pre-submit** | Before merge | Static analysis, unit tests, 80% coverage | Automated |
> | **Post-submit** | After merge | Integration tests, affected tests | CI system |
> | **Release** | Before deploy | E2E, canary 1%, error budget | Ship Room |
>
> **Pre-submit Gate Details:**
> - Code review approved (readability certified)
> - Static analysis clean (Tricorder)
> - All unit tests pass
> - 80% incremental coverage
>
> #### 2.3 How Google Addresses the 11 Decisions
>
> | Decision | Google's Answer  |
> |----------|-------------------------------------------|
> | **What activities?** | Test pyramid: 70% unit, 20% integration, 10% E2E |
> | **What coverage?** | 80% target, tracked per project |
> | **What tools?** | Tricorder (static analysis), TAP (150M tests/day) |
> | **When to test?** | Pre-submit gates (before merge) |
> | **What gates?** | Pre-submit → Post-submit → Release |
> | **Who tests?** | "You build it, you break it" (developers) |
> | **What roles?** | SWE + SET + TE structure |
> | **How to test?** | Test Certified requirements per level |
> | **What standards?** | Readability certification, style guides |
>
> **Your Turn:** Map YOUR project's answers to these 11 decisions.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

### Card 365 — Question 8: Test Process Maturity (TMMi)

> [!question] Question
> **Question 8: Test Process Maturity (TMMi)**
>
> TMMi defines 5 maturity levels from Initial to Optimization.
>
> Describe levels 1, 2, and 3. For a student project, what is a realistic target level? What distinguishes a Level 2 team from a Level 3 team?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.1 Test Process Maturity Levels
>
> A systematic review identified 17 testing process models, most defining 5 maturity levels :
>
> | Level | TMMi Name | Key Characteristics |
> |-------|-----------|---------------------|
> | **1** | Initial | Ad hoc, chaotic, hero-dependent |
> | **2** | Managed | Test planning exists, tracked |
> | **3** | Defined | Standardized process, documented |
> | **4** | Measured | Metrics collected, analyzed |
> | **5** | Optimization | Continuous improvement |
>
> **Most student projects are Level 1-2. Goal: Reach Level 2-3.**
>
> **Key Insight:** You don't need Level 5. You need the RIGHT level for your context.
>
> #### 5.3 Google Test Certified Levels
>
> Google's internal Test Certified program defines progressive maturity :
>
> | Level | Requirements |
> |-------|--------------|
> | **L1** | CI build, tests classified by size, smoke suite, flaky tests identified |
> | **L2** | No red tests at release, smoke tests pass before submit |
> | **L3** | Tests required for all nontrivial changes |
> | **L4** | Pre-submit automation runs in <30 minutes |
> | **L5** | Bug fix = regression test, 60% total coverage, 40% small tests |
>
> **Your Target:**
> - **SQR Project:** Reach Level 2 (CI green, smoke tests)
> - **IPP:** Reach Level 3 (tests required for all changes)

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

### Card 366 — Question 9: Google Test Certified Levels

> [!question] Question
> **Question 9: Google Test Certified Levels**
>
> Google's Test Certified program has 5 levels (L1-L5).
>
> Compare Level 1 requirements with Level 3 requirements. If your team currently has no CI, what steps would you take to reach Level 2?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Google Test Certified Levels
>
> Google's internal Test Certified program defines progressive maturity :
>
> | Level | Requirements |
> |-------|--------------|
> | **L1** | CI build, tests classified by size, smoke suite, flaky tests identified |
> | **L2** | No red tests at release, smoke tests pass before submit |
> | **L3** | Tests required for all nontrivial changes |
> | **L4** | Pre-submit automation runs in <30 minutes |
> | **L5** | Bug fix = regression test, 60% total coverage, 40% small tests |
>
> **Your Target:**
> - **SQR Project:** Reach Level 2 (CI green, smoke tests)
> - **IPP:** Reach Level 3 (tests required for all changes)
>
> #### 5.1 Test Process Maturity Levels
>
> A systematic review identified 17 testing process models, most defining 5 maturity levels :
>
> | Level | TMMi Name | Key Characteristics |
> |-------|-----------|---------------------|
> | **1** | Initial | Ad hoc, chaotic, hero-dependent |
> | **2** | Managed | Test planning exists, tracked |
> | **3** | Defined | Standardized process, documented |
> | **4** | Measured | Metrics collected, analyzed |
> | **5** | Optimization | Continuous improvement |
>
> **Most student projects are Level 1-2. Goal: Reach Level 2-3.**
>
> **Key Insight:** You don't need Level 5. You need the RIGHT level for your context.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

### Card 367 — Question 10: The RACI Matrix

> [!question] Question
> **Question 10: The RACI Matrix**
>
> A RACI matrix assigns Responsible, Accountable, Consulted, and Informed roles.
>
> For unit testing in a typical team, who should be R (Responsible)? Why does Google say "You build it, you break it"? Create a RACI row for "Release decision."

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.4 RACI: Who Does What?
>
> | Activity | Dev | Tester | PM | QA |
> |----------|:---:|:------:|:--:|:--:|
> | Write unit tests | **R** | C | I | I |
> | Write integration tests | C | **R** | I | I |
> | Code review | **R** | C | I | I |
> | Run CI | A | **R** | I | I |
> | Triage bugs | C | **R** | **A** | C |
> | Release decision | C | C | **A** | **R** |
>
> **Legend:**
> - **R** = Responsible (does the work)
> - **A** = Accountable (makes the decision)
> - **C** = Consulted (provides input)
> - **I** = Informed (kept updated)
>
> **"You build it, you break it"** = Developer is R for unit tests, not just Tester.
>
> #### 2.3 How Google Addresses the 11 Decisions
>
> | Decision | Google's Answer  |
> |----------|-------------------------------------------|
> | **What activities?** | Test pyramid: 70% unit, 20% integration, 10% E2E |
> | **What coverage?** | 80% target, tracked per project |
> | **What tools?** | Tricorder (static analysis), TAP (150M tests/day) |
> | **When to test?** | Pre-submit gates (before merge) |
> | **What gates?** | Pre-submit → Post-submit → Release |
> | **Who tests?** | "You build it, you break it" (developers) |
> | **What roles?** | SWE + SET + TE structure |
> | **How to test?** | Test Certified requirements per level |
> | **What standards?** | Readability certification, style guides |
>
> **Your Turn:** Map YOUR project's answers to these 11 decisions.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

### Card 368 — Question 11: IEEE 829 and the "Addressed" Principle

> [!question] Question
> **Question 11: IEEE 829 and the "Addressed" Principle**
>
> IEEE 829 states that every topic must be formally addressed: include, record in tool, or exclude with rationale.
>
> Why is it important to never leave topics blank? Give an example of a section you might "exclude with rationale" for a small project.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The "Addressed" Principle
>
> > All topics must be formally decided: include, record in tool, or exclude with rationale.
>
> For each required topic, you must:
>
> | Option | Meaning |
> |--------|---------|
> | **Include** | Document the information in the plan |
> | **Record in Tool** | Reference where information is stored (e.g., in test management tool) |
> | **Exclude with Rationale** | Explicitly state why not applicable |
>
> **Never leave topics unaddressed.**
>
> #### 6.2 The "Addressed" Principle
>
> > All topics must be formally decided: include, record in tool, or exclude with rationale.
>
> | Option | Meaning |
> |--------|---------|
> | **Include** | Document the information in the plan |
> | **Record in Tool** | Reference where information is stored (e.g., in JIRA) |
> | **Exclude with Rationale** | Explicitly state why not applicable |
>
> **Never leave topics unaddressed.**

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

### Card 369 — Question 12: Test Effort Estimation

> [!question] Question
> **Question 12: Test Effort Estimation**
>
> Tester-to-developer ratios vary from 1:5 to 5:1 across industries. Microsoft uses 1:1.
>
> What factors explain these differences? If testing is typically 30% of total development effort, how would you sanity-check your test estimate for a 100 function-point project?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Test Effort Estimation
>
> Estimating test effort is challenging due to the many factors affecting testing. This page covers estimation methods, tester-to-developer ratios, and practical calculation approaches.
>
> #### [Test Effort Estimation](04-test-effort-estimation.md)
>
> Methods for estimating testing effort: TPA, UCP, historical data, and ML-based approaches.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

### Card 370 — Question 13: The Agile Trust Problem

> [!question] Question
> **Question 13: The Agile Trust Problem**
>
> Koopman (2010) argues that Agile's "trust picture" creates quality risks.
>
> What are Koopman's three evaluative questions for Agile teams? Why does he argue that even Agile teams need independent quality verification?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Three Evaluative Questions for Agile Teams
>
> 1. "Show me the written process you are following" (format can be flexible)
> 2. "Explain to me how an external person can tell whether you are actually following that process"
> 3. "Explain to me how an external person can tell that the process is producing the quality of software you want"
>
> **Quality Plan implication:** Even Agile teams need defined processes combined with independent quality verification.
>
> #### The Trust Problem
>
> Koopman argues that Agile relies on a "trust picture" where developers are expected to do the right thing—often at the expense of external audits and objective verification:
>
> | Risk | Description |
> |------|-------------|
> | **Lack of External Oversight** | No independent verification mechanisms |
> | **Subjectivity of Success** | Difficult to determine if team is actually writing quality code |
> | **Sustainability Risks** | Quality depends on individual "hero" leaders—high risk if they leave |
> | **Auditing Gaps** | Audits are not part of typical Agile trust model |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

### Card 371 — Question 14: Lightweight Test Plan

> [!question] Question
> **Question 14: Lightweight Test Plan**
>
> A one-page test plan can address all 11 decisions with just 6 sections: Scope, Approach, Gates, Roles, Schedule, Risks.
>
> Create a lightweight test plan outline for your SQR project. Include at least one concrete example for each section.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 6.3 Lightweight Test Plan Template
>
> A one-page test plan can address all 11 decisions:
>
> | Section | Content | Example |
> |---------|---------|---------|
> | **1. Scope** | What's tested, what's not | "API endpoints; NOT mobile app" |
> | **2. Approach** | Test pyramid, tools | "70/20/10, Jest, Postman" |
> | **3. Gates** | Entry/exit per milestone | "Sprint: 70% coverage, CI green" |
> | **4. Roles** | Who does what | "Devs: unit tests; QA: E2E" |
> | **5. Schedule** | When activities happen | "Week 1-2: unit; Week 3: integration" |
> | **6. Risks** | What could go wrong | "Flaky tests, environment issues" |
>
> **This template addresses all 11 decisions in 1 page.** Perfect for SQR/IPP projects.
>
> #### 6.1 Master Test Plan Structure
>
> IEEE 829-2008 provides the standard structure for software test documentation :
>
> **Part 1: Introduction**
> - Identifier — Unique document identifier
> - Scope — What is and isn't covered
> - References — Related documents
> - System Overview — High-level description
> - Test Overview — Schedule, resources, responsibilities
>
> **Part 2: Details**
> - Test Processes — How testing will be conducted
> - Test Levels — Component, integration, system, acceptance
> - Documentation Requirements — What documents will be produced
>
> **Part 3: General**
> - Glossary — Definitions of terms
> - Change Procedures — How plan changes are handled
> - Version History — Document revision history

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

### Card 372 — Question 15: CI Dashboard Metrics

> [!question] Question
> **Question 15: CI Dashboard Metrics**
>
> A study identified 39 information needs in CI/CD, with "test suite ownership" as the most important.
>
> Why is knowing who owns each test suite critical? What happens when ownership is unclear and tests start failing?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 8.4 Information Needs in CI/CD
>
> A study identified 39 distinct information needs across CI/CD pipelines :
>
> | Category | Key Needs |
> |----------|-----------|
> | **Test Suite** | Test suite ownership (most important), flaky tests, failure causes |
> | **Code/Commit** | Functional behavior, non-functional impact |
> | **CI Jobs** | Longest-running jobs, recently failed jobs |
> | **Infrastructure** | Hardware/simulator availability |
> | **Trends** | Frequent defects, delivery flow trends |
>
> **Most Important Need:** Test suite ownership — who is responsible for maintaining and fixing each test suite.
>
> #### Information Needs in CI/CD
>
> A study identified 39 distinct information needs across CI/CD pipelines :
>
> | Category | Key Needs |
> |----------|-----------|
> | **Test Suite** | Test suite ownership (most important), flaky tests, failure causes |
> | **Code/Commit** | Functional behavior, non-functional impact, architecture changes |
> | **CI Jobs** | Longest-running jobs, recently failed jobs |
> | **Infrastructure** | Hardware/simulator availability |
> | **Trends** | Frequent defects, delivery flow trends |
> | **Release** | Release dates, contents, resource issues |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

### Card 373 — Question 16: Defect Triage and Bug Bar

> [!question] Question
> **Question 16: Defect Triage and Bug Bar**
>
> During a sprint, your team discovers 5 bugs: 1 causes data loss, 2 have workarounds, and 2 are cosmetic issues.
>
> Classify each bug as P1/P2/P3-P4. If your bug bar is "0 P1s, ≤3 P2s allowed for release," which bugs must be fixed before release? Who should make the triage decision?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.5 Defect Triage: Fix Now or Later?
>
> Defects discovered during testing/development need immediate triage. The Quality Plan must define how bugs are prioritized and when they get fixed.
>
> **Defect Triage Flow:**
>
> ```mermaid
> flowchart TB
>     BF[🐛 Bug Found] --> T{Triage}
>     T -->|P1 Critical| FN[🔥 Fix NOW<br>hotfix branch]
>     T -->|P2 High| FS[⚡ Fix Sprint<br>if capacity]
>     T -->|P3-P4| BL[📋 Backlog<br>next sprint]
> ```
>
> **Triage Decision Table:**
>
> | Priority | Definition | Sprint Rule | Release Gate |
> |----------|------------|-------------|--------------|
> | **P1 (Critical)** | Data loss, security breach, blocks feature | Fix NOW—hotfix branch | **Blocks release** |
> | **P2 (High)** | Major bug, workaround exists | Fix this sprint if capacity | ≤3 open allowed |
> | **P3 (Medium)** | Minor bug, cosmetic issues | Add to backlog | Tracked, not blocking |
> | **P4 (Low)** | Enhancement, nice-to-have | Backlog for future sprint | Not tracked for release |
>
> **Quality Plan Must Define:**
>
> | Decision | Example Rule |
> |----------|--------------|
> | **Who triages?** | Dev + PO at daily standup |
> | **What's P1 vs P2?** | P1 = blocks feature, data loss, security. P2 = workaround exists |
> | **Does P1 block "Done"?** | Yes—feature not Done until P1s fixed |
> | **P2 at sprint end?** | Must document, can release if ≤3 open |
> | **Who can interrupt sprint?** | Only PO for P1 bugs |
>
> **Release Gate Example:**
> - ✅ 0 open P1s
> - ✅ ≤3 open P2s (documented with workarounds)
> - ⚠️ P3-P4 tracked but don't block
>
> **Cross-reference:** See A03 for Microsoft's bug bar and severity definitions.
>
> #### 5.4 RACI: Who Does What?
>
> | Activity | Dev | Tester | PM | QA |
> |----------|:---:|:------:|:--:|:--:|
> | Write unit tests | **R** | C | I | I |
> | Write integration tests | C | **R** | I | I |
> | Code review | **R** | C | I | I |
> | Run CI | A | **R** | I | I |
> | Triage bugs | C | **R** | **A** | C |
> | Release decision | C | C | **A** | **R** |
>
> **Legend:**
> - **R** = Responsible (does the work)
> - **A** = Accountable (makes the decision)
> - **C** = Consulted (provides input)
> - **I** = Informed (kept updated)
>
> **"You build it, you break it"** = Developer is R for unit tests, not just Tester.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

### Card 374 — Question 17: Defense in Depth

> [!question] Question
> **Question 17: Defense in Depth**
>
> The V&V technique selection matrix shows that different techniques suit different quality characteristics (Functionality, Reliability, Usability, Maintainability, Security).
>
> Which technique is strongest for Maintainability? Which for Usability? Explain why no single technique catches all defects and why combining methods is necessary.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.4 Choosing Activities: Defense in Depth
>
> Different V&V techniques are suited for different quality characteristics (see SQR L03: Verification Methods):
>
> | Quality Characteristic | Inspection | Analysis | Testing | Demo |
> |----------------------|:----------:|:--------:|:-------:|:----:|
> | **Functionality** | ○ | ○ | ● | ● |
> | **Reliability** | ○ | ● | ● | ○ |
> | **Usability** | ○ | ○ | ○ | ● |
> | **Efficiency** | ○ | ○ | ● | ● |
> | **Maintainability** | ● | ● | ○ | ○ |
> | **Security** | ○ | ● | ● | ○ |
>
> **Legend:** ● = Strong fit | ○ = Partial fit
>
> **Key Insights:**
> - **Maintainability** is best verified through **Inspection** (code review) and **Analysis** (static analysis tools)
> - **Usability** can only be truly verified through **Demonstration** (user testing)
> - **Security** requires both **Analysis** (SAST tools like `bandit`) and **Testing** (penetration testing)
> - No single technique finds all defects — combine them!
>
> #### Early V&V Techniques
>
> | Technique | Description | Adoption |
> |-----------|-------------|----------|
> | **Model transformations** | Automated conversion between languages | 63% |
> | **Simulation** | Execute models to verify behavior | Common |
> | **Model checking** | Formal verification of properties | Growing |
> | **Reviews** | Engineering review of model artifacts | Standard |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/02-plan/RQ-A4-QualityPlan.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/02-plan/RQ-A4-QualityPlan.md)

## Process Improvement (37)

### Card 375 — Question 1

> [!question] Question
> *A software team consistently delivers projects late. Management responds by requiring overtime. Three months later, two key developers quit and projects are even later. Using the concepts from this lecture, explain what went wrong and what should have been done instead.*

> [!answer]- Reveal answer / cues — model answer
> - Management chose "Working Harder" instead of "Working Smarter"
> - This created a capability trap: overtime led to burnout, turnover, and capability erosion
> - Double-loop learning was needed: analyze WHY projects are late (estimation? scope creep? testing bottleneck?)
> - Should have tolerated the "worse-before-better" dip to invest in process improvement
> - Reference: Repenning & Sterman (2001) capability dynamics

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 376 — Question 2

> [!question] Question
> *Explain why only 12.5% of organizations successfully implement process improvement, using Pfeffer's One-Eighth Rule.*

> [!answer]- Reveal answer / cues — model answer
> Three filters reduce success rate:
> 1. **Belief filter (50%):** Only half believe the evidence connecting practices to results
> 2. **Systemic filter (50%):** Only half try comprehensive change vs. isolated fixes
> 3. **Persistence filter (50%):** Only half persist through the "worse-before-better" phase
>
> Result: 50% × 50% × 50% = 12.5% succeed

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 377 — Question 3

> [!question] Question
> *A code review queue has become a bottleneck. Apply the Theory of Constraints Five Focusing Steps to solve this problem.*

> [!answer]- Reveal answer / cues — model answer
> 1. **Identify:** Code review is the constraint (PRs waiting 3+ days)
> 2. **Exploit:** Prioritize critical path reviews, batch small changes
> 3. **Subordinate:** Developers submit smaller PRs, limit WIP
> 4. **Elevate:** Train more reviewers, add automated linting
> 5. **Repeat:** If testing becomes the new bottleneck, start over

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 378 — Question 4

> [!question] Question
> *What is the difference between Level 1 and Level 2 in CMMI?*

> [!answer]- Reveal answer / cues — model answer
> - **Level 1 (Initial):** Processes are ad hoc; success depends on individual heroics; processes abandoned under stress; cannot repeat successes
> - **Level 2 (Managed):** Project-level process control; practices are planned, performed, and measured; **key difference: practices are retained during stress**; work is visible at milestones

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 379 — Question 5

> [!question] Question
> *Why is management commitment ranked as the #1 critical success factor for SPI?*

> [!answer]- Reveal answer / cues — model answer
> - Resources allocation depends on management support
> - Without champions, improvement time is lost to "firefighting"
> - Managers must model desired behaviors
> - Cultural change requires visible leadership commitment
> - Research consistently shows this as #1 factor across ITIL, Six Sigma, and Lean studies

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 380 — Question 6

> [!question] Question
> *List all Level 2 CMMI Process Areas and explain why "practices retained under stress" is the key differentiator from Level 1.*

> [!answer]- Reveal answer / cues — model answer
> Level 2 Process Areas (7 total):
> 1. **REQM** - Requirements Management
> 2. **PP** - Project Planning
> 3. **PMC** - Project Monitoring and Control
> 4. **SAM** - Supplier Agreement Management
> 5. **MA** - Measurement and Analysis
> 6. **PPQA** - Process and Product Quality Assurance
> 7. **CM** - Configuration Management
>
> "Practices retained under stress" is the key differentiator because:
> - Level 1 organizations abandon processes when facing pressure (deadlines, budget constraints)
> - Level 2 organizations maintain discipline even during crises
> - This means Level 2 can reproduce past successes while Level 1 cannot
> - The difference is not in having processes, but in **following them consistently**

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 381 — Question 7

> [!question] Question
> *An organization wants to move from CMMI Level 3 to Level 4. What is the key transition and which Process Areas must be implemented?*

> [!answer]- Reveal answer / cues — model answer
> **Key Transition:** From qualitative to quantitative management
> - Level 3 uses defined processes with qualitative assessment
> - Level 4 requires statistical process control and fact-based decision making
>
> **New Process Areas at Level 4:**
> 1. **OPP** (Organizational Process Performance) - Establish and maintain organizational process performance baselines
> 2. **QPM** (Quantitative Project Management) - Quantitatively manage the project to achieve quality and process performance objectives
>
> **What Changes:**
> - Decisions must be based on statistical data, not just expert judgment
> - Process performance baselines established and maintained
> - Special causes of variation identified and addressed
> - Quality measures incorporated into decision-making repository
>
> *For detailed explanations, see [Study Notes: Process Improvement](SN-A2-Proc.md)*

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 382 — Q1

> [!question] Question
> What is the "credibility gap" in software organizations according to Humphrey?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.2 The Credibility Gap
>
> Watts Humphrey  challenged executives with a fundamental question: **Why don't organizations practice what they believe?**
>
> | Management Theory Says | Actual Practice |
> |------------------------|-----------------|
> | Measure what matters | Rely on intuition |
> | Invest in learning | Cut training first |
> | Use data for decisions | Ignore metrics |
> | Continually improve | Fight fires |
>
> **The Reality of Most Organizations:**
> - Success depends on "heroics" rather than processes
> - Tendency to over-commit to deadlines
> - Budget overruns are common
> - Cannot repeat past successes reliably
>
> > **Key Insight:** Professional management should not rely on heroics. The gap between theory and practice is where SPI lives.
>
> #### The Credibility Gap
>
> Humphrey posed rhetorical questions to leadership:
> - If you truly believe management adds value, why don't you measure it?
> - If organizational learning is effective, why don't you invest in it?
> - If data-driven decisions are superior to intuition, why rely on heroics?

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 383 — Q2

> [!question] Question
> Explain the One-Eighth Rule and its three filters.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.5 The One-Eighth Rule
>
> Jeff Pfeffer  explains why only **12.5%** of organizations see full benefits from improvement initiatives:
>
> | Stage | Filter | Organizations Remaining |
> |-------|--------|-------------------------|
> | Start | All organizations | 100% |
> | **Belief** | Only half believe the evidence | 50% |
> | **Systemic approach** | Only half try comprehensive change | 25% |
> | **Persistence** | Only half persist long enough | **12.5%** |
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "title": "The One-Eighth Rule: SPI Success Funnel",
>   "width": 300,
>   "height": 200,
>   "data": {
>     "values": [
>       {"stage": "1. Start", "percentage": 100, "order": 1},
>       {"stage": "2. Believe", "percentage": 50, "order": 2},
>       {"stage": "3. Systemic", "percentage": 25, "order": 3},
>       {"stage": "4. Persist", "percentage": 12.5, "order": 4}
>     ]
>   },
>   "mark": {"type": "bar", "cornerRadiusEnd": 4},
>   "encoding": {
>     "y": {"field": "stage", "type": "nominal", "sort": {"field": "order"}, "title": null},
>     "x": {"field": "percentage", "type": "quantitative", "title": "Organizations (%)"},
>     "color": {
>       "field": "percentage",
>       "type": "quantitative",
>       "scale": {"scheme": "reds", "reverse": true},
>       "legend": null
>     }
>   }
> }
> ```
>
> **Why Organizations Fail at Each Stage:**
>
> 1. **Belief Filter (50% → 50%):**
>    - "Our situation is different"
>    - "That won't work here"
>    - Resistance to change based on past failures
>
> 2. **Systemic Filter (50% → 25%):**
>    - Isolated "checkbox" changes instead of comprehensive reform
>    - Implementing tools without changing processes
>    - Training without cultural shift
>
> …
>
> #### The One-Eighth Rule
>
> Proposed by Jeff Pfeffer , this rule explains the high failure rate of management practices despite clear evidence of their benefits.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 384 — Q3

> [!question] Question
> How did organizational culture contribute to the Columbia disaster?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.4 Case Study: Columbia Disaster
>
> The 2003 Space Shuttle Columbia tragedy demonstrates how **organizational failure precedes physical failure** .
>
> **What Happened:**
> - Shuttle disintegrated on reentry, killing all seven crew members
> - Physical cause: foam debris struck wing during launch
> - **Root cause: Organizational systems failure**
>
> **Organizational Failures:**
>
> | Issue | Impact |
> |-------|--------|
> | **Silencing dissent** | Engineers stopped raising technical concerns |
> | **Success-oriented culture** | Bad news was filtered out before reaching decision-makers |
> | **Hierarchical communication** | Information didn't reach those who needed it |
> | **Normalization of deviance** | Anomalies treated as "maintenance events" rather than dangers |
>
> > "If dissent and questioning are not welcomed, you stop doing it." — Sheila Widnall, CAIB Member
>
> **The Culture Definition:**
> Culture is the "set of rules you have to follow to have a fast-track career." At NASA, questioning schedule decisions was not a path to career success, so engineers stopped questioning.
>
> #### Case Study: Space Shuttle Columbia Disaster
>
> The 2003 Columbia tragedy serves as a primary example of how **organizational failure precedes physical failure** .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 385 — Q4

> [!question] Question
> Why do quick fixes fail to solve recurring quality problems?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.2 Why Improvements Fail
>
> Returning to Pfeffer's One-Eighth Rule  in detail:
>
> **Filter 1: Belief (100% → 50%)**
> - Only half believe the connection between management practices and business results
> - Common excuses: "Our situation is different," "That won't work here"
> - **Result:** 50% don't even start seriously
>
> **Filter 2: Systemic Approach (50% → 25%)**
> - Only half of believers try comprehensive systemic change
> - Common mistake: Isolated "checkbox" changes
> - Example: Implementing a tool without changing processes or training
>
> **Filter 3: Persistence (25% → 12.5%)**
> - Only half persist long enough for results to manifest
> - Killed by: Budget cuts, leadership changes, "worse-before-better" phase
> - Timeline: Real improvements often take 18-24 months
>
> **Implications:**
> 1. Evidence alone is insufficient
> 2. Must believe AND act systematically AND persist
> 3. Most fail not because SPI doesn't work, but because they don't follow through
>
> #### 4.4 Five Maturity Levels - Quick Reference
>
> | Level | Name | Process Scope | Approach | Key Phrase |
> |:-----:|------|---------------|----------|------------|
> | **1** | Initial | Ad-hoc | Reactive | "Heroics and chaos" |
> | **2** | Managed | Project-level | Disciplined | "Retained under stress" |
> | **3** | Defined | Organization-level | Proactive | "Standards and consistency" |
> | **4** | Quant. Managed | Statistical | Measured | "Fact-based decisions" |
> | **5** | Optimizing | Continuous | Improving | "Incremental & innovative" |
>
> ```mermaid
> flowchart TB
>     subgraph CMMI["CMMI Maturity Levels"]
>         direction TB
>         L5["Level 5: Optimizing<br>🚀 Continuous Improvement"]
>         L4["Level 4: Quantitatively Managed<br>📊 Statistical Control"]
>         L3["Level 3: Defined<br>📋 Organization-wide Standards"]
>         L2["Level 2: Managed<br>📁 Project-level Control"]
>         L1["Level 1: Initial<br>🔥 Ad hoc, Chaotic"]
>     end
>
>     L1 --> L2 --> L3 --> L4 --> L5
>
>     style L1 fill:#FFCDD2
>     style L2 fill:#FFE0B2
>     style L3 fill:#FFF9C4
>     style L4 fill:#C8E6C9
>     style L5 fill:#B3E5FC
> ```

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 386 — Q5

> [!question] Question
> What percentage of organizations successfully implement SPI? Why is this number so low?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The SPI Research Landscape
>
> A systematic mapping study of 769 SPI publications  found:
>
> | Finding | Percentage |
> |---------|------------|
> | Solution proposals | 38.2% |
> | Philosophical papers | 34.3% |
> | Evaluation research | Only 15% |
> | Success factors papers | 16.4% |
>
> #### 1.3 Business Scenarios Driving SPI
>
> Three common scenarios explain why organizations pursue process improvement:
>
> | Scenario | Problem | Quick Fix vs. Real Fix |
> |----------|---------|------------------------|
> | **Internet Company** | Bugs in client-facing products affecting profits | Fix the bug → OR → Fix why bugs keep appearing |
> | **Small Engineering Firm** | Great products but consistently beaten to market | Work harder → OR → Fix the delivery process |
> | **Consulting Firm** | Late on milestones, client threatening to leave | Overtime → OR → Improve estimation and planning |
>
> **Example - The Bug Fix Dilemma:**
> ```
> Scenario: E-commerce site has recurring payment failures
>
> Quick fix approach:
>   - Developer patches the specific bug
>   - Manager declares victory
>   - Next week: similar bug appears
>
> Process improvement approach:
>   - Root cause analysis: Why do payment bugs keep appearing?
>   - Finding: No integration tests for payment flow
>   - Fix: Add mandatory payment test coverage
>   - Result: Payment bugs reduced by 60%
> ```
>
> > **Exam Tip:** When asked about SPI motivations, remember: quick fixes address symptoms, process improvement addresses root causes.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 387 — Q1

> [!question] Question
> Explain the difference between single-loop and double-loop learning with an example.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.2 Single-Loop vs Double-Loop Learning
>
> Argyris and Schon  introduced these concepts to explain different levels of organizational learning:
>
> | Type | Definition | Focus | Characteristic Response |
> |------|------------|-------|------------------------|
> | **Single-Loop** | Recognize error, correct it, continue same strategy | "Fixing the problem" | *"Someone is screwing up"* |
> | **Double-Loop** | Recognize error, question assumptions, modify strategy | "Fixing the system" | *"The system is failing"* |
>
> **Diagram: The Learning Loops**
>
> ```mermaid
> flowchart LR
>     subgraph Single-Loop["Single-Loop Learning"]
>         direction LR
>         E1[Error] --> C1[Correct Error]
>         C1 --> S1[Same Strategy]
>         S1 -.-> E1
>     end
>
>     subgraph Double-Loop["Double-Loop Learning"]
>         direction LR
>         E2[Error] --> Q2[Question Assumptions]
>         Q2 --> M2[Modify Strategy]
>         M2 --> N2[New Approach]
>         N2 -.-> E2
>     end
> ```
>
> **Software Engineering Examples:**
>
> | Scenario | Single-Loop Response | Double-Loop Response |
> |----------|---------------------|---------------------|
> | Server crashes | Restart the server | Add monitoring policy; implement auto-restart |
> | Test failures | Fix the failing tests | Analyze why tests weren't written earlier; improve TDD practices |
> | Late delivery | Work overtime to catch up | Examine estimation process; improve planning methodology |
> | Bug in production | Patch and deploy hotfix | Root cause analysis; add regression tests and code review |
>
> **Example - The Recurring Bug:**
> ```
> Scenario: Login failures spike every Monday morning
>
> Single-loop thinking:
>   Week 1: Fix the bug, deploy hotfix
>   Week 2: Same type of bug, fix again
>   Week 3: "Why does this keep happening?"
>
> …
>
> #### Single-Loop vs Double-Loop Learning
>
> Chris Argyris and Donald Schon introduced these concepts to explain different levels of organizational learning .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 388 — Q2

> [!question] Question
> Apply the PDCA cycle to a scenario of reducing bug escape rate.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.3 PDCA Cycle (Deming Cycle)
>
> The Plan-Do-Check-Act cycle is the foundation of continuous improvement:
>
> | Stage | Activity | Key Questions |
> |-------|----------|---------------|
> | **Plan** | Establish objectives and processes | What do we want to achieve? How will we measure success? |
> | **Do** | Implement the plan/process | Execute changes on a small scale first |
> | **Check** | Measure results against goals | Did we achieve what we planned? What did we learn? |
> | **Act** | Adjust based on learning | Standardize if successful; revise if not |
>
> ```mermaid
> flowchart LR
>     P[Plan] --> D[Do]
>     D --> C[Check]
>     C --> A[Act]
>     A --> P
>
>     style P fill:#4CAF50,color:#fff
>     style D fill:#2196F3,color:#fff
>     style C fill:#FF9800,color:#fff
>     style A fill:#9C27B0,color:#fff
> ```
>
> **PDCA in Software Frameworks:**
>
> | Framework | Plan | Do | Check | Act |
> |-----------|------|-----|-------|-----|
> | **Scrum** | Sprint planning | Sprint work | Sprint demo | Retrospective |
> | **CMMI** | Assessment | Implement | Measure | Adjust |
> | **DevOps** | Deploy strategy | Deploy | Monitor | Improve pipeline |
>
> **Example - PDCA for Reducing Build Time:**
> ```
> PLAN: "We will reduce build time from 45 min to 15 min by adding caching"
>   - Objective: 15-minute builds
>   - Measure: CI pipeline duration
>
> DO: Implement build caching for dependencies
>   - Add cache layer for npm packages
>   - Cache compiled intermediate files
>
> CHECK: Measure results after 2 weeks
>   - Average build time: 22 minutes (not 15)
>   - Finding: Test execution is now the bottleneck
>
> ACT: Adjust strategy
>   - Caching helped (45→22 min)
>   - Next cycle: parallelize tests to reach 15 min target
> ```
>
> #### PDCA/PDSA Cycle (Deming)
>
> The Plan-Do-Check-Act (PDCA) cycle, also known as the Deming Cycle, is a four-stage iterative method for continuous improvement.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 389 — Q3

> [!question] Question
> What are the four principles of Kaizen?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.4 Kaizen: Continuous Small Improvements
>
> Kaizen is a Japanese philosophy meaning "continuous improvement" — involving everyone from CEO to front-line workers.
>
> **Core Principles:**
>
> | Principle | Description | Example |
> |-----------|-------------|---------|
> | **Incremental** | Small, frequent changes (not "Big Bang") | Daily code reviews vs. quarterly audits |
> | **Everyone participates** | From CEO to developers | Retrospectives include whole team |
> | **Bottom-up** | Developer-driven, not mandated | Engineers propose automation ideas |
> | **Continuous** | Part of daily work, never stops | CI/CD, not manual releases |
>
> **Software Kaizen Manifestations:**
>
> | Traditional Approach | Kaizen Approach |
> |---------------------|-----------------|
> | Quarterly releases with extensive change logs | Dozens of deployments per day |
> | Annual performance reviews | Continuous feedback and retrospectives |
> | One-time training events | Daily learning and pair programming |
> | Large refactoring projects | Incremental "boy scout rule" improvements |
>
> > **Key Insight:** Kaizen + DevOps = Continuous deployment with real-time feedback loops.
>
> #### Kaizen Philosophy
>
> Kaizen is a Japanese philosophy meaning "continuous improvement" — involving every employee from the CEO to the front-line worker.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 390 — Q4

> [!question] Question
> Describe the "worse-before-better" dynamic. Why do organizations fall into the capability trap?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.6 The Capability Trap
>
> When managers cannot tolerate the short-term dip, they revert to "Working Harder":
>
> **Two Responses to Performance Gap:**
>
> | Option | Short-term Effect | Long-term Effect |
> |--------|------------------|------------------|
> | **Work Harder** | Immediate recovery (overtime, shortcuts) | Capability erosion, burnout |
> | **Work Smarter** | Performance dip | Sustainable high performance |
>
> **The Trap Mechanism:**
> 1. Team invests in improvement → performance dips
> 2. Manager panics → "Stop improving, just deliver!"
> 3. Team reverts to Working Harder → immediate recovery
> 4. Working Harder becomes the norm → less time for improvement
> 5. Capability erodes → more pressure → vicious cycle
> 6. Eventually: burnout, technical debt, quality collapse
>
> ```mermaid
> flowchart TD
>     subgraph Trap["❌ The Capability Trap (Vicious Cycle)"]
>         direction TB
>         P1["Performance Gap"] --> M1["Manager: Work Harder!"]
>         M1 --> O1["Overtime & Shortcuts"]
>         O1 --> R1["Short-term Recovery"]
>         R1 --> N1["No Time for Improvement"]
>         N1 --> E1["Capability Erodes"]
>         E1 --> P1
>     end
>
>     subgraph Escape["✅ Escape: Work Smarter"]
>         direction TB
>         P2["Performance Gap"] --> M2["Manager: Invest in Improvement"]
>         M2 --> D2["Temporary Dip"]
>         D2 --> C2["Capability Building"]
>         C2 --> S2["Sustained High Performance"]
>     end
>
>     style P1 fill:#FFCDD2
>     style E1 fill:#FFCDD2
>     style S2 fill:#C8E6C9
>     style C2 fill:#C8E6C9
> ```
>
> **Example - The Automation Trap:**
> ```
> Quarter 1: Team proposes automation to reduce manual testing (2 weeks investment)
>   Manager: "We don't have time, just do manual testing"
>
> …
>
> #### 2.5 The "Worse-Before-Better" Dynamic
>
> Repenning & Sterman  explain why "Working Smarter" causes a temporary performance dip:
>
> **The Dynamic:**
>
> | Phase | What Happens | Example |
> |-------|--------------|---------|
> | **Investment** | Time diverted from production to improvement | Team spends 2 days learning new testing framework |
> | **Initial dip** | Short-term metrics decline | Velocity drops 20% during learning curve |
> | **Capability building** | Skills and processes improve | Team becomes proficient with new tools |
> | **Payoff** | Performance exceeds baseline | Velocity increases 30% above original |
>
> **Diagram: Worse-Before-Better**
>
> ```mermaid
> %%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#019546'}}}%%
> flowchart LR
>     subgraph Timeline["Performance Over Time"]
>         direction LR
>         A["📊 Baseline"] --> B["📉 Investment Dip"]
>         B --> C["📈 Capability Building"]
>         C --> D["🚀 Sustained Gains"]
>     end
>
>     style A fill:#90CAF9
>     style B fill:#FFCDD2
>     style C fill:#FFF9C4
>     style D fill:#A5D6A7
> ```
>
> **Visual Representation:**
> - **Baseline** → Starting performance level
> - **Investment Dip** → Short-term decline during learning
> - **Capability Building** → Skills improve, performance recovers
> - **Sustained Gains** → Long-term performance exceeds original baseline

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 391 — Q5

> [!question] Question
> How does DevOps embody Kaizen principles?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.4 Kaizen: Continuous Small Improvements
>
> Kaizen is a Japanese philosophy meaning "continuous improvement" — involving everyone from CEO to front-line workers.
>
> **Core Principles:**
>
> | Principle | Description | Example |
> |-----------|-------------|---------|
> | **Incremental** | Small, frequent changes (not "Big Bang") | Daily code reviews vs. quarterly audits |
> | **Everyone participates** | From CEO to developers | Retrospectives include whole team |
> | **Bottom-up** | Developer-driven, not mandated | Engineers propose automation ideas |
> | **Continuous** | Part of daily work, never stops | CI/CD, not manual releases |
>
> **Software Kaizen Manifestations:**
>
> | Traditional Approach | Kaizen Approach |
> |---------------------|-----------------|
> | Quarterly releases with extensive change logs | Dozens of deployments per day |
> | Annual performance reviews | Continuous feedback and retrospectives |
> | One-time training events | Daily learning and pair programming |
> | Large refactoring projects | Incremental "boy scout rule" improvements |
>
> > **Key Insight:** Kaizen + DevOps = Continuous deployment with real-time feedback loops.
>
> #### Software Kaizen
>
> In software engineering, Kaizen manifests as:
>
> | Practice | Kaizen Element |
> |----------|----------------|
> | **Agile Retrospectives** | Regular reflection and adjustment by the team |
> | **CI/CD Pipelines** | Small, frequent deployments with real-time feedback |
> | **DevOps Culture** | Continuous improvement embedded in daily operations |
> | **Code Reviews** | Incremental quality improvement through peer feedback |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 392 — Q1

> [!question] Question
> What are the four components of IBM's Defect Prevention Process?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.3 IBM's Defect Prevention Process (DPP)
>
> DPP  represents a paradigm shift from defect **detection** to defect **prevention**.
>
> **The Four Key Components:**
>
> | Component | Description | Purpose |
> |-----------|-------------|---------|
> | **Causal Analysis Meetings** | Teams analyze defects using fishbone diagrams | Understand *why* defects occur |
> | **Action Team** | Cross-functional group with authority | Implement preventive actions |
> | **Stage Kickoff Meetings** | Review common errors at each stage | Increase awareness, prevent known issues |
> | **Data Collection & Tracking** | Systematic tracking of defects and causes | Enable feedback and continuous improvement |
>
> **Quantitative Results:**
>
> | Metric | Improvement |
> |--------|-------------|
> | Defect reduction (development) | **54%** |
> | Defect reduction (field/production) | **60%** |
> | Resource cost | Only **0.5%** of project budget |
> | ROI | Significant positive return |
>
> …
>
> #### IBM's Defect Prevention Process (DPP)
>
> DPP represents a paradigm shift from **defect detection** to **defect prevention** through systematic root cause analysis . Originated at IBM in 1983, it spread to over 25 development organizations by 1990.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 393 — Q2

> [!question] Question
> Apply the Five Focusing Steps to a scenario where testing is the bottleneck.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The Five Focusing Steps
>
> | Step | Name | Action |
> |------|------|--------|
> | 1 | **Identify** | Locate the physical (equipment) or managerial (policy) "weakest link" |
> | 2 | **Exploit** | Ensure the bottleneck is used as effectively as possible without expensive upgrades |
> | 3 | **Subordinate** | Align all non-constraints to support the bottleneck, even if it reduces their efficiency |
> | 4 | **Elevate** | Invest in rigorous improvement to increase the bottleneck's capacity |
> | 5 | **Repeat** | If constraint is broken, return to Step 1; do not let inertia become the new bottleneck |
>
> #### 3.4 Theory of Constraints (ToC)
>
> Goldratt  introduced TOC based on a fundamental principle:
>
> > "Every system has at least one constraint; otherwise unlimited results would be possible."
>
> **The Five Focusing Steps:**
>
> | Step | Name | Action | Software Example |
> |------|------|--------|------------------|
> | 1 | **Identify** | Find the weakest link | Code review queue is slow |
> | 2 | **Exploit** | Use bottleneck effectively | Prioritize critical reviews first |
> | 3 | **Subordinate** | Align others to support it | Slow down PR submissions to match review capacity |
> | 4 | **Elevate** | Invest to increase capacity | Add more reviewers, automate linting |
> | 5 | **Repeat** | Return to step 1 | Testing is now the new bottleneck |
>
> ```mermaid
> flowchart TD
>     I["1️⃣ IDENTIFY<br>Find the constraint"] --> E["2️⃣ EXPLOIT<br>Maximize constraint usage"]
>     E --> S["3️⃣ SUBORDINATE<br>Align everything else"]
>     S --> EL["4️⃣ ELEVATE<br>Increase capacity"]
>     EL --> R{"5️⃣ REPEAT<br>Constraint broken?"}
>     R -->|Yes| I
>     R -->|No| EL
>
>     style I fill:#E3F2FD
>     style E fill:#E8F5E9
>     style S fill:#FFF3E0
>     style EL fill:#FCE4EC
>     style R fill:#F3E5F5
> ```
>
> **The Hiking Group Analogy:**
> ```
> Scenario: Group hiking to summit. One person keeps falling behind.
>
> That person IS the constraint - group speed = slowest person's speed.
>
> Five Focusing Steps applied:
>   1. IDENTIFY: "Alex is the slowest"
>   2. EXPLOIT: Move heavy items from Alex's backpack to others
>   3. SUBORDINATE: Strongest hiker walks with Alex (not ahead)
>   4. ELEVATE: Give Alex hiking poles, lightest boots
>   5. REPEAT: Now someone else is slowest - repeat process
> ```
>
> **Advantages and Disadvantages:**
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 394 — Q3

> [!question] Question
> Explain the DMAIC cycle phases.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### The DMAIC Cycle
>
> | Phase | Activity | Key Questions |
> |-------|----------|---------------|
> | **Define** | Identify project goals and customer requirements (CTQ) | What is the problem? Who is the customer? |
> | **Measure** | Determine how to measure the process; establish baseline | How do we measure success? What's our current state? |
> | **Analyze** | Use statistical methods to find root causes | What causes the defects? |
> | **Improve** | Implement solutions to remove causes | How do we fix it? Does the solution work? |
> | **Control** | Put systems in place to maintain improvements | How do we prevent regression? |
>
> #### 3.5 Six Sigma (DMAIC)
>
> Six Sigma  is a data-driven methodology aiming for **3.4 defects per million opportunities**.
>
> **The DMAIC Cycle:**
>
> | Phase | Activity | Key Questions | Tools |
> |-------|----------|---------------|-------|
> | **Define** | Identify goals and customer requirements (CTQ) | What is the problem? Who is the customer? | Project charter, Voice of Customer |
> | **Measure** | Determine how to measure; establish baseline | How do we measure success? Current state? | Process mapping, data collection |
> | **Analyze** | Use statistical methods to find root causes | What causes the defects? | Statistical analysis, fishbone diagram |
> | **Improve** | Implement solutions to remove causes | Does the solution work? | Pilot testing, optimization |
> | **Control** | Maintain improvements | How do we prevent regression? | Control charts, documentation |
>
> ```mermaid
> flowchart LR
>     D["Define"] --> M["Measure"]
>     M --> A["Analyze"]
>     A --> I["Improve"]
>     I --> C["Control"]
>     C -.->|Continuous| D
>
>     style D fill:#1565C0,color:#fff
>     style M fill:#2E7D32,color:#fff
>     style A fill:#F57F17,color:#fff
>     style I fill:#6A1B9A,color:#fff
>     style C fill:#C62828,color:#fff
> ```
>
> **Six Sigma Infrastructure:**
>
> | Role | Responsibility |
> |------|----------------|
> | **Champion** | Executive sponsor, removes barriers |
> | **Black Belt** | Full-time improvement specialist |
> | **Green Belt** | Part-time improvement participant |
> | **Yellow Belt** | Awareness and participation |
>
> **12 Critical Success Factors** (ranked) :
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 395 — Q4

> [!question] Question
> What is the target defect rate for Six Sigma?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Six Sigma (DMAIC)
>
> Six Sigma is a data-driven methodology aimed at achieving stable and predictable process results by identifying and removing causes of variation .
>
> #### Lean Six Sigma
>
> Lean Six Sigma integrates:
> - **Lean:** Eliminate waste, improve flow
> - **Six Sigma:** Reduce variation, improve quality

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 396 — Q5

> [!question] Question
> Compare DPP and Agile retrospectives.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Retrospectives vs DPP
>
> | Aspect | DPP | Retrospectives |
> |--------|-----|----------------|
> | Trigger | Defects discovered | Sprint/iteration end |
> | Focus | Root cause of defects | Team effectiveness |
> | Participants | Action team | Whole team |
> | Frequency | After defect discovery | Regular cadence (2-4 weeks) |
> | Data source | Defect database | Team discussion + repository data |
>
> #### 3.6 Agile Retrospectives
>
> Retrospectives are a modern grassroots improvement mechanism embodying double-loop learning .
>
> **Core Questions:**
> 1. What went well?
> 2. What didn't go well?
> 3. What will we change?
>
> **Structured Activities:**
>
> | Activity | Purpose | How It Works |
> |----------|---------|--------------|
> | **Sailboat** | Identify threats and opportunities | Team draws anchors (blockers) and wind (helpers) |
> | **Five Whys** | Root cause analysis | Ask "why?" five times to find root cause |
> | **6 Thinking Hats** | Multiple perspectives | Team wears different "hats" (facts, emotions, risks...) |
> | **Timeline** | Map patterns over time | Create visual timeline of sprint events |
>
> **Retrospectives vs DPP:**
>
> | Aspect | DPP | Retrospectives |
> |--------|-----|----------------|
> | Trigger | Defects discovered | Sprint/iteration end |
> | Focus | Root cause of defects | Team effectiveness |
> | Frequency | After defect discovery | Regular cadence (2-4 weeks) |
> | Participants | Action team | Whole team |
> | Data source | Defect database | Team discussion + repository data |
>
> **Empirical Finding:** 75% of retrospective statements focus on controllable topics (sprint planning, implementation, testing) .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 397 — Q1

> [!question] Question
> What are the five maturity levels of CMMI? Describe each briefly.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.4 Five Maturity Levels - Quick Reference
>
> | Level | Name | Process Scope | Approach | Key Phrase |
> |:-----:|------|---------------|----------|------------|
> | **1** | Initial | Ad-hoc | Reactive | "Heroics and chaos" |
> | **2** | Managed | Project-level | Disciplined | "Retained under stress" |
> | **3** | Defined | Organization-level | Proactive | "Standards and consistency" |
> | **4** | Quant. Managed | Statistical | Measured | "Fact-based decisions" |
> | **5** | Optimizing | Continuous | Improving | "Incremental & innovative" |
>
> ```mermaid
> flowchart TB
>     subgraph CMMI["CMMI Maturity Levels"]
>         direction TB
>         L5["Level 5: Optimizing<br>🚀 Continuous Improvement"]
>         L4["Level 4: Quantitatively Managed<br>📊 Statistical Control"]
>         L3["Level 3: Defined<br>📋 Organization-wide Standards"]
>         L2["Level 2: Managed<br>📁 Project-level Control"]
>         L1["Level 1: Initial<br>🔥 Ad hoc, Chaotic"]
>     end
>
>     L1 --> L2 --> L3 --> L4 --> L5
>
>     style L1 fill:#FFCDD2
>     style L2 fill:#FFE0B2
>     style L3 fill:#FFF9C4
>     style L4 fill:#C8E6C9
>     style L5 fill:#B3E5FC
> ```
>
> #### 4.2 What is CMMI?
>
> CMMI (Capability Maturity Model Integration) is a **best practice framework** providing structured guidance for process improvement.
>
> **How Organizations Use Frameworks:**
> - Qualify/rank suppliers
> - Gap analysis ("Where are we vs. where should we be?")
> - Improvement roadmap
> - Shared vision across teams
>
> **Major Frameworks Comparison:**
>
> | Framework | Focus |
> |-----------|-------|
> | **ISO 9001** | Quality management systems |
> | **CMMI** | Process maturity (software development) |
> | **ITIL** | IT service management |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 398 — Q2

> [!question] Question
> What is the key difference between Level 1 and Level 2?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.5 Detailed Level Definitions
>
> #### Level 1: Initial
> **Summary:** Process ad-hoc and/or incomplete. Reactive.
>
> **Definition:** Processes are usually ad hoc and chaotic; the environment is not stable. Success depends on the competence and heroics of the people, not on the use of proven processes. These organizations often produce products and services that work; however, they frequently exceed time and monetary budgets.
>
> **Characteristics:**
> - Tendency to over-commit
> - Abandonment of processes in a time of crisis
> - Inability to repeat successes
>
> > **Exam Tip:** Level 1 organizations succeed through individual heroics, not repeatable processes.
>
> #### Level 2: Managed
> **Summary:** Process developed at the projects level, practices are retained during times of stress.
>
> **Definition:** Projects ensure that requirements are managed and that processes are planned, performed, measured, and controlled according to documented plans. Process discipline helps to ensure that existing practices are retained during times of stress.
>
> **Key Characteristics:**
> - Status of work products visible to management at defined points (milestones)
> - Commitments established among relevant stakeholders and revised as needed
> - Work products are appropriately controlled
> - Products and services satisfy specified process descriptions, standards, and procedures
>
> **Process Areas:** REQM, PP, PMC, SAM, MA, PPQA, CM (7 PAs)
>
> > **Key Distinction from Level 1:** Practices are **retained during stress** — this is the critical difference.
>
> #### Level 3: Defined
> **Summary:** Process developed at the organization level. Proactive.
>
> **Definition:** Processes are well characterized and understood, and are described in standards, procedures, tools, and methods.
>
> …
>
> #### 4.6 Key Transitions Between Levels
>
> | Transition | Key Change | What's New |
> |------------|------------|------------|
> | **1 → 2** | From chaos to project control | Basic planning, tracking, configuration management |
> | **2 → 3** | From project to organization | Standard processes, training, process definition |
> | **3 → 4** | From qualitative to quantitative | Statistical process control, performance baselines |
> | **4 → 5** | From managed to optimizing | Continuous improvement, innovation deployment |
>
> > **Exam Tip:** Remember the key phrase for each transition — this is a common exam question.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 399 — Q3

> [!question] Question
> List all Level 2 Process Areas with their abbreviations.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.7 CMMI Process Areas by Level
>
> | Level | Name | Focus | Process Areas |
> |:-----:|------|-------|---------------|
> | **5** | Optimizing | Continuous process improvement | OID, CAR |
> | **4** | Quantitatively Managed | Quantitative management | OPP, QPM |
> | **3** | Defined | Process standardization | RD, TS, PI, VER, VAL, OPF, OPD, OT, IPM, RSKM, DAR |
> | **2** | Managed | Basic project management | REQM, PP, PMC, SAM, MA, PPQA, CM |
> | **1** | Initial | Work harder | *(none defined - ad hoc)* |
>
> #### 4.9 Process Area Abbreviations Reference
>
> **Level 2 Process Areas (7 total):**
>
> | Abbrev | Full Name |
> |--------|-----------|
> | REQM | Requirements Management |
> | PP | Project Planning |
> | PMC | Project Monitoring and Control |
> | SAM | Supplier Agreement Management |
> | MA | Measurement and Analysis |
> | PPQA | Process and Product Quality Assurance |
> | CM | Configuration Management |
>
> **Level 3 Process Areas (11 total):**
>
> | Abbrev | Full Name |
> |--------|-----------|
> | RD | Requirements Development |
> | TS | Technical Solution |
> | PI | Product Integration |
> | VER | Verification |
> | VAL | Validation |
> | OPF | Organizational Process Focus |
> | OPD | Organizational Process Definition |
> | OT | Organizational Training |
> | IPM | Integrated Project Management |
> | RSKM | Risk Management |
> | DAR | Decision Analysis and Resolution |
>
> **Level 4 Process Areas (2 total):**
>
> | Abbrev | Full Name |
> |--------|-----------|
> | OPP | Organizational Process Performance |
> | QPM | Quantitative Project Management |
>
> **Level 5 Process Areas (2 total):**
>
> | Abbrev | Full Name |
> |--------|-----------|
> | OID | Organizational Innovation and Deployment |
> | CAR | Causal Analysis and Resolution |
>
> > **Exam Tip:** Know the abbreviations! Common exam questions ask you to identify which level a Process Area belongs to.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 400 — Q4

> [!question] Question
> What are the four Process Area categories in CMMI?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.9 Process Area Abbreviations Reference
>
> **Level 2 Process Areas (7 total):**
>
> | Abbrev | Full Name |
> |--------|-----------|
> | REQM | Requirements Management |
> | PP | Project Planning |
> | PMC | Project Monitoring and Control |
> | SAM | Supplier Agreement Management |
> | MA | Measurement and Analysis |
> | PPQA | Process and Product Quality Assurance |
> | CM | Configuration Management |
>
> **Level 3 Process Areas (11 total):**
>
> | Abbrev | Full Name |
> |--------|-----------|
> | RD | Requirements Development |
> | TS | Technical Solution |
> | PI | Product Integration |
> | VER | Verification |
> | VAL | Validation |
> | OPF | Organizational Process Focus |
> | OPD | Organizational Process Definition |
> | OT | Organizational Training |
> | IPM | Integrated Project Management |
> | RSKM | Risk Management |
> | DAR | Decision Analysis and Resolution |
>
> **Level 4 Process Areas (2 total):**
>
> | Abbrev | Full Name |
> |--------|-----------|
> | OPP | Organizational Process Performance |
> | QPM | Quantitative Project Management |
>
> **Level 5 Process Areas (2 total):**
>
> | Abbrev | Full Name |
> |--------|-----------|
> | OID | Organizational Innovation and Deployment |
> | CAR | Causal Analysis and Resolution |
>
> > **Exam Tip:** Know the abbreviations! Common exam questions ask you to identify which level a Process Area belongs to.
>
> #### 4.7 CMMI Process Areas by Level
>
> | Level | Name | Focus | Process Areas |
> |:-----:|------|-------|---------------|
> | **5** | Optimizing | Continuous process improvement | OID, CAR |
> | **4** | Quantitatively Managed | Quantitative management | OPP, QPM |
> | **3** | Defined | Process standardization | RD, TS, PI, VER, VAL, OPF, OPD, OT, IPM, RSKM, DAR |
> | **2** | Managed | Basic project management | REQM, PP, PMC, SAM, MA, PPQA, CM |
> | **1** | Initial | Work harder | *(none defined - ad hoc)* |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 401 — Q5

> [!question] Question
> How do Generic Goals ensure process sustainability?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Why Process Improvement?
>
> Software Process Improvement (SPI) is a systematic approach to enhancing organizational performance by modifying technical, organizational, and cultural structures to achieve better business outcomes .
>
> #### 4.3 CMMI Structure
>
> **Hierarchical Meta-Model:**
>
> | Component | Description | Example |
> |-----------|-------------|---------|
> | **Process Areas (PA)** | Groups of related practices | Project Planning (PP), Configuration Management (CM) |
> | **Specific Goals (SG)** | Unique objectives for one PA | "Establish and maintain project estimates" |
> | **Specific Practices (SP)** | Concrete activities to achieve goals | "Estimate effort and cost for work products" |
> | **Generic Goals (GG)** | Apply to every PA | "Institutionalize a managed process" |
>
> **Generic Goals Ensure Sustainability:**
>
> | Component | Purpose | Example |
> |-----------|---------|---------|
> | Commitment | Policies and sponsorship | "Management commits to process" |
> | Ability | Resources and training | "Team has required skills" |
> | Directing | Measurement and analysis | "Process performance is measured" |
> | Verification | Conformance audits | "Process is reviewed for compliance" |
>
> **Two Representations:**
> - **Staged:** Organization's overall maturity level (1-5)
> - **Continuous:** Individual process area capability levels

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 402 — Q6

> [!question] Question
> Explain the key transition from Level 3 to Level 4.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.6 Key Transitions Between Levels
>
> | Transition | Key Change | What's New |
> |------------|------------|------------|
> | **1 → 2** | From chaos to project control | Basic planning, tracking, configuration management |
> | **2 → 3** | From project to organization | Standard processes, training, process definition |
> | **3 → 4** | From qualitative to quantitative | Statistical process control, performance baselines |
> | **4 → 5** | From managed to optimizing | Continuous improvement, innovation deployment |
>
> > **Exam Tip:** Remember the key phrase for each transition — this is a common exam question.
>
> #### 4.5 Detailed Level Definitions
>
> #### Level 1: Initial
> **Summary:** Process ad-hoc and/or incomplete. Reactive.
>
> **Definition:** Processes are usually ad hoc and chaotic; the environment is not stable. Success depends on the competence and heroics of the people, not on the use of proven processes. These organizations often produce products and services that work; however, they frequently exceed time and monetary budgets.
>
> **Characteristics:**
> - Tendency to over-commit
> - Abandonment of processes in a time of crisis
> - Inability to repeat successes
>
> > **Exam Tip:** Level 1 organizations succeed through individual heroics, not repeatable processes.
>
> #### Level 2: Managed
> **Summary:** Process developed at the projects level, practices are retained during times of stress.
>
> **Definition:** Projects ensure that requirements are managed and that processes are planned, performed, measured, and controlled according to documented plans. Process discipline helps to ensure that existing practices are retained during times of stress.
>
> **Key Characteristics:**
> - Status of work products visible to management at defined points (milestones)
> - Commitments established among relevant stakeholders and revised as needed
> - Work products are appropriately controlled
> - Products and services satisfy specified process descriptions, standards, and procedures
>
> **Process Areas:** REQM, PP, PMC, SAM, MA, PPQA, CM (7 PAs)
>
> > **Key Distinction from Level 1:** Practices are **retained during stress** — this is the critical difference.
>
> #### Level 3: Defined
> **Summary:** Process developed at the organization level. Proactive.
>
> **Definition:** Processes are well characterized and understood, and are described in standards, procedures, tools, and methods.
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 403 — Q7

> [!question] Question
> Why can CMMI and Agile work together?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.11 CMMI + Agile Integration
>
> **Common Misconception:**
> - CMMI = heavy, bureaucratic
> - Agile = light, flexible
> - Therefore: incompatible?
>
> **Reality:** CMMI v2.0 was designed for Agile, SAFe, and DevSecOps integration .
>
> **Challenges of Integration:**
> - Agile lacks explicit org-level processes
> - Philosophy tension: control vs. minimal bureaucracy
> - Documentation requirements
>
> **The Hybrid Model:**
>
> | Aspect | CMMI Contribution | Agile Contribution |
> |--------|-------------------|-------------------|
> | Structure | Organization-wide consistency | Team flexibility |
> | Documentation | Required artifacts | Minimal viable docs |
> | Planning | Long-term roadmap | Iteration planning |
> | Improvement | Formal assessment | Retrospectives |
>
> #### 4.10 CMMI v1.3 vs v2.0 Changes
>
> | Aspect | CMMI v1.3 | CMMI v2.0 |
> |--------|-----------|-----------|
> | Structure | 3 constellations (DEV, SVC, ACQ) | Single unified model |
> | Process Areas | 22 Process Areas | 20 Practice Areas |
> | Levels | ML 1-5, CL 0-3 | ML 1-5, CL 1-5 |
> | Agile support | Challenging | Native integration |
> | Appraisal | SCAMPI A/B/C | Benchmark, Sustainment, Action |
>
> > **Key Insight:** CMMI v2.0 was redesigned with Agile, SAFe, and DevSecOps in mind.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 404 — Q8

> [!question] Question
> What quantitative results has CMMI adoption shown?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.12 CMMI Results
>
> **Quantitative Results from CMMI v2.0:**
>
> | Metric | Improvement |
> |--------|-------------|
> | Estimation accuracy | **+17%** |
> | Rework reduction | **70%** |
> | On-time delivery | **97%** |
>
> **Bangalore IT Study Results** :
>
> | Outcome | Respondents Reporting |
> |---------|----------------------|
> | Improved software quality | 37% |
> | Reduced defects | 35% |
> | Enhanced customer satisfaction | 32% |
> | Higher employee engagement | 29% |
>
> > **Key:** Success requires leadership commitment and cultural alignment, not just process documentation.
>
> #### Quantitative Results
>
> | Metric | Improvement |
> |--------|-------------|
> | Defect reduction (development) | 54% |
> | Defect reduction (field) | 60% |
> | Resource cost | Only 0.5% of project |
> | ROI | Significant positive return |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 405 — Q9

> [!question] Question
> Which Process Areas belong to Level 5?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.7 CMMI Process Areas by Level
>
> | Level | Name | Focus | Process Areas |
> |:-----:|------|-------|---------------|
> | **5** | Optimizing | Continuous process improvement | OID, CAR |
> | **4** | Quantitatively Managed | Quantitative management | OPP, QPM |
> | **3** | Defined | Process standardization | RD, TS, PI, VER, VAL, OPF, OPD, OT, IPM, RSKM, DAR |
> | **2** | Managed | Basic project management | REQM, PP, PMC, SAM, MA, PPQA, CM |
> | **1** | Initial | Work harder | *(none defined - ad hoc)* |
>
> #### 4.8 Process Areas by Category
>
> | Category | Process Areas | Levels |
> |----------|---------------|--------|
> | **Process Management** | OPF, OPD, OT, OPP, OID | 3-5 |
> | **Project Management** | PP, PMC, SAM, IPM, RSKM, QPM | 2-4 |
> | **Engineering** | REQM, RD, TS, PI, VER, VAL | 2-3 |
> | **Support** | CM, PPQA, MA, DAR, CAR | 2-5 |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 406 — Q10

> [!question] Question
> What changed between CMMI v1.3 and v2.0?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.2 What is CMMI?
>
> CMMI (Capability Maturity Model Integration) is a **best practice framework** providing structured guidance for process improvement.
>
> **How Organizations Use Frameworks:**
> - Qualify/rank suppliers
> - Gap analysis ("Where are we vs. where should we be?")
> - Improvement roadmap
> - Shared vision across teams
>
> **Major Frameworks Comparison:**
>
> | Framework | Focus |
> |-----------|-------|
> | **ISO 9001** | Quality management systems |
> | **CMMI** | Process maturity (software development) |
> | **ITIL** | IT service management |
>
> #### 4.10 CMMI v1.3 vs v2.0 Changes
>
> | Aspect | CMMI v1.3 | CMMI v2.0 |
> |--------|-----------|-----------|
> | Structure | 3 constellations (DEV, SVC, ACQ) | Single unified model |
> | Process Areas | 22 Process Areas | 20 Practice Areas |
> | Levels | ML 1-5, CL 0-3 | ML 1-5, CL 1-5 |
> | Agile support | Challenging | Native integration |
> | Appraisal | SCAMPI A/B/C | Benchmark, Sustainment, Action |
>
> > **Key Insight:** CMMI v2.0 was redesigned with Agile, SAFe, and DevSecOps in mind.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 407 — Q1

> [!question] Question
> For each of the three filters in Pfeffer's One-Eighth Rule, describe one specific mitigation strategy from the change management literature that helps an organization pass through that filter.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.5 The One-Eighth Rule
>
> Jeff Pfeffer  explains why only **12.5%** of organizations see full benefits from improvement initiatives:
>
> | Stage | Filter | Organizations Remaining |
> |-------|--------|-------------------------|
> | Start | All organizations | 100% |
> | **Belief** | Only half believe the evidence | 50% |
> | **Systemic approach** | Only half try comprehensive change | 25% |
> | **Persistence** | Only half persist long enough | **12.5%** |
>
> ```vega-lite
> {
>   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
>   "title": "The One-Eighth Rule: SPI Success Funnel",
>   "width": 300,
>   "height": 200,
>   "data": {
>     "values": [
>       {"stage": "1. Start", "percentage": 100, "order": 1},
>       {"stage": "2. Believe", "percentage": 50, "order": 2},
>       {"stage": "3. Systemic", "percentage": 25, "order": 3},
>       {"stage": "4. Persist", "percentage": 12.5, "order": 4}
>     ]
>   },
>   "mark": {"type": "bar", "cornerRadiusEnd": 4},
>   "encoding": {
>     "y": {"field": "stage", "type": "nominal", "sort": {"field": "order"}, "title": null},
>     "x": {"field": "percentage", "type": "quantitative", "title": "Organizations (%)"},
>     "color": {
>       "field": "percentage",
>       "type": "quantitative",
>       "scale": {"scheme": "reds", "reverse": true},
>       "legend": null
>     }
>   }
> }
> ```
>
> **Why Organizations Fail at Each Stage:**
>
> 1. **Belief Filter (50% → 50%):**
>    - "Our situation is different"
>    - "That won't work here"
>    - Resistance to change based on past failures
>
> 2. **Systemic Filter (50% → 25%):**
>    - Isolated "checkbox" changes instead of comprehensive reform
>    - Implementing tools without changing processes
>    - Training without cultural shift
>
> …
>
> #### The One-Eighth Rule
>
> According to Jeff Pfeffer :
> - Only **one-half** of organizations believe the evidence connecting management practices to business results
> - Only **one-half** of believers try comprehensive systemic change (not just isolated fixes)
> - Only **one-half** of those persist long enough to see benefits
> - **Result:** Only 1/8 (12.5%) of organizations see the full results of SPI

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 408 — Q2

> [!question] Question
> List the top three adoption barriers to SPI identified in Shelat 2025 (with percentages). Propose a concrete mitigation strategy for each.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.5 Adoption Barriers
>
> **Primary Barriers (2025 Study)** :
>
> | Barrier | Percentage |
> |---------|------------|
> | Employee resistance | **42%** |
> | Resistance to change | **38%** |
> | Documentation burden | **32-38%** |
> | Knowledge gaps | **34%** |
> | Process vs. agility tension | **25-30%** |
>
> #### Barriers to Success
>
> A 2025 study of CMMI adoption found:
>
> | Barrier | Percentage |
> |---------|------------|
> | Employee resistance | 42% |
> | Documentation overhead | 38% |
> | Process vs. agility tension | 25-30% |
> | Ineffective training | 25-30% |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 409 — Q3

> [!question] Question
> Compare operational changes vs. cultural changes in process improvement. Give one concrete example of an SPI initiative that failed because only the operational level was addressed.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Why Process Improvement?
>
> Software Process Improvement (SPI) is a systematic approach to enhancing organizational performance by modifying technical, organizational, and cultural structures to achieve better business outcomes .
>
> #### Process Improvement
>
> Software Process Improvement (SPI) is a systematic approach to enhancing organizational performance through deliberate modification of technical, organizational, and cultural structures.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 410 — Q4

> [!question] Question
> Describe the two levels of organizational change identified by Andrews & Stalick. Why must both levels change for process improvement to be sustainable?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Two Levels of Organizational Change
>
> Andrews & Stalick  identified two levels that must both change:
>
> **Operational Changes (Easier, Visible):**
>
> | Component | Examples |
> |-----------|----------|
> | **Structure** | Who reports to whom, team composition |
> | **Process** | Steps, procedures, workflows |
> | **Technology** | Tools, platforms, automation |
> | **Rewards** | Promotions, incentives, recognition |
>
> **Cultural Changes (Harder, Deeper):**
>
> | Component | Examples |
> |-----------|----------|
> | **Mental models** | How people think about problems |
> | **Power structures** | Who has influence and why |
> | **Dissent tolerance** | Protection for alternative viewpoints |
> | **Problem framing** | Willingness to re-examine from ground up |
>
> **Why Cultural Change Matters:**
>
> | Without Cultural Shift | With Cultural Shift |
> |------------------------|---------------------|
> | Old behaviors persist | New behaviors adopted |
> | New processes gamed | Processes followed in spirit |
> | Improvements abandoned under stress | Practices retained during crisis |
> | Return to "the way we've always done it" | Permanent transformation |
>
> > **Key Insight:** Culture is "the set of rules you have to follow to have a fast-track career." If questioning isn't rewarded, people stop questioning.
>
> #### Two Levels of Change
>
> Process improvement must address two distinct levels :
>
> | Level | Components |
> |-------|------------|
> | **Operational** | Organization charts, process structures (what, when, how), reward structures (promotions, incentives) |
> | **Cultural/Values** | Mental models, power structures that protect alternative viewpoints, willingness to re-examine problems from ground up |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

### Card 411 — Q5

> [!question] Question
> What are the top 3 critical success factors for SPI based on research? Why is management commitment ranked #1?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.4 Critical Success Factors
>
> Research consistently identifies these top factors :
>
> | Rank | Factor | Evidence |
> |------|--------|----------|
> | 1 | **Management Commitment** | #1 in ITIL, Six Sigma, Lean Sigma surveys |
> | 2 | Cultural Change | Learning culture over blame culture |
> | 3 | Training | Experiential, role-based, hands-on |
> | 4 | Communication | Clear, consistent messaging |
> | 5 | Staff Involvement | Developer-driven, not just top-down |
>
> **Why Management Commitment is #1:**
>
> Without visible leadership as "champions":
> - Resources not allocated
> - Improvement time lost to "firefighting"
> - Desired behaviors not modeled
> - Initiatives seen as temporary
>
> **Research Data** :
>
> | Success Factor | Impact |
> |----------------|--------|
> | Leadership-driven change | 42% cite as key enabler |
> | Role-based training | 38% cite as key enabler |
> | Phased rollout with pilots | 30% resistance reduction |
>
> #### Critical Success Factors for SPI
>
> Research consistently highlights that technical updates alone are insufficient for process maturity .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/03-process/RQ-A2-Proc.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/03-process/RQ-A2-Proc.md)

## Industry Practices (12)

### Card 412 — Question 1: The Test Pyramid

> [!question] Question
> **Question 1: The Test Pyramid**
>
> Google recommends a 70/20/10 distribution for small (unit), medium (integration), and large (E2E) tests.
>
> Explain why this ratio exists. What problems occur when teams have an "inverted pyramid" with mostly E2E tests and few unit tests?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 1.1 The Test Pyramid (70/20/10)
>
> **What is it?**
> The test pyramid is a model for organizing tests by scope, speed, and cost. The base (widest) contains the most tests; the top (narrowest) contains the fewest.
>
> **The Three Levels:**
>
> | Level | Name | Scope | Speed | Ratio |
> |-------|------|-------|-------|-------|
> | Base | **Small tests** (Unit) | Single function/class | Milliseconds | **70%** |
> | Middle | **Medium tests** (Integration) | 2+ modules | Seconds | **20%** |
> | Top | **Large tests** (E2E) | Entire system | Minutes | **10%** |
>
> **Google Scale:** 150M tests/day, 5.5M test targets, ~1 commit/second
>
> **Why This Ratio Works:**
> - **Small tests:** Fast to run, deterministic, easy to debug. When a small test fails, you know *exactly* which function broke.
> - **Medium tests:** Verify component integration. May use real implementations (e.g., in-memory databases) instead of mocks.
> - **Large tests:** Validate critical user journeys. When a large test fails, you might spend hours debugging across 20 services.
>
> > "User-facing projects may increase medium/large test proportion. Infrastructure projects use significantly more small tests."
>
> **Concrete Example - E-commerce Checkout:**
>
> ```
> Small tests (70%):
>   - validateCreditCard() returns true for valid Visa
>   - calculateTax() handles edge case of $0 subtotal
>   - formatCurrency() displays correct decimal places
>
> Medium tests (20%):
>   - PaymentService correctly calls StripeAPI mock
>   - OrderService persists to in-memory database
>   - InventoryService reduces stock after purchase
>
> Large tests (10%):
>   - User can add item, checkout, pay, receive confirmation email
>   - Failed payment shows error and preserves cart
> ```
>
> …
>
> #### 1.3 Test Selection & Prioritization
>
> **Dependency-Based Selection (Google)** :
> - **Build graph:** In-memory graph of build dependencies
> - **Transitive mapping:** Follow edges to find all tests depending on changed code
> - **Affected test selection:** Run only minimal set of affected tests
> - **Result:** Faster feedback, can run tests on every commit at scale
>
> **Prioritization Strategies:**
>
> | Strategy | Description |
> |----------|-------------|
> | **ACC Risk Heat Map** | Red (high risk) - Yellow - Green. Prioritize red areas |
> | **Priority Levels (MS)** | P1, P2, P3. Early milestones = P1 only. Release = all |
> | **70/20/10 Rule** | Prioritize unit tests (fast, deterministic) |
> | **Smoke Tests** | Critical path tests that must pass before submit |
>
> **Test Scheduling by Size:**
>
> | Size | Scheduling |
> |------|------------|
> | **Small** | Run immediately, highest priority |
> | **Medium** | Queue after small tests |
> | **Large** | Run in parallel, don't block small tests |
>
> **Microsoft Priority Model** :
>
> | Milestone | Tests Required |
> |-----------|----------------|
> | M1 | P1 only |
> | M2 | P1 + P2 |
> | Release | All tests |
>
> **Benefits of Dependency Graphs:**
> - **Isolation:** Identify exact change where test started failing
> - **Efficiency:** Run minimal tests without sacrificing accuracy
> - **Scale:** Handle changes to common libraries (may trigger thousands of tests)
>
> **Maturity:** Intermediate - Requires build system integration

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/05-practice/RQ-A3-Practice.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/05-practice/RQ-A3-Practice.md)

### Card 413 — Question 2: Test Coverage Limitations

> [!question] Question
> **Question 2: Test Coverage Limitations**
>
> Microsoft targets 80% code coverage at final release, yet the book states "coverage ≠ quality."
>
> Explain the difference between what coverage measures and what it cannot detect. Give a concrete example where 100% coverage fails to catch a bug.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 100% coverage, but has a bug!
>
> def divide(a, b):
>     return a / b  # No handling for b=0
>
> def test_divide():
>     assert divide(10, 2) == 5  # Covers the function
>     # But what about divide(10, 0)? Not tested!
> ```
>
> **Limitations of Coverage:**
> - **Quality vs Quantity** - 100% coverage doesn't guarantee absence of bugs
> - **Missing logic** - Coverage doesn't detect functionality that was never written
> - **Exercising bugs** - Retrofitted tests may exercise buggy behavior, not correct behavior
> - **False confidence** - High unit coverage doesn't prove E2E functionality
> - **Production gaps** - Test environments != production conditions
>
> > "Coverage finds gaps, tests find bugs."
>
> **Practical Rule:**
> 80% coverage is a good target. The last 20% often includes error handlers and edge cases that are expensive to test but rarely run.
>
> **Anti-patterns to Avoid:**
> - Treating coverage as quality proof (high coverage != good tests)
> - Retrofitting tests to bad code (may exercise bugs)
> - Ignoring E2E coverage (unit coverage alone insufficient)
> - Gaming coverage metrics (testing getters/setters vs logic)
>
> **Maturity:** Starter - Coverage tools available in most languages
>
> #### 1.5 Test Coverage (80% Target)
>
> **The Practice:**
> - **Coverage is a standard metric** but must be part of broader quality strategy, not an end in itself
> - **Tiered thresholds** increase as product nears release or reaches higher maturity
> - **70/20/10 rule** ensures majority of coverage comes from fast, deterministic unit tests
>
> **Microsoft Milestone Targets** :
>
> | Milestone | Code Coverage |
> |-----------|---------------|
> | M2 | 65% |
> | M3 | 75% |
> | Final Release | **80%** |
> | Feature Crews | 80% unit test for new code |
>
> **Google Test Certified Levels** :
>
> | Level | Total Coverage | Small Test Coverage |
> |-------|----------------|---------------------|
> | Level 2 | 50% incremental | 10% |
> | Level 4 | 40% | 25% |
> | Level 5 | 60% | 40% |
>
> **Coverage Measurement Types:**
> - **Statement coverage** - whether each line of code was executed
> - **Branch coverage** - whether each logical block was exercised
> - **Mutation coverage** - whether tests detect code changes (stronger)
>
> **Why 100% Coverage Can Be Misleading:**
>
> ```python

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/05-practice/RQ-A3-Practice.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/05-practice/RQ-A3-Practice.md)

### Card 414 — Question 3: Code Review Speed and Size

> [!question] Question
> **Question 3: Code Review Speed and Size**
>
> Google's code review data shows median latency <4 hours and median change size of 24 lines.
>
> Why are small, fast reviews important? What happens to review quality when changes exceed 100 lines?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Code Review at Scale
>
> Sadowski et al. (2018) analyzed **9 million code reviews** at Google involving 25,000+ developers, providing unprecedented empirical data on modern code review practices :
>
> | Metric | Finding |
> |--------|---------|
> | Reviews analyzed | **9 million** (Jan 2014 - Jul 2016) |
> | Median review latency | **Under 4 hours** |
> | Small changes | Feedback often in **under 1 hour** |
> | Change size | 35%+ modify only a single file |
> | Median lines modified | **24 lines** |
> | Reviewer count | Median of **1 reviewer** |
> | Satisfaction | **97%** satisfied with Critique tool |
>
> #### Key Insight: Education Over Defect Detection
>
> Unlike traditional code inspection focused on finding defects, Google's code review prioritizes **knowledge transfer and maintainability**:
>
> - **Readability certification**: Every change requires approval from a language-certified reviewer
> - **New hire learning**: Developers under 1 year receive **2x more comments** per change
> - **Lightweight process**: 80%+ of changes require at most one iteration
> - **Tool integration**: Tricorder static analysis integrated directly in review UI
>
> > "The foremost reason for introducing code review at Google was to improve code understandability and maintainability."
>
> #### 2.1 Traditional Code Review Process
>
> **Google Code Review Workflow** :
>
> 1. **Create Change List (CL)** - Package code changes (few lines to hundreds)
> 2. **Pre-submit automation** - Static analysis (Tricorder), unit tests
> 3. **Route for review** - Submit to qualified reviewers
> 4. **Iterative feedback** - Address comments, repeat until approved
> 5. **Final signoff** - Move to submit queue, verify build stays green
>
> **Readability Certification:**
> - **What:** Language-specific certification (C++, Java, Python, JavaScript)
> - **Requirement:** Either have readability OR get signoff from certified reviewer
> - **Purpose:** Ensure code quality baseline, consistent codebase style
> - **Outcome:** Codebase "looks like one person wrote it"
>
> **What Reviewers Look For:**
>
> | Focus | Description |
> |-------|-------------|
> | **Correctness** | Logic errors that tests might miss |
> | **Standards** | Style guide adherence, data structure choices |
> | **Understandability** | Security/reliability properties obvious to future maintainers |
> | **Knowledge sharing** | Educational feedback for author |
> | **Minimalism** | YAGNI - eliminate over-engineering |
>
> **Key Metrics** :
>
> | Metric | Value |
> |--------|-------|
> | Median latency | **< 4 hours** |
> | Median change size | **24 lines** |
> | Tool satisfaction | **97%** |
> | Volume | ~50,000 reviews/day (via Tricorder) |
>
> **Review Principles:**
> - **No solo commits** - Multi-party authorization required
> - **Just-in-time notifications** - Keep developers unblocked
> - **One-click fixes** - Suggested auto-fixes for common issues
> - **Low friction** - Automation handles mechanical details
>
> **Microsoft Effective Review Practices** :
>
> …

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/05-practice/RQ-A3-Practice.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/05-practice/RQ-A3-Practice.md)

### Card 415 — Question 4: Static Analysis Adoption

> [!question] Question
> **Question 4: Static Analysis Adoption**
>
> Google disables any static analysis check with >10% false positive rate.
>
> Explain why false positives matter for tool adoption. What happens when developers receive too many false warnings?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 2.2 Static Analysis (<10% False Positive Rule)
>
> **Industry Tools:**
>
> | Company | Tool | Focus |
> |---------|------|-------|
> | Google | **Tricorder** | Central platform for all checkers |
> | Google | Error Prone | Java bugs |
> | Google | Clang-Tidy | C/C++ |
> | Microsoft | **PREfast** | Native code analysis |
> | Microsoft | Managed code analyzers | .NET |
>
> **When It Runs:**
> 1. **IDE** - Underlines problems as developer types (fastest feedback)
> 2. **Pre-submit/Code Review** - Integrated into review UI
> 3. **CI Pipeline** - Gated checks that block merge
> 4. **Milestone Gates** - Part of exit criteria
>
> **What It Catches:**
> - **Bug patterns:** Null pointer dereference, uninitialized memory, integer conversion errors
> - **Security vulnerabilities:** SQL injection, XSS (injection sinks detection)
> - **API conformance:** Deprecated/risky API usage flagged at compile time
> - **Style/readability:** Enforce language style guides for consistency
>
> **Why <=10% False Positives?**
>
> | FP Rate | Developer Response |
> |---------|-------------------|
> | <5% | Trust and fix |
> | 10% | Grudging acceptance |
> | >15% | Ignore the tool |
> | >30% | Demand removal |
>
> **Effectiveness Metrics:**
> - **10% false positive rule** - Google disables checks with >10% noise
> - **"Not useful" feedback** - Tricorder lets devs report unhelpful warnings
> - **2 orders of magnitude** - XSS vulnerabilities reduced with safe types
> - **Auto-fixes** - One-click fixes encourage adoption
>
> **Adoption Strategies:**
> - **Integrate into code review** - Make results visible where developers work
> - **Minimize friction** - Auto-suggest fixes, low false-positive rate
> - **Incremental rollout** - Enforce on new code, exempt legacy until cleaned
> - **Developer feedback loop** - Let devs report "not useful" to tune tools
>
> …
>
> #### When Static Analysis Runs
>
> | Stage | Purpose | Feedback Time |
> |-------|---------|---------------|
> | **IDE** | Underlines problems as you type | Immediate |
> | **Pre-submit** | Integrated into code review UI | Before merge |
> | **CI Pipeline** | Blocks merge if not green | Minutes |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/05-practice/RQ-A3-Practice.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/05-practice/RQ-A3-Practice.md)

### Card 416 — Question 5: Canary Deployment

> [!question] Question
> **Question 5: Canary Deployment**
>
> Canary deployment exposes only 1% of users to new code initially.
>
> Explain how canary limits "blast radius." Calculate: if a bug causes 20% errors in the new code, what is the overall error rate with a 5% canary vs no canary?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 3.2 Deployment Strategies (Canary at 1%)
>
> **Strategy Comparison:**
>
> | Strategy | Description | Rollback | Resources | Best For |
> |----------|-------------|----------|-----------|----------|
> | **Canary** | Deploy to ~1% first | Stop rollout | 1x + canary | Most changes |
> | **Blue-Green** | Two environments, switch router | Instant switch | 2x | Database migrations |
> | **Progressive** | 1% - 10% - 50% - 100% | Stop at any stage | 1x | Major features |
> | **Feature Flags** | Decouple feature from binary | Disable flag | 1x | A/B testing |
>
> **Canary Process at Google** :
> 1. Deploy Release Candidate to small segment (~1%)
> 2. Compare metrics against "Live" control
> 3. Monitor for errors, latency regressions
> 4. If OK, expand to next stage
> 5. If problems, halt and rollback
>
> **Staged Rollout Percentages:**
>
> | Stage | Population | Purpose |
> |-------|------------|---------|
> | **Canary** | ~1% | Initial risk detection |
> | **Expand** | ~10% | Broader validation |
> | **Wide** | ~50% | Near-full confidence |
> | **Full** | 100% | Complete rollout |
>
> **Canary Math - Why It Limits Blast Radius:**
> ```
> Scenario: Canary has a bug causing 20% error rate
>
> Without canary: 100% of users see 20% errors = 20% overall error rate
> With 5% canary: Only 5% of users affected = 1% overall error rate
>
> Your SLO of 99.9% is preserved while you detect and fix the bug!
> ```
>
> **VALET Framework (Home Depot):**
> - **V**olume - traffic handled
> - **A**vailability - uptime
> - **L**atency - response speed
> - **E**rrors - failure rate
> - **T**ickets - manual interventions
>
> **Maturity:** Intermediate - Requires deployment automation
>
> #### Error Budget Math for Canary
>
> > 5% canary serving 20% errors = only 1% overall error rate (SLO preserved)
>
> This allows teams to detect issues before they affect the full user base.

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/05-practice/RQ-A3-Practice.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/05-practice/RQ-A3-Practice.md)

### Card 417 — Question 6: SLIs, SLOs, and SLAs

> [!question] Question
> **Question 6: SLIs, SLOs, and SLAs**
>
> The SRE model defines three levels: SLI (indicator), SLO (objective), and SLA (agreement).
>
> Explain the hierarchy. Why should your internal SLO be stricter than the external SLA you promise customers?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.1 SLIs, SLOs, and SLAs
>
> **The Hierarchy:**
>
> ```
> SLI (Indicator) -> What you MEASURE
>     |
> SLO (Objective) -> What you AIM FOR internally
>     |
> SLA (Agreement) -> What you PROMISE customers (with penalties)
> ```
>
> **Definitions** :
>
> | Term | Definition | Example |
> |------|------------|---------|
> | **SLI** | Service Level Indicator - measurable metric | "Percentage of requests faster than 200ms" |
> | **SLO** | Service Level Objective - internal target | "We aim for 99.95% of requests < 200ms" |
> | **SLA** | Service Level Agreement - external contract | "If <99.9%, customer gets credit" |
>
> **Why SLO > SLA?**
> Your internal target (SLO) should be stricter than your customer promise (SLA). This gives you a buffer to catch problems before you violate the contract.
>
> ```
> Example:
>   SLA to customers: 99.9% availability
>   Internal SLO:     99.95% availability
>
>   If you drop to 99.92%, you:
>   + Still meet SLA (no refunds)
>   - Violated SLO (trigger reliability work)
> ```
>
> **Common SLIs:**
>
> | Service Type | SLI | Formula |
> |--------------|-----|---------|
> | Request-driven | Availability | Successful requests / Total requests |
> | Request-driven | Latency | Requests < 100ms / Total requests |
> | Data pipeline | Freshness | Data updated < threshold / Total |
>
> **Availability Targets:**
>
> | Target | Downtime/year | Use Case |
> |--------|---------------|----------|
> | 99.5% | ~1.8 days | Non-critical apps |
> | 99.9% (3 nines) | ~8.7 hours | Internal systems |
> | 99.95% | ~4.4 hours | Production services |
> | 99.99% (4 nines) | **~52 minutes** | Shared infrastructure |
>
> > "100% reliability is the wrong target - it leaves no room for change and costs more than the marginal utility it provides."
>
> **Maturity:** Intermediate - Requires monitoring infrastructure
>
> #### SRE vs Traditional Operations
>
> | Aspect | Traditional Operations | SRE Approach |
> |--------|----------------------|--------------|
> | **Philosophy** | Manual system maintenance | Automation and systematic problem-solving |
> | **Posture** | Reactive incident response | Proactive engineering and prevention |
> | **Success Metric** | System uptime | SLOs, error budgets, quantitative analysis |
> | **Reliability Target** | Best effort | "Four nines" (99.99%) with data-driven decisions |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/05-practice/RQ-A3-Practice.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/05-practice/RQ-A3-Practice.md)

### Card 418 — Question 7: Error Budgets

> [!question] Question
> **Question 7: Error Budgets**
>
> Error budget equals 100% minus SLO. If you have a 99.9% SLO and serve 3 million requests per month:
>
> Calculate your monthly error budget. What actions does a team take when the error budget is exhausted? What can they do when budget remains?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.2 Error Budgets
>
> **What is an Error Budget?**
> An error budget is the maximum amount of unreliability you can "spend" before you must stop shipping features and focus on reliability.
>
> **Formula** :
> ```
> Error Budget = 100% - SLO
> ```
>
> **Worked Example - Monthly Budget:**
> ```
> SLO: 99.9% availability
> Error Budget: 100% - 99.9% = 0.1%
>
> If you serve 3 million requests/month:
>   Allowed errors = 3,000,000 x 0.001 = 3,000 errors
>
> If you serve 10 million requests/month:
>   Allowed errors = 10,000,000 x 0.001 = 10,000 errors
> ```
>
> **Real Scenario - The Feature Freeze Decision:**
> ```
> Week 1: 500 errors (2,500 remaining for month)
> Week 2: 800 errors (1,700 remaining)
> Week 3: Major outage causes 2,000 errors -> BUDGET EXHAUSTED
>
> Result: All new features frozen until next month.
> Team must focus on reliability improvements.
> ```
>
> **Budget Exhausted -> Actions:**
>
> | Action | Description |
> |--------|-------------|
> | **Feature freeze** | Halt all new launches |
> | **Reliability focus** | Pivot to reliability work |
> | **Production freeze** | Minimize change risk |
> | **Mandatory postmortem** | If single incident uses >20% of 4-week budget |
>
> **Budget Remaining -> Benefits:**
> - Deploy features aggressively
> - Allow risky experiments
> - Favor speed over safety checks
>
> **Burn Rate Explained:**
> Burn rate measures how fast you're consuming your budget.
>
> ```
> Burn rate 1  = Using budget at exactly sustainable pace
> Burn rate 10 = Using budget 10x too fast (30-day budget gone in 3 days!)
>
> Alert thresholds:
> - Burn rate 2 for 1 hour  -> Page (immediate response)
> - Burn rate 6 for 6 hours -> Ticket (scheduled fix)
> ```
>
> **Extreme Example:**
> > 99.999% monthly availability means 100% outage exhausts entire budget in **26 seconds**
>
> …
>
> #### Budget Exhausted → Actions
>
> | Action | Description |
> |--------|-------------|
> | **Feature freeze** | Halt all new feature launches |
> | **Reliability focus** | Pivot engineering to stability work |
> | **Production freeze** | Minimize change risk |
> | **Mandatory postmortem** | Required if >20% budget consumed by single incident |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/05-practice/RQ-A3-Practice.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/05-practice/RQ-A3-Practice.md)

### Card 419 — Question 8: Four Golden Signals

> [!question] Question
> **Question 8: Four Golden Signals**
>
> SRE monitors Latency, Traffic, Errors, and Saturation.
>
> Explain the difference between alerting on "symptoms" vs "causes." Give an example of a bad alert (cause) and a good alert (symptom) for the same underlying issue.

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 4.3 Monitoring & Four Golden Signals
>
> **Core Philosophy:**
> Every collected metric must serve a specific purpose: alerting, debugging, or capacity planning. Measurement is crucial for establishing reality and creating objective foundation for decisions.
>
> **The Four Golden Signals** :
>
> | Signal | What It Tells You | Example Metric | Alert Threshold |
> |--------|-------------------|----------------|-----------------|
> | **Latency** | Is the service fast? | p99 < 200ms | p99 > 500ms |
> | **Traffic** | How much demand? | 1000 req/sec | Unusual spike/drop |
> | **Errors** | Is it working? | 0.1% HTTP 500s | >1% errors |
> | **Saturation** | Will it break soon? | 70% CPU | >85% CPU |
>
> **Practical Example - E-commerce Site:**
> ```
> Normal state:
>   Latency: p99 = 150ms ok
>   Traffic: 500 req/sec ok
>   Errors:  0.05% ok
>   Saturation: 40% CPU ok
>
> Black Friday:
>   Latency: p99 = 800ms ALERT <- Users experiencing delays
>   Traffic: 2000 req/sec    <- Expected spike
>   Errors:  2.5% ALERT      <- Checkout failing
>   Saturation: 95% CPU ALERT <- Need to scale
> ```
>
> **Symptoms vs Causes:**
>
> | Type | Use For | Example |
> |------|---------|---------|
> | Symptoms | Alerting (page on-call) | "The service is slow" |
> | Causes | Debugging | "Database at 90% CPU" |
>
> **Why Page on Symptoms, Not Causes:**
> ```
> Scenario: Database CPU at 95%
>
> Bad alert: "Database CPU high"
>   -> Maybe the database is fine at 95%, or maybe it's not affecting users
>
> Good alert: "Checkout latency > 2 seconds"
>   -> Definitely affecting users, investigate to find cause
> ```
>
> > "Page on the symptom 'the service is slow', not the cause 'database at 90% CPU'. The cause may not actually affect users."
>
> **Burn Rate Alert Levels:**
>
> …
>
> #### The Four Golden Signals
>
> The SRE Book defines four key metrics that every service should monitor :
>
> | Signal | What It Measures | Example Metrics |
> |--------|------------------|-----------------|
> | **Latency** | Time to serve a request | p50, p95, p99 response time |
> | **Traffic** | Demand on the system | Requests per second, transactions |
> | **Errors** | Rate of failed requests | HTTP 500s / total requests |
> | **Saturation** | Resource utilization | CPU%, memory%, queue depth |

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/05-practice/RQ-A3-Practice.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/05-practice/RQ-A3-Practice.md)

### Card 420 — Question 9: Toil and the 50% Rule

> [!question] Question
> **Question 9: Toil and the 50% Rule**
>
> Google SRE defines "toil" as manual, repetitive, automatable work with no enduring value, and limits it to 50% of SRE time.
>
> Give three examples of toil vs engineering work. Why is the 50% threshold important for team sustainability?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 5.3 Toil Management
>
> **Definition:**
> Toil is repetitive, manual work that lacks enduring value, grows linearly with service size, and could be automated .
>
> **Five Characteristics of Toil:**
>
> | Characteristic | Description |
> |----------------|-------------|
> | **Manual** | Requires human intervention |
> | **Repetitive** | Done over and over again |
> | **Automatable** | Could be done by a machine |
> | **Nontactical** | No lasting strategic value |
> | **No Enduring Value** | Doesn't improve the system permanently |
>
> **The 50% Rule:**
> > "SREs should spend no more than 50% of their time on toil - the rest should be engineering work that reduces future toil."
>
> **Toil Examples vs Engineering:**
>
> | Toil (Bad) | Engineering (Good) |
> |------------|-------------------|
> | Manual deploys | CI/CD pipeline |
> | Alert triage | Better monitoring |
> | Password resets | Self-service portal |
> | Log searches | Dashboards |
>
> **Reduction Strategies:**
>
> | Strategy | Description |
> |----------|-------------|
> | **Engineer out** | Automate the task entirely |
> | **Reject** | Push back on toil requests, propose alternatives |
> | **Human-backed interfaces** | Design systems where humans are last resort |
> | **Melt snowflakes** | Standardize to reduce special cases |
> | **Self-service** | Enable users to help themselves |
>
> **Complexity Toil Warning:**
> > "Automatable" doesn't always mean "should automate" - overly complex automation becomes its own form of toil when it breaks and requires debugging.
>
> **Maturity:** Starter - Can track immediately, automation builds over time
>
> #### Toil Management
>
> **Toil** is work that is manual, repetitive, automatable, tactical, lacks enduring value, and scales linearly with service size .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/05-practice/RQ-A3-Practice.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/05-practice/RQ-A3-Practice.md)

### Card 421 — Question 10: LLM Testing Risks

> [!question] Question
> **Question 10: LLM Testing Risks**
>
> Research shows up to 68.1% of LLM-generated tests may "validate bugs" due to the "intent gap."
>
> Explain what the intent gap means. Why do LLM-generated tests often pass for buggy code? How should developers review AI-generated assertions?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Code Review Research
>
> Microsoft research on code review effectiveness provides guidance for practitioners .
>
> #### LLM-GENERATED TEST (validates the bug!):
>
> def test_calculate_total():
>     assert calculate_total(100) == 101  # "Passes" but is WRONG
> ```
>
> The LLM saw the code returns 101, so it wrote a test expecting 101. The test passes, but the code is wrong!
>
> **Why This Matters:** Up to **68.1%** of LLM-generated test suites may validate bugs by testing what code *does* rather than what it *should do*.
>
> **Mitigation:** Always review LLM-generated assertions against requirements, not just code.
>
> **Maturity:** Advanced - Requires careful human oversight

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/05-practice/RQ-A3-Practice.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/05-practice/RQ-A3-Practice.md)

### Card 422 — Question 11: Chaos Engineering

> [!question] Question
> **Question 11: Chaos Engineering**
>
> Netflix runs Chaos Monkey during business hours to randomly terminate production instances.
>
> Explain the difference between resilience testing and chaos engineering. Why is discovering unknown weaknesses valuable before customers do?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### Part 6: Chaos Engineering & Resilience
>
> {: .note }
> > **See also:** [Testing Practices](04-testing-practices.md) for chaos engineering and shift-right testing, [Site Reliability Engineering](06-site-reliability-engineering.md) for resilience practices.
>
> #### Chaos Engineering
>
> Owotogbe et al. (2024) conducted a multi-vocal literature review of **96 sources** (49 academic + 47 grey literature) on chaos engineering practices pioneered by Netflix .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/05-practice/RQ-A3-Practice.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/05-practice/RQ-A3-Practice.md)

### Card 423 — Question 12: AI Agent Trust Tiers

> [!question] Question
> **Question 12: AI Agent Trust Tiers**
>
> The trust tier framework (T0-T3) governs AI agent autonomy, from observational (T0) to full autonomy (T3).
>
> What are the requirements for an AI agent to reach T3? Why does research show a 37.6% increase in vulnerabilities when AI iterates without human gates?

> [!answer]- Reveal answer / cues — source notes
> **Relevant SQRBOK source notes — active-recall cue, not a model answer.**
>
> #### 7.2 Trust Tiers (T0-T3)
>
> **Why Trust Tiers?**
> You wouldn't give a new intern access to delete production databases. Similarly, AI agents need to earn trust gradually through demonstrated competence.
>
> **Framework for scaling agent autonomy:**
>
> | Tier | Name | Capability | Example |
> |------|------|------------|---------|
> | T0 | Observational | Summaries only | "Here's what I found in the logs" |
> | T1 | Approval-Gated | Needs human signature | "I recommend this fix. Approve?" |
> | T2 | Narrow Autonomy | Limited actions | Can rollback if <20% traffic affected |
> | T3 | Conditional | Full autonomy + audit | Auto-deploys with continuous monitoring |
>
> **Scenario - Promoting an Agent Through Tiers:**
>
> ```
> Month 1 (T0): Agent summarizes PR changes, suggests tests
>   -> Human writes all code, agent just advises
>
> Month 2 (T1): Agent writes test code, human reviews and approves
>   -> "I generated 5 tests. Here they are for your review."
>
> Month 3 (T2): Agent can auto-fix failing tests if fix is <10 lines
>   -> Small fixes happen automatically, big changes need approval
>
> Month 6 (T3): Agent handles routine bug fixes end-to-end
>   -> Creates PR, gets review, merges, monitors deployment
>   -> REQUIRES: 95% success rate, 0 policy violations over 100 deploys
> ```
>
> #### Convergent Quality Engineering Framework
>
> The Convergent Quality Engineering framework proposes a holistic integration of shift-left and shift-right methodologies into a continuous quality loop .

> [!info]- Source
> [SQRBOK handbook](https://sqrbok.github.io/organization/05-practice/RQ-A3-Practice.html) · [source Markdown](https://github.com/sqrbok/sqrbok-preview/blob/main/content/organization/05-practice/RQ-A3-Practice.md)
