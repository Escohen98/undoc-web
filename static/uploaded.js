/*
 * Copyright © Eric Cohen 2023
 * Script to toggle key button.
 */

(function() {
    window.addEventListener("load", initialize)

  //Initializes key button
  function initialize() {
    document.getElementById("key-button").addEventListener("click", toggleKey);
    buildToolTip()
  }

  /*
   * Toggles the key's hidden state
   * I know there's a toggle function, but I can't find it,
   * so I'm going to use an if statement
   */
  function toggleKey() {
    //Key div
    key = document.getElementById("keys");
    if (key.hidden) {
        key.hidden = false;
    } else {
      key.hidden = true;
    }
  }

  //Found this online. Lost the link.
  //Creates a tooltip for the spans 
  function buildToolTip() {
    var spans = document.getElementsByTagName('span');
    // Create a div to use as a tooltip
    var tooltip = document.createElement('div');
    tooltip.style.display = 'none';
    tooltip.style.position = 'fixed';
    tooltip.style.background = '#eee';
    tooltip.style.border = '1px solid #333';
    tooltip.style.padding = '5px';
    tooltip.style.zIndex = '1000';
    document.body.appendChild(tooltip);

    // Iterate over each span
    for(var i=0; i<spans.length; i++) {
      // Add a mouseover event listener to each span
      spans[i].addEventListener('mouseover', function(event) {
          // Get the tag from the class name
          var tag = this.className;

          // Construct the tooltip text with a switch statement
          var description = getDescription(tag);

          // Set the tooltip text
          tooltip.innerHTML = this.innerHTML + ': ' + description;

          // Position the tooltip
          tooltip.style.left = (event.pageX + 20) + 'px';
          tooltip.style.top = (event.pageY + 20) + 'px';

          // Show the tooltip
          tooltip.style.display = 'block';
      });
      spans[i].addEventListener('mouseout', function(event) {
          tooltip.style.display = 'none';
      });
    }
  }

  /*
   * Get each word description.
   * This is going to be fun...
   */
   function getDescription(tag) {
     let description = "";
     switch(tag) {
        case 'CC':
            description = 'Coordinating Conjunction';
            break;
        case 'LS':
            description = 'List Item Marker';
            break;
        case 'MD':
            description = 'Modal';
            break;
        case 'RP':
            description = 'Particle';
            break;
        case 'TO':
            description = '"to" as Preposition or Infinitive';
            break;
        case 'CD':
            description = 'Cardinal Number';
            break;
        case 'PRP':
            description = 'Personal Pronoun';
            break;
        case 'PRP$':
            description = 'Possessive Pronoun';
            break;
        case 'WP':
            description = 'Wh-Pronoun';
            break;
        case 'DT':
            description = 'Determiner';
            break;
        case 'PDT':
            description = 'Predeterminer';
            break;
        case 'POS':
            description = 'Possessive Ending';
            break;
        case 'WDT':
            description = 'Wh-Determiner';
            break;
        case 'EX':
            description = 'Existential There';
            break;
        case 'UH':
            description = 'Interjection';
            break;
        case 'JJ':
            description = 'Adjective';
            break;
        case 'JJR':
            description = 'Adjective, Comparative';
            break;
        case 'JJS':
            description = 'Adjective, Superlative';
            break;
        case 'RB':
            description = 'Adverb';
            break;
        case 'RBR':
            description = 'Adverb, Comparative';
            break;
        case 'RBS':
            description = 'Adverb, Superlative';
            break;
        case 'WRB':
            description = 'Wh-Adverb';
            break;
        case 'NN':
            description = 'Noun, Singular or Mass';
            break;
        case 'NNP':
            description = 'Proper Noun, Singular';
            break;
        case 'NNS':
            description = 'Noun, Plural';
            break;
        case 'VB':
            description = 'Verb, Base Form';
            break;
        case 'VBD':
            description = 'Verb, Past Tense';
            break;
        case 'VBG':
            description = 'Verb, Gerund or Present Participle';
            break;
        case 'VBN':
            description = 'Verb, Past Participle';
            break;
        case 'VBP':
            description = 'Verb, Non-3rd Person Singular Present';
            break;
        case 'VBZ':
            description = 'Verb, 3rd Person Singular Present';
            break;
        default:
            description = 'This tag is not recognized.';
      }
      return description;
   }

})();
