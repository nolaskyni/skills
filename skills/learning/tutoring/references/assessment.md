# Assessment

Assess what the user can explain and do, rather than what they have read or find
familiar. Match questions to their goal and judge answers against the material
or reliable sources.

Distinguish assessment of independent understanding from practice with feedback.
Hints, corrections, and explanations change what later answers demonstrate.
Report those answers as assisted, and keep unassessed material separate from
demonstrated gaps.

Offer explanations or practice on gaps afterward in the teaching mode, as the
"Choose the Mode" section in [`SKILL.md`](../SKILL.md) describes.

## Set the Scope

Use the request and prior context to establish the following:

- **Material**: the subject, document, or part of a codebase to assess, and the
  boundaries of the test.
- **Purpose**: what the user needs to demonstrate, such as readiness for an
  exam, understanding a paper, or explaining code before running it.
- **Length**: the requested number of questions, or five by default.
- **Feedback**: deferred to the end by default, or after each answer for
  practice. A request for immediate feedback selects practice.

Ask only about missing information that would materially change the test. State
reasonable defaults for the rest and begin without requiring confirmation.

With deferred feedback, hold correctness judgments, corrections, answer keys,
and teaching until the end. In practice, give brief feedback after each answer
and allow another attempt. If the user changes the feedback timing, follow their
request and distinguish answers given before and after assistance.

Read existing topic notes when available. Within the requested scope, sample
relevant open gaps and revisit previously resolved gaps. Don't let unrelated
gaps displace the material the user asked to assess.

## Write Good Questions

Match each question to the learning objective. Include recall when facts,
terminology, or fluent retrieval matter. To assess understanding, ask the user
to do one of the following:

- Explain a concept in their own words.
- Predict an outcome, including what changes when an assumption fails.
- Trace a process, derivation, or flow of data.
- Justify a choice of method or design and explain its tradeoffs.
- Find the flaw in an argument, derivation, or description.
- Apply an idea to an unfamiliar case.

Avoid trivia unrelated to the objective, trick questions, and wording that gives
away the answer. Prefer free-response questions. When using multiple-choice
questions, make the incorrect options reflect plausible misconceptions.

Base questions on the supplied material or reliable sources. For a document or
codebase, read the relevant passages or code before writing questions.

Before asking a question, establish what makes an answer acceptable and what
evidence supports that judgment. For questions with a definite answer, verify
the answer and reasoning. For open-ended questions, establish a rubric that
allows defensible alternatives.

Use verification appropriate to the subject:

- Check factual claims and interpretations against relevant sources, including
  their context, assumptions, and limitations.
- Check calculations and technical claims through a suitable method, such as
  substitution, a separate derivation, or executing relevant code.
- For interpretive answers, assess support from the material and the reasoning
  rather than agreement with one preferred interpretation.
- For practical skills, assess observable work against explicit criteria.

An agent's confidence or another agent's agreement isn't sufficient
verification. Check for missing cases, conflicting evidence, and valid
alternative answers before using the key or rubric.

If you can't establish a defensible basis for assessment, choose another
question. If uncertainty emerges after asking, leave the item ungraded until it
is resolved. Don't record an unresolved judgment as a learner gap.

### Mathematical Questions

- Make the question unambiguous about the quantities, domain, and given
  assumptions.
- Define notation unless interpreting it is being tested.
- Accept equivalent expressions and valid alternative methods.
- Distinguish notation difficulties from conceptual errors.

Verify these questions and judge their answers by the same rules as other
questions.

### Diagram-Based Questions

Use a diagram when interpreting structure or relationships serves the learning
objective, such as tracing a state transition or finding an incorrect
connection. Choose the representation that fits: Mermaid for compact flows,
dependencies, sequences, and states; a plot for quantitative relationships; or a
sketch when spatial layout matters.

Keep the diagram legible. Explain unfamiliar notation unless that notation is
being tested. Accept answers in words unless constructing a diagram is part of
the objective, and distinguish notation difficulties from gaps in subject
knowledge.

Check labels, annotations, and visible diagram source for answer leakage.
Withhold corrected or completed diagrams until the selected feedback time. If
the user requests help, record the assistance as you would another hint.

Check that the diagram agrees with the intended question and answer. Inspect the
rendered result when rendering is available. Otherwise, provide an equivalent
readable text representation that preserves the question without supplying its
solution.

## Run the Test

Ask one question at a time, identify the topic it covers, and wait for the
user's answer before continuing.

Don't give hints unless the user requests help. Keep the initial answer separate
from later attempts, and record what assistance was supplied. With deferred
feedback, a requested hint applies to that question; it doesn't change the
feedback timing for other questions.

Accept "I don't know" as an answer without pressuring the user to guess. Adjust
difficulty to the answers: probe further after strong answers and return to
fundamentals after answers that reveal gaps.

When feedback is deferred, acknowledge answers without indicating whether they
are correct. Keep clarification questions neutral so they don't reveal the
missing concept or the answer. Give correctness feedback and teaching at the
selected feedback time.

### Pause, Skip, or Stop Early

Let the user skip a question, pause, stop, or change topics. Record skipped or
unanswered questions as unassessed; don't infer a knowledge gap from the
decision to skip.

When the user pauses, preserve the question position, collected answers,
assistance, and feedback timing in the session context or authorized topic
notes. Keep deferred feedback withheld unless the user requests it. Resume from
that point rather than restarting the test.

When the user stops early, provide a brief partial report based on the answers
collected and identify the remaining scope as unassessed. Don't require more
questions or a closing exercise. Honor an explicit request to stop without a
report.

If the user changes topics, keep the scopes distinct rather than implying that
the original test was completed.

## Judge Answers

Evaluate answers against the verified key or rubric, but communicate judgments
only at the selected feedback time. This includes confirmation, partial credit,
and corrections to your key. If the user requests an immediate explanation,
provide it and record the assistance.

Judge the substance and supporting reasoning rather than whether an answer
matches your wording. Accept defensible alternatives. When an answer is
ambiguous, ask a neutral follow-up before judging it.

Distinguish the following:

- **Gap**: an answer reveals missing knowledge or reasoning.
- **Misconception**: an answer expresses an incorrect belief or explanation.
- **Slip**: an isolated execution error despite otherwise sound reasoning.

Give credit for correct parts and identify what is missing or incorrect. Don't
infer understanding the user hasn't expressed, or classify an unassessed point
as a gap.

Recheck the key or rubric when an answer exposes an inconsistency or the user
challenges a judgment. Leave unresolved judgments ungraded, as described in the
"Write Good Questions" section.

If your key or judgment was wrong, acknowledge the error, reassess affected
answers, and correct affected feedback and saved notes.

Keep feedback specific and proportionate. A correct answer needs brief
confirmation rather than inflated praise.

## Report Results

At the end, give a concise report covering the following:

1. **Demonstrated independently**: what the user's unassisted answers support,
   limited to the concepts and difficulty actually sampled.
2. **Assisted**: what they answered after hints, corrections, or explanations.
   Don't count a corrected repetition as independent understanding.
3. **Gaps**: missing knowledge or reasoning revealed by their answers.
4. **Misconceptions**: incorrect beliefs or explanations they expressed, with
   the correction stated briefly.
5. **Not assessed**: relevant parts of the agreed scope that weren't tested.
   Don't classify these as gaps or as understood.
6. **Ungraded**: answered questions whose evaluation remains unresolved, with
   the reason judgment was withheld.
7. **Where to review**: specific passages, files, sources, or exercises that
   address the demonstrated gaps and misconceptions.

Distinguish isolated slips from gaps and misconceptions when discussing errors.
Match the strength of each conclusion to the evidence collected.

Update the topic record according to the established saving preference, as the
"Notes" section in [`SKILL.md`](../SKILL.md) describes. Offer to work on gaps
and misconceptions in the teaching mode.
